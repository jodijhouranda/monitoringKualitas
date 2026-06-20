import asyncio
import json
import os
import pandas as pd
from datetime import datetime
from tqdm.asyncio import tqdm as async_tqdm
from playwright.async_api import async_playwright

# Import dari script yang ada
from survey_manager import load_config
from scraping_manager import fetch_datatable, fetch_detail_api

dir_path = os.path.dirname(os.path.abspath(__file__))
region_file = os.path.join(dir_path, "region_mapping.json")

async def init_browser_jodi():
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False)
    
    state_file = os.path.join(os.path.dirname(dir_path), "state.json")
    if os.path.exists(state_file):
        print("Mencoba login otomatis dengan sesi sebelumnya...")
        context = await browser.new_context(storage_state=state_file)
    else:
        context = await browser.new_context()
        
    page = await context.new_page()
    
    print("Membuka halaman utama...")
    try:
        await page.goto("https://fasih-sm.bps.go.id/")
        await page.wait_for_timeout(3000) # Tunggu sejenak agar sistem bisa redirect jika belum login
    except Exception as e:
        print(f"Gagal memuat halaman: {e}")
    
    # Cek apakah halaman dialihkan ke halaman SSO / Login BPS
    if "login" in page.url.lower() or "sso" in page.url.lower():
        print("\n" + "="*50)
        print("PAUSED UNTUK LOGIN MANUAL")
        print("Sesi Anda belum ada atau sudah kedaluwarsa.")
        print("1. Silakan login ke akun Anda di browser yang terbuka.")
        print("2. Setelah berhasil masuk ke halaman dashboard/awal,")
        print("3. Buka jendela 'Playwright Inspector' dan klik tombol 'Resume' (ikon panah biru) untuk melanjutkan.")
        print("="*50 + "\n")
        
        # Tunggu pengguna login secara manual
        await page.pause()
        
        # Simpan state login untuk digunakan nanti (jika perlu)
        await context.storage_state(path=state_file)
        print("Sesi login telah disimpan untuk pemakaian berikutnya!")
    else:
        print("Login otomatis sukses!")
    
    xsrf_token = ""
    for c in await context.cookies():
        if c["name"] == "XSRF-TOKEN":
            xsrf_token = c["value"]
            break
            
    return p, browser, page, xsrf_token

