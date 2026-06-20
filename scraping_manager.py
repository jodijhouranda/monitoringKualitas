import asyncio
import json
import os
import pandas as pd
from datetime import datetime
from survey_manager import load_config
from tqdm.asyncio import tqdm as async_tqdm

dir_path = os.path.dirname(os.path.abspath(__file__))
region_file = os.path.join(dir_path, "region_mapping.json")

async def _fetch_single(page, url, payload, xsrf_token, sem, retry_count):
    full_url = f"https://fasih-sm.bps.go.id{url}" if url.startswith("/") else url
    async with sem:
        for r in range(retry_count):
            try:
                resp = await page.context.request.post(
                    full_url,
                    headers={
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'X-XSRF-TOKEN': xsrf_token
                    },
                    data=payload
                )
                if resp.ok:
                    res = await resp.json()
                    if isinstance(res, dict) and "searchData" in res:
                        return res["searchData"]
                else:
                    await asyncio.sleep(2)
            except Exception as e:
                await asyncio.sleep(2)
        return []

async def fetch_datatable(page, url, payload_template, xsrf_token, sem, name, retry_count=3):
    p_all = payload_template.copy()
    p_all["filterTargetType"] = "ALL"
    
    data_all = await _fetch_single(page, url, p_all, xsrf_token, sem, retry_count)
    if len(data_all) < 1000:
        return name, data_all
        
    # Hit 1000 limit! Split by TARGET and NON_TARGET
    all_data = []
    for ftype in ["TARGET_ONLY", "NON_TARGET_ONLY"]:
        p_sub = payload_template.copy()
        p_sub["filterTargetType"] = ftype
        data_sub = await _fetch_single(page, url, p_sub, xsrf_token, sem, retry_count)
        
        if len(data_sub) < 1000:
            all_data.extend(data_sub)
        else:
            # Hit 1000 again! Split by ASC and DESC
            p_sub["order"] = [{"column": 0, "dir": "asc"}]
            data_asc = await _fetch_single(page, url, p_sub, xsrf_token, sem, retry_count)
            
            p_sub["order"] = [{"column": 0, "dir": "desc"}]
            data_desc = await _fetch_single(page, url, p_sub, xsrf_token, sem, retry_count)
            
            # Merge and deduplicate
            combined = {row["id"]: row for row in data_asc + data_desc if "id" in row}
            all_data.extend(list(combined.values()))
            
    # Final deduplication just in case
    final_combined = {row["id"]: row for row in all_data if "id" in row}
    return name, list(final_combined.values())

