# 📋 Kamus Variabel Kuesioner SE2026 - FASIH BPS

Dokumen ini berisi pemetaan lengkap antara **variabel (dataKey)** di API dengan **pertanyaan asli** di kuesioner, disusun sesuai urutan blok/sidebar.

> **Catatan:** Di file Excel hasil scraping, variabel-variabel ini muncul dengan prefix:
> - `ans_` → Jawaban PPL (data aktual)
> - `pre_` → Data prelist (data awal sebelum didata)

---


## 📁 PENGANTAR

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `cawi_identifier` | number | cawi_identifier | - |
| 2 | `is_cawi` | number | is_cawi | - |
| 3 | `is_from_cawi` | number | is_from_cawi | False |
| 4 | `ec_mulai` | number | New Question | False |
| 5 | `mode` | number | Mode | CAPI |
| 6 | `nama_principal` | number | Nama Keluarga/Bangunan/Usaha untuk principal | RIKADIUS HANDOKO / LISARI |

## 📁 IDENTITAS WILAYAH

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `kode_prov` | number | kode_prov | 61 |
| 2 | `prov_kab` | number | prov_kab | 6106 |
| 3 | `sudah` | number | sudah | True |
| 4 | `tahun_survei` | number | Tahun Survei | 2026 |
| 5 | `has_kodepos` | number | has_kodepos | True |
| 6 | `has_ubah_sls` | number | has_ubah_sls | True |
| 7 | `tahun_lalu` | number | Tahun survei minus 1 | 2025 |
| 8 | `var_desa` | number | New Question | 6106030020 |