async def scrape_usaha_datatable_jodi(page, xsrf_token, template_file, custom_name="jodi_data_usaha", max_workers=50):
    cfg = load_config()
    survey_id = cfg.get("survey_period_id")
    region1Id = cfg.get("region1Id")
    if not survey_id or not region1Id:
        print("Survey ID atau Provinsi belum diatur. Silakan jalankan Setup Survei terlebih dahulu di main.py.")
        return None

    if not os.path.exists(region_file):
        print("region_mapping.json tidak ditemukan! Silakan jalankan Setup Survei di main.py.")
        return None

    if not os.path.exists(template_file):
        print(f"File template {template_file} tidak ditemukan!")
        return None
    
    df_template = pd.read_excel(template_file)
    if 'idsls' not in df_template.columns:
        print("Kolom 'idsls' tidak ditemukan di template!")
        return None
        
    target_sls_codes = set(df_template['idsls'].dropna().astype(str).tolist())
    print(f"Ditemukan {len(target_sls_codes)} target SLS dari template.")

    with open(region_file, "r", encoding="utf-8") as f:
        region_data = json.load(f)
        
    sls_list = []
    for kab_code, kab_info in region_data.items():
        kab_id = kab_info.get("id")
        for kec_code, kec_info in kab_info.get("kecamatan", {}).items():
            kec_id = kec_info.get("id")
            for desa_code, desa_info in kec_info.get("desa", {}).items():
                desa_id = desa_info.get("id")
                for sls_code, sls_info in desa_info.get("sls", {}).items():
                    if sls_code in target_sls_codes:
                        sls_list.append({
                            "code": sls_code,
                            "kab_id": kab_id,
                            "kec_id": kec_id,
                            "desa_id": desa_id,
                            "sls_id": sls_info.get("id"),
                            "idsls_asli": sls_code
                        })
                    
    if not sls_list:
        print("Tidak ada target SLS yang cocok dengan region_mapping.json.")
        return None
        
    print(f"Akan menarik data Usaha untuk {len(sls_list)} SLS yang cocok secara paralel.")
    
    sem = asyncio.Semaphore(max_workers)
    api_url = "/app/api/analytic/api/v2/assignment/datatable-all-user-survey-periode"
    
    csv_file = os.path.join(dir_path, "hasil_scraping_temp_jodi.csv")
    if os.path.exists(csv_file):
        os.remove(csv_file)
        
    # Kolom standar yang disyaratkan BPS API (Jika meminta data11, API akan me-return error)
    api_columns = [
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
    ]
    
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
            "columns": api_columns,
            "order": [],
            "search": {"value": "", "regex": False}
        }
        name_str = f"{sls['idsls_asli']}|{sls['code']}"
        tasks.append(fetch_datatable(page, api_url, payload, xsrf_token, sem, name_str))
        
    print(f"\n>>> Memulai proses penarikan data (Turbo Mode dengan {max_workers} Koneksi Paralel)...")
    
    batch_records = []
    
    for coro in async_tqdm.as_completed(tasks, desc="Scraping Datatable Jodi"):
        name_str, search_data = await coro
        sls_asli, sub_code = name_str.split("|")
        
        if search_data:
            for row in search_data:
                record = {k: v for k, v in row.items()}
                record["Assignment ID"] = row.get("id")
                record["ID_SLS"] = sls_asli
                record["ID_SUB_SLS"] = sub_code
                batch_records.append(record)
                
    if batch_records:
        df_final = pd.DataFrame(batch_records)
        
        print("\nMenyiapkan data Usaha...")
        for col in df_final.columns:
            if "data" in col.lower() or col == "codeIdentity":
                df_final[col] = df_final[col].astype(str).str.replace(r'\.0$', '', regex=True)
                
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_csv = os.path.join(dir_path, f"{custom_name}_{timestamp}.csv")
        df_final.to_csv(output_csv, index=False)
        print(f"Data usaha (seluruh variabel) siap untuk proses detail.")
        return output_csv
    else:
        print("\nTidak ada data yang didapatkan dari scraping datatable.")
        return None

async def scrape_detail_data_jodi(page, xsrf_token, input_csv, custom_name="jodi_detail", max_workers=50):
    if not input_csv or not os.path.exists(input_csv):
        print("File CSV input untuk detail tidak valid.")
        return None, None
        
    df_existing = pd.read_csv(input_csv, low_memory=False)
    if "Assignment ID" not in df_existing.columns:
        print("Kolom 'Assignment ID' tidak ditemukan.")
        return None, None
        
    all_ids = df_existing["Assignment ID"].dropna().tolist()
    valid_ids = [a_id for a_id in all_ids if str(a_id).strip() and str(a_id) != "TIDAK_DITEMUKAN"]
    unique_assignment_ids = list(dict.fromkeys(valid_ids))
    
    total_found = len(unique_assignment_ids)
    if total_found == 0:
        print("Tidak ada Assignment ID valid untuk detail.")
        return None, None
        
    print(f"Akan menarik {total_found} ID untuk detail data...")
    sem = asyncio.Semaphore(max_workers)
    tasks = []
    for a_id in unique_assignment_ids:
        tasks.append(fetch_detail_api(page, a_id, xsrf_token, sem))
        
    all_api_data = []
    failed_logs = []
    
    for coro in async_tqdm.as_completed(tasks, desc="Scraping Detail Jodi"):
        a_id, result, error = await coro
        if result:
            all_api_data.append(result)
        else:
            failed_logs.append({"Assignment ID": a_id, "Error": error})
            
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    error_file = None
    if failed_logs:
        error_file = os.path.join(dir_path, f"{custom_name}_error_log_{timestamp}.csv")
        pd.DataFrame(failed_logs).to_csv(error_file, index=False)
        print(f"\n[WARNING] Ada {len(failed_logs)} data detail gagal discrap.")

    output_file = None
    if all_api_data:
        api_data_df = pd.DataFrame(all_api_data)
        output_file = os.path.join(dir_path, f"{custom_name}_{timestamp}.csv")
        api_data_df.to_csv(output_file, index=False)
        print(f"Data detail telah diunduh.")
    else:
        print("Tidak ada detail informasi yang didapat.")
        
    return output_file, error_file