async def scrape_usaha_datatable(page, xsrf_token, custom_name="", max_workers=50):
    cfg = load_config()
    survey_id = cfg.get("survey_period_id")
    region1Id = cfg.get("region1Id")
    if not survey_id or not region1Id:
        print("Survey ID atau Provinsi belum diatur. Jalankan Setup Survei terlebih dahulu.")
        return None

    if not os.path.exists(region_file):
        print("region_mapping.json tidak ditemukan! Jalankan Setup Survei untuk mengunduh wilayah.")
        return None
        
    with open(region_file, "r", encoding="utf-8") as f:
        region_data = json.load(f)
        
    sls_list = []
    # Dynamic region extraction
    for kab_code, kab_info in region_data.items():
        kab_id = kab_info.get("id")
        for kec_code, kec_info in kab_info.get("kecamatan", {}).items():
            kec_id = kec_info.get("id")
            for desa_code, desa_info in kec_info.get("desa", {}).items():
                desa_id = desa_info.get("id")
                for sls_code, sls_info in desa_info.get("sls", {}).items():
                    sls_list.append({
                        "code": sls_code,
                        "kab_id": kab_id,
                        "kec_id": kec_id,
                        "desa_id": desa_id,
                        "sls_id": sls_info.get("id")
                    })
                    
    if not sls_list:
        print("Tidak ada data SLS di region_mapping.json.")
        return None
        
    print(f"\nAkan menarik data Usaha untuk {len(sls_list)} SLS secara paralel.")
    
    sem = asyncio.Semaphore(max_workers)
    api_url = "/app/api/analytic/api/v2/assignment/datatable-all-user-survey-periode"
    
    csv_file = os.path.join(dir_path, "hasil_scraping_temp.csv")
    if os.path.exists(csv_file):
        os.remove(csv_file)
    
    tasks = []
    for sls in sls_list:
        payload = {
            "start": 0, "length": 1000,
            "assignmentExtraParam": {
                "surveyPeriodId": survey_id, 
                "assignmentErrorStatusType": -1,
                "region1Id": region1Id,
                "region2Id": sls["kab_id"],
                "region3Id": sls["kec_id"],
                "region4Id": sls["desa_id"],
                "region5Id": sls["sls_id"]
            },
            "filterTargetType": "ALL",
            "surveyPeriodId": survey_id,
            "region1Id": region1Id,
            "region2Id": sls["kab_id"],
            "region3Id": sls["kec_id"],
            "region4Id": sls["desa_id"],
            "region5Id": sls["sls_id"],
            "columns": [
                {"data": "id", "orderable": True},
                {"data": "codeIdentity", "orderable": True},
                {"data": "data1", "orderable": True},
                {"data": "data2", "orderable": True},
                {"data": "data3", "orderable": True},
                {"data": "data4", "orderable": True},
                {"data": "data5", "orderable": True},
                {"data": "data6", "orderable": True},
                {"data": "data7", "orderable": True},
                {"data": "data8", "orderable": True},
                {"data": "data9", "orderable": True},
                {"data": "data10", "orderable": True},
                {"data": "statusName", "orderable": True}
            ],
            "order": [],
            "search": {"value": "", "regex": False}
        }
        tasks.append(fetch_datatable(page, api_url, payload, xsrf_token, sem, f"SLS {sls['code']}"))
        
    print(f"\n>>> Memulai proses penarikan data (Turbo Mode dengan {max_workers} Koneksi Paralel)...")
    
    batch_records = []
    all_records_count = 0
    total_sls = len(sls_list)
    
    for coro in async_tqdm.as_completed(tasks, desc="Scraping Datatable"):
        sls_code, search_data = await coro
        
        if search_data:
            for row in search_data:
                batch_records.append({
                    "Kode Identitas": row.get("codeIdentity"),
                    "Data 1": row.get("data1"),
                    "Data 2": row.get("data2"),
                    "Data 3": row.get("data3"),
                    "Data 4": row.get("data4"),
                    "Data 5": row.get("data5"),
                    "Data 6": row.get("data6"),
                    "Data 7": row.get("data7"),
                    "Data 8": row.get("data8"),
                    "Data 9": row.get("data9"),
                    "Data 10": row.get("data10"),
                    "Status": row.get("statusName"),
                    "Assignment ID": row.get("id")
                })
                
        if len(batch_records) >= 2000:
            df_batch = pd.DataFrame(batch_records)
            mode = 'a' if os.path.exists(csv_file) else 'w'
            header = not os.path.exists(csv_file)
            df_batch.to_csv(csv_file, mode=mode, header=header, index=False)
            batch_records = []
            
    # Sisa data
    if batch_records:
        df_batch = pd.DataFrame(batch_records)
        mode = 'a' if os.path.exists(csv_file) else 'w'
        header = not os.path.exists(csv_file)
        df_batch.to_csv(csv_file, mode=mode, header=header, index=False)
                
    if os.path.exists(csv_file):
        print("\nMenyimpan data Usaha...")
        df_final = pd.read_csv(csv_file, low_memory=False)
        for col in ["Kode Identitas", "Data 1", "Data 2"]:
            if col in df_final.columns:
                df_final[col] = df_final[col].astype(str).str.replace(r'\.0$', '', regex=True)
                
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        prefix = custom_name if custom_name else "universal_data_usaha"
        output_csv = os.path.join(dir_path, f"{prefix}_{timestamp}.csv")
        df_final.to_csv(output_csv, index=False)
        print(f"BERHASIL! Total {len(df_final)} data lengkap disimpan dengan kilat ke: {output_csv}")
        try: os.remove(csv_file)
        except: pass
        return output_csv
    else:
        print("\nTidak ada data yang didapatkan.")
        return None

def flatten_assignment_data(raw_json):
    flat_data = {}
    if not isinstance(raw_json, dict) or "data" not in raw_json:
        return flat_data
        
    core = raw_json["data"]
    if not isinstance(core, dict):
        return flat_data
        
    flat_data["_id"] = core.get("_id")
    flat_data["survey_period_id"] = core.get("survey_period_id")
    
    if isinstance(core.get("mode"), list) and len(core.get("mode")) > 0:
        flat_data["mode"] = core["mode"][0]
    else:
        flat_data["mode"] = core.get("mode")
        
    flat_data["assignment_error_status_type"] = core.get("assignment_error_status_type")
    
    def parse_answer(ans):
        if ans is None: return ""
        if isinstance(ans, list):
            vals = []
            for item in ans:
                if isinstance(item, dict):
                    if "label" in item: vals.append(str(item["label"]))
                    elif "value" in item: vals.append(str(item["value"]))
                    else: vals.append(str(item))
                else: vals.append(str(item))
            return " | ".join(vals)
        elif isinstance(ans, dict):
            if "label" in ans: return str(ans["label"])
            elif "value" in ans: return str(ans["value"])
            return str(ans)
        return str(ans)
    
    if "pre_defined_data" in core and core["pre_defined_data"]:
        pre_val = core["pre_defined_data"]
        try:
            pre_json = json.loads(pre_val) if isinstance(pre_val, str) else pre_val
            if isinstance(pre_json, dict) and "predata" in pre_json:
                for item in pre_json["predata"]:
                    k = "pre_" + str(item.get("dataKey", ""))
                    flat_data[k] = parse_answer(item.get("answer", ""))
        except Exception: pass
            
    if "data" in core and core["data"]:
        ans_val = core["data"]
        try:
            ans_json = json.loads(ans_val) if isinstance(ans_val, str) else ans_val
            if isinstance(ans_json, dict) and "answers" in ans_json:
                for item in ans_json["answers"]:
                    k = "ans_" + str(item.get("dataKey", ""))
                    flat_data[k] = parse_answer(item.get("answer", ""))
        except Exception: pass
            
    return flat_data