## 📁 SE2026 - P

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `is_keluarga` | number | Flag keluarga yang berasal dari prelist Terisi 1 Jika merupakan prelist keluarga | 1 |
| 2 | `nik_anggta_lain_prelist` | number | nik_anggta_lain_prelist | 6104025210940002 |
| 3 | `is_usaha` | number | Flag usaha yang berasal dari prelist Terisi 1 Jika merupakan prelist usaha/ umkm | - |
| 4 | `is_prelist` | number | Flag prelist yang diisikan pada proses pembuatan prelist Terisi 1 jika merupakan prelist | 1 |
| 5 | `set_is_prelist` | number | set_is_prelist | - |
| 6 | `ec_non_keluarga` | number | Enabling Untuk Rincian Bangunan/Usaha Lainnya mencakup : Usaha prelist, Bangunan Lainnya ditemukan dan Usaha/ Bangunan Baru | False |
| 7 | `ket_editable` | number | Keterangan/Catatan Kaki untuk predefined editable | Perbaiki jika terdapat kesalahan penulisan |
| 8 | `ub_prelist` | number | Status UB Prelist | - |
| 9 | `ub` | number | Status UB umkm |  |
| 10 | `jenis_prelist` | number | Jenis Prelist | keluarga |
| 11 | `flag_pbi` | number | PBI | 0 |
| 12 | `no_kk_prelist` | number | Nomor KK prelist untuk pembanding | - |
| 13 | `nik_prelist` | number | NIK prelist untuk pembanding | 6104020705940001 |
| 14 | `nama_lookup_umkm` | number | Nama dari Lookup | - |
| 15 | `set_nama_usaha_bang` | number | set_nama_usaha_bang | - |
| 16 | `alsan_tidak_kk` | number | Alasan Kode KK tidak dapat diberikan: | - |
| 17 | `callnik_button_p` | radio | CEK NIK | - |
| 18 | `hasilPemadananNIK_p` | number | Hasil Pengecekkan NIK | - |
| 19 | `htmlHasilPemadananNIK2_p` | number | Hasil Pengecekan NIK | - |
| 20 | `htmlHasilPemadananNIK_p` | number | ‎ Hasil Pengecekan NIK | - |
| 21 | `result_callnik_p` | number | ‎ | - |
| 22 | `alamat_lookup_umkm` | number | Alamat dari lookup | - |
| 23 | `alamat_klrg` | number | Alamat $ket | DUSUN BATU PERAK |
| 24 | `kode_keberedaan_keluarga` | number | Pilihan kode keberadaan keluarga | [{"label": "0. Tidak Ditemukan", "value": "0"}, {"label": "2... |
| 25 | `kode_keluarga_new` | number | Pilihan Keberadaan Keluarga (new) | [{"label": "0. Tidak Ditemukan (STOP)", "value": "0"}, {"lab... |
| 26 | `kode_bangunan_new` | number | Pilihan Keberadaan Bangunan (new) | [{"label": "2. Baru", "value": "2"}]... |
| 27 | `set_ada_bang_usaha` | number | set_ada_bang_usaha | - |
| 28 | `ec_keluarga` | number | Enabling Untuk Rincian Keluarga mencakup : Keluarga prelist ditemukan dan Keluarga Baru | True |
| 29 | `no_keluarga_terbesar` | number | NOMOR URUT KELUARGA TERBESAR: | 0 |
| 30 | `no_bangunan_terbesar` | number | NOMOR URUT BANGUNAN TERBESAR: | 5 |
| 31 | `pilihan_kode_bang` | number | Options untuk kode_bang disesuaikan | [{"label": "2. Bangunan Campuran", "value": "2"}, {"label": ... |
| 32 | `jumlah_usaha_ditemukan` | number | Jumlah usaha yang ditemukan Jumlah usaha akan terisi dengan meng-update keberadaan usaha | 1 |
| 33 | `daftar_nik_pengusaha` | number | daftar_nik_pengusaha | ["6104020705940001"]... |
| 34 | `usaha_gabung` | number | List yang ditampilkan di se2026_nested | [{"id_pmss": "", "nousaha": 1, "label": "UTP PERKEBUNAN HAND... |
| 35 | `ec_ada_usaha` | number | Enabling Condition Keberadaan Usaha | True |
| 36 | `nama_usaha_prelist` | number | Nama Usaha Prelist | [{"id_art": "6106030020000500-001001001-001#01", "id_ruta": ... |
| 37 | `list_individu_dtsen_prelist` | number | List Individu Prelist | [{"nama_ak": "RIKADIUS HANDOKO", "label": "RIKADIUS HANDOKO"... |
| 38 | `status_pegawai` | number | status_pegawai | - |
| 39 | `idsbr_all` | number | idsbr_all | 5 /  |
| 40 | `nib_all` | number | nib_all |  |
| 41 | `email_all` | number | email_all |  |
| 42 | `skala_usaha_all` | number | skala_usaha_all | UMKM / KELUARGA |
| 43 | `idunik_MSSD` | number | idunik_MSSD | 6DAB715A-1728-488E-8294-F4F27356592E |
| 44 | `jumlah_usaha` | number | jumlah_usaha | 1 |
| 45 | `ya_pertanian` | number | Jumlah Usaha Pertanian | 1 |
| 46 | `ya_nonpertanian` | number | Jumlah Usaha Non-Pertanian | 0 |
| 47 | `ya_gabung` | number | jum usaha gabung | 1 |
| 48 | `skala_usaha_prelist` | number | skala_usaha_prelist | UMKM |

## 📁 SE2026 - L BLOK I

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `set_nik_kk` | number | Set NIK KK | - |
| 2 | `label_usaha` | number | Label Usaha |      <ul style="list-style-type: disc; padding-left: 20px; m... |
| 3 | `prelist_dtsen` | number | Nama anggota keluarga | - |
| 4 | `gabung_dtsen` | number | gabung_dtsen | [{"no_urut": 1, "label": "RIKADIUS HANDOKO", "value": 1, "is... |
| 5 | `art_pengusaha` | number | art_pengusaha | [{"nik": "6104020705940001", "jk": [{"label": "1. Laki-laki"... |
| 6 | `art_keberadaan15` | number | art yg keberadaan kode 1 dan 5 | [{"label": "RIKADIUS HANDOKO", "value": "1"}, {"label": "LIS... |
| 7 | `cek1` | number | cek jum art 15 | 4 |
| 8 | `jk_krt` | number | jk_krt | [{"gender": 1, "label": "RIKADIUS HANDOKO", "value": "1"}]..... |
| 9 | `umur_krt` | number | umur krt | 32 |
| 10 | `jum_anakmantucucu` | number | Jumlah anak mantu cucu | 2 |
| 11 | `jum_pasangan` | number | Jumlah pasangan suami / istri | 1 |
| 12 | `jum_art_semua` | number | jum_art_semua | 4 |
| 13 | `jum_art_1345` | number | jum_art_1345 | 4 |
| 14 | `jum_art_1345_umurkur10` | number | jum_art_1345_umurkur10 | 0 |
| 15 | `jum_kk_lebihdr10th` | number | jum_kk_lebihdr10th | 1 |
| 16 | `jum_kk` | number | jum_kk | 1 |
| 17 | `nested_dtsen` | text | Keterangan Anggota Keluarga | - |
| 18 | `isprelistart` | number | Apakah prelist art | - |
| 19 | `no_urut_kk` | number | 5. Nomor urut anggota keluarga | - |
| 20 | `nama_dtsen` | number | 6. Nama anggota keluarga | - |
| 21 | `set_nik_dtsen_prelist` | number | set_nik_dtsen_prelist | - |
| 22 | `nik_dtsen_prelist` | number | nik_dtsen_prelist | - |
| 23 | `callnik_button` | radio | CEK NIK | - |
| 24 | `hasilPemadananNIK` | number | Hasil Pengecekkan NIK | - |
| 25 | `htmlHasilPemadananNIK2` | number | . | - |
| 26 | `htmlHasilPemadananNIK` | number | Hasil Pengecekan NIK | - |
| 27 | `result_callnik` | number | . | - |
| 28 | `ec_anggota_keluarga` | number | Enabling anggota keluarga | - |
| 29 | `set_jk_prelist` | number | set_jk_prelist | - |
| 30 | `jk_prelist` | number | jk_prelist | - |
| 31 | `set_umur_ak` | number | set_umur_ak | - |

## 📁 SE2026 - L BLOK II

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `se2026_nested` | text | Keterangan Usaha/Perusahaan | - |
| 2 | `pilih_umkm_options` | number | Opsi Pilih UMKM dalam satu SLS yang sama | - |
| 3 | `prov_l` | number | 1. Provinsi | - |
| 4 | `kab_l` | number | 2. Kabupaten/Kota | - |
| 5 | `kec_l` | number | 3. Kecamatan | - |
| 6 | `desa_l` | number | 4. Kelurahan/Desa/Nagari | - |
| 7 | `kodesls_l` | number | Kode SLS/Sub-SLS | - |
| 8 | `sls_l` | number | Nama SLS/Sub-SLS | - |
| 9 | `no_bang_l` | number | 6. Nomor Bangunan | - |
| 10 | `no_usaha` | number | 7. Nomor Urut Usaha/Perusahaan | - |
| 11 | `ec_mulai_L` | number | New Question | - |
| 12 | `nama_usaha` | number | 8. a. Nama usaha/perusahaan | - |
| 13 | `set_keberadaan_usaha` | number | set_keberadaan_usaha | - |
| 14 | `skala_usaha` | number | skala_usaha | - |
| 15 | `is_prelist2` | number | Is_Prelist2 | - |
| 16 | `id_pmss` | number | id_pmss | - |
| 17 | `idsbr` | number | ID SBR | - |
| 18 | `kode_keberadaan_usaha` | number | Pilihan untuk keberadaan Usaha | - |
| 19 | `alamat_usaha_var` | number | 8. c. Alamat usaha/perusahaan | - |
| 20 | `alamat_usaha` | number | alamat_usaha | - |
| 21 | `kp_nested` | text | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Daftar Kantor Cabang | - |
| 22 | `kp_total_pengeluaran` | address | Pengeluaran Tahun 2025 (Rupiah) | - |
| 23 | `kp_total_pendapatan` | address | Pendapatan Tahun 2025 (Rupiah) | - |
| 24 | `kode_pos` | number | Kode Pos | - |
| 25 | `ec_usaha_respons` | number | Enabling Condition Usaha Respons di Roster | - |
| 26 | `cek_nib` | radio | CEK NIB | - |
| 27 | `hasilCekNIB` | number | ​ | - |
| 28 | `htmlHasilCekNIB` | number | Hasil Pengecekan NIB | - |
| 29 | `result_callnib` | number | result_callnib | - |
| 30 | `pengusaha_var_prelist` | number | pengusaha_var_prelist | - |
| 31 | `set_pengusaha_var` | number | set_pengusaha_var | - |
| 32 | `set_default_pengusaha_var` | number | set_default_pengusaha_var | - |
| 33 | `jk_var` | number | 12. b. Jenis Kelamin | - |
| 34 | `umur_pj_var` | number | 12. c. Umur | - |
| 35 | `nik_pengusaha_var` | number | 12. d. Nomor Induk Kependudukan (NIK ) | - |
| 36 | `callnik_button_l` | radio | CEK NIK | - |
| 37 | `hasilPemadananNIK_l` | number | Hasil Pengecekkan NIK | - |
| 38 | `htmlHasilPemadananNIK2_l` | number | ​ | - |
| 39 | `htmlHasilPemadananNIK_l` | number | Hasil Pengecekan NIK | - |
| 40 | `result_callnik_l` | number | ​ | - |
| 41 | `jenis_kegiatan` | number | jenis_kegiatan | - |
| 42 | `genai_button` | radio | DAPATKAN REKOMENDASI KBLI | - |
| 43 | `var_kbli` | number | Pilihan untuk KBLI | - |
| 44 | `result_gen_ai` | number | Result Gen AI | - |
| 45 | `kbli_prelist` | number | kbli_prelist | - |
| 46 | `kbli_genai_cawi` | number | kbli_genai_cawi | - |
| 47 | `kbli_cawi` | number | kbli_cawi | - |
| 48 | `set_kbli_cawi` | number | set_kbli_cawi | - |
| 49 | `kbli_akhir` | number | KBLI Akhir | - |
| 50 | `kategori_2025` | number | kategori_2025 | - |
| 51 | `kategori` | number | 13. h. Kategori Lapangan Usaha: | - |
| 52 | `msg_error_kategori` | number | &nbsp | - |
| 53 | `html_msg_error` | number | Error: $ket | - |
| 54 | `var_hiden_pml` | number | New Question | - |
| 55 | `ec_usaha_lanjutan` | number | Enabling Condition untuk Usaha Ditemukan selain penunjang dan pusat | - |
| 56 | `ec_halal` | number | ec_halal | - |
| 57 | `ec_bpom` | number | ec_bpom | - |
| 58 | `total_tk_jk_var` | number | total_tk_jk_var | - |
| 59 | `total_tk_bayar_var` | number | total_tk_bayar_var | - |
| 60 | `ec_usaha_bulan` | number | enabling condition pertanyaan 25 s.d 28 | - |
| 61 | `ec_usaha_tahun` | number | enabling condition pertanyaan 21s.d 24 | - |
| 62 | `gaji` | address | 26. a. Total upah dan gaji, serta jaminan sosial pegawai | - |
| 63 | `biaya_produksi` | address | 26. b. Biaya produksi | - |
| 64 | `biaya_pembelian` | address | 26. c. Biaya pembelian barang yang terjual | - |
| 65 | `operasional` | address | 26. d. Biaya operasional (air, listrik, gas, internet, pulsa, pemeliharaan, biaya angkutan, dll.) | - |
| 66 | `non_operasional` | address | 26. e. Biaya non-operasional | - |
| 67 | `total_pengeluaran_var` | number | total_pengeluaran_var | - |
| 68 | `total_pengeluaran` | address | 26. f. Total pengeluaran (a+b+c+d+e) | - |
| 69 | `var_narasi` | number | Narasi Pendapatan | - |
| 70 | `nilai_pendapatan` | address | 27. a. Nilai $narasi barang dan jasa | - |
| 71 | `pendapatan_lain` | address | 27. b. Pendapatan lainnya yang dihasilkan perusahaan | - |
| 72 | `total_pendapatan` | address | 27. c. Total nilai $narasi (a+b) | - |
| 73 | `total_pendapatan_var` | number | total_pendapatan_var | - |
| 74 | `aset_usaha_thn` | address | 28. a. Nilai aset tanah dan bangunan pada 31 Desember 2025 | - |
| 75 | `aset_lain_thn` | address | 28. b. Nilai aset selain tanah dan bangunan pada 31 Desember 2025 | - |
| 76 | `total_aset_thn` | address | 28. c. Nilai total aset pada 31 Desember 2025 | - |
| 77 | `total_aset_thn_var` | number | total_aset_thn_var | - |
| 78 | `info_total_var` | number | info_total_var | - |
| 79 | `gaji_bln` | address | 30. a. Total upah dan gaji, serta jaminan sosial pegawai | - |
| 80 | `biaya_produksi_bln` | address | 30. b. Biaya produksi | - |
| 81 | `biaya_pembelian_bln` | address | 30. c. Biaya pembelian barang yang terjual | - |
| 82 | `operasional_bln` | address | 30. d. Biaya operasional (air, listrik, gas, internet, pulsa, pemeliharaan, biaya angkutan) | - |
| 83 | `non_operasional_bln` | address | 30. e. Biaya non-operasional | - |
| 84 | `total_pengeluaran_bln` | address | 30. f. Total pengeluaran (a+b+c+d+e) | - |
| 85 | `total_pengeluaran_bln_var` | number | total_pengeluaran_bln | - |
| 86 | `nilai_pendapatan_bln` | address | 31. a. Nilai $narasi barang dan jasa | - |
| 87 | `pendapatan_lain_bln` | address | 31. b. Pendapatan lainnya yang dihasilkan | - |
| 88 | `total_pendapatan_bln` | address | 31. c. Total nilai $narasi (a+b) | - |
| 89 | `total_pendapatan_bln_var` | number | total_pendapatan_bln_var | - |
| 90 | `aset_tanah_bln` | address | 32. a. Nilai aset tanah dan bangunan pada akhir bulan yang lalu | - |
| 91 | `aset_lain_bln` | address | 32. b. Nilai aset selain tanah dan bangunan pada akhir bulan yang lalu | - |
| 92 | `total_aset_bln` | number | 32. c. Nilai total aset pada akhir bulan yang lalu* | - |
| 93 | `cek5` | number | New Question | - |
| 94 | `info_total_didirikan_var` | number | info_total_didirikan_var | - |

## 📁 SE2026 - L BLOK III

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `dtsen_nama_kk` | number | 1. a. Nama Kepala Keluarga | RIKADIUS HANDOKO |
| 2 | `nik_kk` | number | 1. b. NIK Kepala Keluarga | 6104020705940001 |
| 3 | `dtsen_no_kk` | number | 1. c. Nomor kartu keluarga | 6104020608140004 |
| 4 | `jml_kk` | number | 2. a. Jumlah anggota keluarga sesuai KK | 4 |
| 5 | `jml_kk_update` | number | 2. b. Jumlah anggota keluarga sesuai hasil pendataan | 4 |
| 6 | `prelist_dtsen_var` | number | Nama anggota keluarga prelist | - |
| 7 | `tambah_dtsen_var` | number | Nama anggota keluarga tambahan | - |
| 8 | `gabung_dtsen_var` | number | gabung_dtsen | [{"label": "RIKADIUS HANDOKO", "value": 1, "is_prelist": "1"... |
| 9 | `gabung_dtsen_2` | number | gabung_dtsen_2 | [{"no_urut": 1, "label": "RIKADIUS HANDOKO", "value": 1, "is... |
| 10 | `total_pendapatan_keluarga_sebulan` | number | total_pendapatan_keluarga_sebulan (sudah dari semua anggota keluarga) | 2510000 |
| 11 | `nested_dtsen_var` | text | Keterangan Anggota Keluarga | - |
| 12 | `no_urut_kk_var` | number | Nomor urut anggota keluarga | - |
| 13 | `nama_dtsen_var` | number | Nama anggota keluarga | - |
| 14 | `ec_art_dtsen` | number | ec_art_dtsen | - |
| 15 | `ec_art_pendapatan` | number | ec_art_pendapatan | - |
| 16 | `set_sekolah_prelist` | number | set_sekolah_prelist | - |
| 17 | `sekolah_prelist` | number | Sekolah Prelist | - |
| 18 | `set_ijazah_prelist` | number | set_ijazah_prelist | - |
| 19 | `ijazah_prelist` | number | Ijazah Prelist | - |
| 20 | `pend_gaji` | address | a. Upah/Gaji | - |
| 21 | `pend_tunjangan` | address | b. Tunjangan | - |
| 22 | `pend_uangmkn` | address | c. Uang Makan | - |
| 23 | `pend_honor` | address | d. Honor | - |
| 24 | `pend_lembur` | address | e. Lembur | - |
| 25 | `pend_lainnya` | address | f. Lainnya | - |
| 26 | `nilai_pend_pekerjaan` | number | 18. a1. Total Pendapatan (a+b+c+d+e+f) | - |
| 27 | `pend_usaha` | address | 18. b1. Total Pendapatan | - |
| 28 | `nilai_pend_lain` | address | 18. c1. Total Pendapatan | - |

## 📁 SE2026 - L BLOK IV

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `total_pengeluaran_keluarga_sebulan` | number | total_pengeluaran_keluarga_sebulan | 2671428.571428572 |
| 2 | `sewa_sendiri` | address | &nbsp;&nbsp;a. Jika milik sendiri/bebas sewa, perkiraan harga sewa sebulan: | 500000 |
| 3 | `sewa_kontrak` | address | &nbsp;&nbsp;b. Jika kontrak/sewa , nilai kontrak sebulan: | - |
| 4 | `sewa_dinas` | address | &nbsp;&nbsp;c. Jika dinas atau lainnya, perkiraan nilai sewa sebulan: | - |
| 5 | `nested_meteran` | text | 14. b. Berapa daya yang terpasang di rumah ini? | - |
| 6 | `urutan_meteran_lain` | number | Meteran ke- | - |
| 7 | `cek_idpel` | radio | CEK ID PELANGGAN | - |
| 8 | `hasilCekIdPel` | number | ​ | - |
| 9 | `htmlHasilCekIdPel` | number | ​ | - |
| 10 | `result_cekidpel` | number | ​ | - |
| 11 | `cek_no_meteran` | radio | CEK NOMOR METERAN | - |
| 12 | `htmlHasilCekMeteran` | number | ​ | - |
| 13 | `hasilCekMeteran` | number | ​ | - |
| 14 | `result_cekmeteran` | number | result_cekmeteran | - |
| 15 | `listrik_sebulan` | address | 15. a. Berapa nilai pengeluaran listrik sebulan? (Dapat menggunakan pertanyaan seperti: biasanya, rata-rata, atau sebulan terakhir) | 250000 |
| 16 | `pulsa_sebulan` | address | 15. b. Berapa pengeluaran pulsa dan internet seluruh anggota keluarga sebulan? (Dapat menggunakan pertanyaan seperti: biasanya, rata-rata, atau sebulan terakhir) | 150000 |
| 17 | `pengeluaran_makanan_mingguan` | address | 16. a. Berapa rata-rata pengeluaran makanan keluarga seminggu? | 250000 |
| 18 | `jml_meteran_var` | number | jml_meteran_var | 1 |
| 19 | `pengeluaran_non_makan_bulanan` | address | 16. b. Berapa rata-rata pengeluaran bukan makanan rutin keluarga bulanan? | 800000 |
| 20 | `pengeluaran_non_makan_tahunan` | address | 16. c. Berapa rata-rata pengeluaran bukan makanan rutin keluarga tahunan? | 9600000 |
| 21 | `jumlah_tabung3kg` | number | jumlah_tabung3kg_prelist | - |
| 22 | `jumlah_tabung5kg` | number | jumlah_tabung5kg_prelist | - |
| 23 | `jumlah_kulkas` | number | jumlah_kulkas_prelist | 1 |
| 24 | `jumlah_ac` | number | jumlah_ac_prelist | 2 |
| 25 | `jumlah_emas` | number | jumlah_emas_prelist | 0 |
| 26 | `jumlah_laptop` | number | jumlah_laptop_prelist | 1 |
| 27 | `jumlah_motor` | number | jumlah_motor_prelist | 1 |
| 28 | `nilai_motor` | address | g. ii. Total nilai aset sepeda motor (rupiah) | 8000000 |
| 29 | `jumlah_mobil` | number | jumlah_mobil_prelist | 1 |
| 30 | `nilai_mobil` | address | h. ii. Total nilai aset mobil (rupiah) | - |
| 31 | `jumlah_lahan` | number | jumlah_lahan_prelist | - |
| 32 | `nilai_lahan` | address | a. ii. Total nilai harga jual tanah/lahan di tempat lain (selain yang ditempati): | 15000000 |
| 33 | `jumlah_rumah` | number | jumlah_rumah_prelist | - |
| 34 | `nilai_rumah` | address | b. ii. Total nilai harga jual rumah/bangunan di tempat lain (selain yang ditempati): | - |
| 35 | `set_default_aset` | number | set_default_aset | - |

## 📁 KETERANGAN PEMBERI JAWABAN

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `nama_info` | number | nama_info_cawi | - |
| 2 | `ak_info` | number | ak_info | [{"no_urut": 1, "label": "RIKADIUS HANDOKO", "value": 1, "is... |

## 📁 CATATAN

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `idsbr_keluarga` | number | ID SBR keluarga |  |
| 2 | `idsbr_match` | number | ID SBR Match | None |
| 3 | `id_l1_umkm` | number | New Question | - |
| 4 | `id_l2_umkm` | number | New Question | - |
| 5 | `id_keluarga` | number | New Question | 6104020608140004 |
| 6 | `id_regsosek` | number | New Question | - |
| 7 | `daftar_anomali` | number | daftar_anomali | - |

## 📁 ANOMALI

| No | Variabel (`dataKey`) | Tipe | Pertanyaan | Contoh Isian |
|----|---------------------|------|------------|-------------|
| 1 | `cek_anomali` | number | CEK ANOMALI | - |
| 2 | `custom_script_table` | number | custom_script_table | - |
| 3 | `tanggal_anomali` | number | tanggal_anomali | - |
| 4 | `tanggal_selesai_anomali` | number | tanggal_selesai_anomali | - |