async def main():
    print("==================================================")
    print("      UNIVERSAL BPS SCRAPER - JODI SPECIFIC       ")
    print("==================================================")
    
    print("\nPILIHAN MENU:")
    print("1. Scraping Datatable Saja (Cepat, tapi tidak ada detail data11-data50)")
    print("2. Scraping Datatable + Detail Data (Lengkap, butuh waktu lebih lama)")
    pilihan = input("Pilih mode (1/2) [default: 2]: ").strip()
    scrape_detail = (pilihan != '1')
    
    template_file = os.path.join(dir_path, "Template jodi.xlsx")
    max_workers = 50
    
    print("\n1. Melakukan inisialisasi browser...")
    p, browser, page, xsrf_token = await init_browser_jodi()
    
    if not page:
        print("Gagal inisialisasi browser. Keluar...")
        return
        
    print("\n2. Menjalankan Menu 2 (Scraping Datatable Usaha)...")
    usaha_csv = await scrape_usaha_datatable_jodi(page, xsrf_token, template_file, custom_name="jodi_data_usaha", max_workers=max_workers)
    
    if usaha_csv:
        detail_csv, error_csv = None, None
        
        if scrape_detail:
            print("\n3. Menjalankan Menu 3 (Scraping Detail Data)...")
            detail_csv, error_csv = await scrape_detail_data_jodi(page, xsrf_token, usaha_csv, custom_name="jodi_detail_assignment", max_workers=max_workers)
        else:
            print("\n3. Melewati Menu 3 (Scraping Detail Data tidak dijalankan).")
            
        print("\n4. Menggabungkan hasil ke dalam satu file Excel...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        excel_file = os.path.join(dir_path, f"Hasil_Scraping_Jodi_Lengkap_{timestamp}.xlsx")
        
        with pd.ExcelWriter(excel_file) as writer:
            # Sheet 1: Data Usaha
            df_usaha = pd.read_csv(usaha_csv, low_memory=False)
            df_usaha.to_excel(writer, sheet_name='Data_Usaha', index=False)
            
            # Buat Pivot assignmentStatusAlias dengan One-to-One matching (16 digit sub SLS)
            if 'codeIdentity' in df_usaha.columns:
                df_usaha['ID_SUB_SLS_REAL'] = df_usaha['codeIdentity'].astype(str).str.extract(r'^(\d{16})')[0]
                df_usaha['ID_SUB_SLS_REAL'] = df_usaha['ID_SUB_SLS_REAL'].fillna(df_usaha['ID_SLS'].astype(str) + "00")
            elif 'ID_SLS' in df_usaha.columns:
                df_usaha['ID_SUB_SLS_REAL'] = df_usaha['ID_SLS'].astype(str) + "00"
                
            if 'ID_SUB_SLS_REAL' in df_usaha.columns and 'assignmentStatusAlias' in df_usaha.columns:
                pivot_df = pd.crosstab(df_usaha['ID_SUB_SLS_REAL'], df_usaha['assignmentStatusAlias'])
                pivot_df = pivot_df.reset_index()
            else:
                pivot_df = pd.DataFrame()
                
            # Sheet 2: Template Wilayah + Merge Pivot One-to-One
            df_template = pd.read_excel(template_file)
            
            # Hapus kolom Submit, Draf, Total yang sudah ada di template lama
            cols_to_drop = [c for c in df_template.columns if str(c).strip().lower() in ['submit', 'draf', 'total']]
            df_template = df_template.drop(columns=cols_to_drop, errors='ignore')
            
            if 'idsls' in df_template.columns and not pivot_df.empty:
                idsls_str = df_template['idsls'].astype(str).str.replace(r'\.0$', '', regex=True)
                
                if 'kdsubsls' in df_template.columns:
                    kdsubsls_str = df_template['kdsubsls'].astype(str).str.replace(r'\.0$', '', regex=True)
                    kdsubsls_str = pd.to_numeric(kdsubsls_str, errors='coerce').fillna(0).astype(int).astype(str).str.zfill(2)
                    df_template['id_match'] = idsls_str + kdsubsls_str
                else:
                    df_template['id_match'] = idsls_str + "00"
                    
                df_merged = pd.merge(df_template, pivot_df, left_on='id_match', right_on='ID_SUB_SLS_REAL', how='left')
                
                # Mengisi 0 pada hasil pivot agar tidak NaN
                status_cols = pivot_df.columns.drop('ID_SUB_SLS_REAL')
                for col in status_cols:
                    if col in df_merged.columns:
                        df_merged[col] = df_merged[col].fillna(0).astype(int)
                
                # Ekstrak value spesifik
                val_open = df_merged['OPEN'] if 'OPEN' in df_merged.columns else pd.Series(0, index=df_merged.index)
                val_submit = df_merged['SUBMITTED BY Pencacah'] if 'SUBMITTED BY Pencacah' in df_merged.columns else pd.Series(0, index=df_merged.index)
                val_draft = df_merged['DRAFT'] if 'DRAFT' in df_merged.columns else pd.Series(0, index=df_merged.index)
                
                total_all = df_merged[status_cols].sum(axis=1)
                
                # Buat kolom baru sesuai instruksi
                df_merged['Open'] = val_open
                df_merged['Submit'] = val_submit
                df_merged['Draft 1'] = total_all - val_open - val_submit
                df_merged['Total'] = df_merged['Submit'] + df_merged['Draft 1']
                df_merged['Draft 2'] = val_draft
                
                # Susun kolom akhir
                template_base_cols = [c for c in df_template.columns if c != 'id_match']
                other_statuses = [c for c in status_cols if c not in ['OPEN', 'SUBMITTED BY Pencacah', 'DRAFT']]
                
                final_cols = template_base_cols + ['Open', 'Submit', 'Draft 1', 'Total', 'Draft 2'] + other_statuses
                
                df_merged = df_merged[final_cols]
                df_merged.to_excel(writer, sheet_name='Template_Wilayah', index=False)
                
                # --- SHEET KINERJA PPL ---
                if 'PPL' in df_merged.columns:
                    valid_ppl_cols = [c for c in ['Open', 'Submit', 'Draft 1', 'Draft 2'] + other_statuses if c in df_merged.columns]
                    df_ppl = df_merged.groupby('PPL')[valid_ppl_cols].sum().reset_index()
                    
                    # 1. Total semua status (Beban Tugas)
                    # Hindari double counting: Beban sesungguhnya adalah Open + Submit + Draft 1
                    base_cols = [c for c in ['Open', 'Submit', 'Draft 1'] if c in df_ppl.columns]
                    df_ppl['Beban Tugas (Total)'] = df_ppl[base_cols].sum(axis=1)
                    
                    # 2. Persentase Selesai Lapangan
                    # Selesai lapangan = Beban Tugas - Open (alias Submit + Draft 1)
                    df_ppl['Selesai Lapangan'] = df_ppl['Beban Tugas (Total)'] - df_ppl.get('Open', 0)
                    df_ppl['% Selesai Lapangan'] = (df_ppl['Selesai Lapangan'] / df_ppl['Beban Tugas (Total)'].replace(0, 1) * 100).round(2)
                    
                    # 3. Rata-rata per hari (dari 15 Juni)
                    now = datetime.now()
                    start_date = datetime(now.year, 6, 15)
                    hari_berjalan = (now - start_date).days
                    if hari_berjalan <= 0:
                        hari_berjalan = 1
                        
                    df_ppl['Kecepatan (Dokumen/Hari)'] = (df_ppl['Selesai Lapangan'] / hari_berjalan).round(2)
                    
                    # 4. Metric tambahan untuk pantauan
                    df_ppl['Sisa Dokumen (Open)'] = df_ppl.get('Open', 0)
                    df_ppl['Estimasi Butuh Waktu (Hari)'] = (df_ppl['Sisa Dokumen (Open)'] / df_ppl['Kecepatan (Dokumen/Hari)'].replace(0, 0.0001)).round(1)
                    
                    if 'Submit' in df_ppl.columns:
                        df_ppl['% Progress Murni (Submit)'] = (df_ppl['Submit'] / df_ppl['Beban Tugas (Total)'].replace(0, 1) * 100).round(2)
                        
                    # Urutkan dari yang % Selesai Lapangan nya paling rendah agar prioritas pantau
                    df_ppl = df_ppl.sort_values(by='% Selesai Lapangan', ascending=True)
                    df_ppl.to_excel(writer, sheet_name='Kinerja_PPL', index=False)
                    
            else:
                df_template.to_excel(writer, sheet_name='Template_Wilayah', index=False)
                if not pivot_df.empty:
                    pivot_df.to_excel(writer, sheet_name='Rekap_Status', index=False)
            
            # Sheet 3: Detail Data
            if detail_csv and os.path.exists(detail_csv):
                df_detail = pd.read_csv(detail_csv, low_memory=False)
                
                # Tambahkan status assignment dari df_usaha
                if 'Assignment ID' in df_detail.columns and 'Assignment ID' in df_usaha.columns and 'assignmentStatusAlias' in df_usaha.columns:
                    status_map = df_usaha.set_index('Assignment ID')['assignmentStatusAlias'].to_dict()
                    df_detail['Status Assignment'] = df_detail['Assignment ID'].map(status_map)
                    
                    # Pindahkan kolom ke setelah 'id' atau 'Assignment ID'
                    cols = df_detail.columns.tolist()
                    cols.remove('Status Assignment')
                    if 'id' in cols:
                        insert_idx = cols.index('id') + 1
                    else:
                        insert_idx = cols.index('Assignment ID') + 1
                    cols.insert(insert_idx, 'Status Assignment')
                    df_detail = df_detail[cols]
                    
                df_detail.to_excel(writer, sheet_name='Detail_Data', index=False)
                
            # Sheet 4: Error Log (Jika ada)
            if error_csv and os.path.exists(error_csv):
                df_error = pd.read_csv(error_csv, low_memory=False)
                df_error.to_excel(writer, sheet_name='Error_Log', index=False)
                
        print(f"\n==================================================")
        print(f"BERHASIL! Data telah digabung menjadi satu file Excel:")
        print(f"--> {excel_file}")
        print(f"==================================================")
        
        # Membersihkan file CSV sementara
        try:
            if os.path.exists(usaha_csv): os.remove(usaha_csv)
            if detail_csv and os.path.exists(detail_csv): os.remove(detail_csv)
            if error_csv and os.path.exists(error_csv): os.remove(error_csv)
            print("File CSV temporary telah dihapus.")
        except Exception as e:
            print(f"Catatan: Gagal menghapus beberapa file sementara: {e}")
            
    else:
        print("\nProses berhenti karena scraping datatable gagal/kosong.")

    await browser.close()
    await p.stop()

if __name__ == "__main__":
    asyncio.run(main())