async def fetch_detail_api(page, a_id, xsrf_token, sem, retry_count=3):
    api_url = f"https://fasih-sm.bps.go.id/app/api/assignment-general/api/assignment/get-by-assignment-id?assignmentId={a_id}"
    async with sem:
        last_error = "Unknown"
        for r in range(retry_count):
            try:
                resp = await page.context.request.get(
                    api_url,
                    headers={
                        'Accept': 'application/json',
                        'X-XSRF-TOKEN': xsrf_token
                    }
                )
                if resp.ok:
                    res = await resp.json()
                    if isinstance(res, dict) and res.get("success") == True:
                        flat_row = flatten_assignment_data(res)
                        flat_row["_origin_assignmentId"] = a_id
                        return (a_id, flat_row, None)
                    else:
                        last_error = "Response not successful"
                        await asyncio.sleep(2)
                else:
                    last_error = f"ERROR_{resp.status}"
                    await asyncio.sleep(2)
            except Exception as e:
                last_error = f"Exception: {str(e)}"
                await asyncio.sleep(2)
        return (a_id, None, last_error)

async def scrape_detail_data(page, xsrf_token, input_excel, custom_name="", start_idx=0, end_idx=None, max_workers=50):
    if not os.path.exists(input_excel):
        print(f"File {input_excel} tidak ditemukan.")
        return None
        
    try:
        if input_excel.endswith('.csv'):
            df_existing = pd.read_csv(input_excel, low_memory=False)
        else:
            df_existing = pd.read_excel(input_excel)
            if "Assignment ID" not in df_existing.columns:
                try: df_existing = pd.read_excel(input_excel, sheet_name='Data_Usaha')
                except Exception: pass
                
        if "Assignment ID" not in df_existing.columns:
            print("Kolom 'Assignment ID' tidak ditemukan pada file sumber.")
            return None
            
        all_ids = df_existing["Assignment ID"].dropna().tolist()
        valid_ids = [a_id for a_id in all_ids if str(a_id).strip() and str(a_id) != "TIDAK_DITEMUKAN"]
        unique_assignment_ids = list(dict.fromkeys(valid_ids))
        
        total_found = len(unique_assignment_ids)
        if total_found == 0:
            print("Tidak ada Assignment ID valid yang bisa diproses.")
            return None
            
        if end_idx is None or end_idx > total_found:
            end_idx = total_found
        if start_idx < 0:
            start_idx = 0
            
        unique_assignment_ids = unique_assignment_ids[start_idx:end_idx]
        
        if not unique_assignment_ids:
            print("Rentang baris tidak valid. Tidak ada Assignment ID untuk ditarik.")
            return None
            
        print(f"Berhasil menemukan {total_found} ID. Akan memproses baris {start_idx + 1} hingga {end_idx} (Total: {len(unique_assignment_ids)} ID).")
    except Exception as e:
        print(f"Gagal membaca file sumber: {e}")
        return None

    sem = asyncio.Semaphore(max_workers)
    tasks = []
    for a_id in unique_assignment_ids:
        tasks.append(fetch_detail_api(page, a_id, xsrf_token, sem))
        
    print(f"\n>>> Memulai proses penarikan data detail (Turbo Mode dengan {max_workers} Koneksi Paralel)...")
    
    all_api_data = []
    failed_logs = []
    
    for coro in async_tqdm.as_completed(tasks, desc="Scraping Detail"):
        a_id, result, error = await coro
        if result:
            all_api_data.append(result)
        else:
            failed_logs.append({"Assignment ID": a_id, "Error": error})
            
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    prefix = custom_name if custom_name else "universal_detail_assignment"
    
    if failed_logs:
        error_file = os.path.join(dir_path, f"{prefix}_error_log_{timestamp}.csv")
        pd.DataFrame(failed_logs).to_csv(error_file, index=False)
        print(f"\n[WARNING] Ada {len(failed_logs)} data yang gagal discrap. Log error disimpan ke: {error_file}")

    if all_api_data:
        api_data_df = pd.DataFrame(all_api_data)
        output_file = os.path.join(dir_path, f"{prefix}_{timestamp}.csv")
        
        print(f"\nMenyimpan ke file CSV dengan kilat ({output_file})...")
        try:
            api_data_df.to_csv(output_file, index=False)
            print(f"Data BERHASIL disimpan ke file: {output_file}")
            print(f"Total Detail Didapat: {len(api_data_df)}")
            return output_file
        except Exception as e:
            print(f"\n[ERROR] Terjadi kesalahan saat menyimpan file: {e}")
    else:
        print("\nTidak ada detail informasi yang didapatkan.")
        return None
