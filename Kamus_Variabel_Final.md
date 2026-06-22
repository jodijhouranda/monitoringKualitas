# 📋 Kamus Variabel Kuesioner SE2026 – FASIH BPS

Pemetaan **variabel API** ↔ **pertanyaan kuesioner asli**, disusun per blok.

> Di file Excel hasil scraping, variabel muncul dengan prefix:
> - **`ans_`** → Jawaban PPL (data aktual hasil pendataan)
> - **`pre_`** → Data prelist (data awal sebelum didata)

---


---

## 📁 PENGANTAR

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `mulai` | Waktu (Datetime) | Waktu Mulai | 2026-06-20T13:04:39 |
| 2 | `cawi_identifier` | Angka/Tersembunyi | cawi_identifier |  |
| 3 | `is_cawi` | Angka/Tersembunyi | is_cawi |  |
| 4 | `is_from_cawi` | Angka/Tersembunyi | is_from_cawi | False |
| 5 | `kunjungan_1` | Waktu (Datetime) | Waktu Kunjungan I | 2026-06-20T13:04:42 |
| 6 | `catatan_1` | Isian Teks Panjang | Catatan Kunjungan I |  |
| 7 | `kunjungan_2` | Waktu (Datetime) | Waktu Kunjungan II |  |
| 8 | `catatan_2` | Isian Teks Panjang | Catatan Kunjungan II |  |
| 9 | `kunjungan_3` | Waktu (Datetime) | Waktu Kunjungan III |  |
| 10 | `alasan_nr` | Pilihan Dropdown | Alasan Nonrespon |  |
| 11 | `catatan_3` | Isian Teks Panjang | Catatan Kunjungan III |  |
| 12 | `kunjungan_pml` | Waktu (Datetime) | Waktu Kunjungan PML |  |
| 13 | `geotag_pml` | Geotag/GPS | Geotaging oleh PML |  |
| 14 | `catatan_pml` | Isian Teks Panjang | Catatan Kunjungan PML |  |
| 15 | `ec_mulai` | Angka/Tersembunyi | New Question | False |
| 16 | `mode` | Angka/Tersembunyi | Mode | CAPI |
| 17 | `nama_principal` | Angka/Tersembunyi | Nama Keluarga/Bangunan/Usaha untuk principal | RIKADIUS HANDOKO / LISARI |

---

## 📁 IDENTITAS WILAYAH

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `prov` | Pilihan Dropdown | 1. Provinsi | [61] KALIMANTAN BARAT |
| 2 | `kab` | Pilihan Dropdown | 2. Kabupaten/Kota | [06] KETAPANG |
| 3 | `kec` | Pilihan Dropdown | 3. Kecamatan | [030] MARAU |
| 4 | `desa` | Pilihan Dropdown | 4. Desa/Kelurahan | [020] RIAM BATU GADING |
| 5 | `ubah_wilayah` | Pilihan Dropdown | Apakah Terdapat Perubahan Wilayah? | [{"label": "Tidak", "value": "2"}] |
| 6 | `kab_baru` | Pilihan Dropdown | 2. Kabupaten/Kota |  |
| 7 | `kec_baru` | Pilihan Dropdown | 3. Kecamatan |  |
| 8 | `desa_baru` | Pilihan Dropdown | 4. Desa/Kelurahan |  |
| 9 | `kode_prov` | Angka/Tersembunyi | kode_prov | 61 |
| 10 | `prov_kab` | Angka/Tersembunyi | prov_kab | 6106 |
| 11 | `klas_desa` | Pilihan Dropdown | 5. Klasifikasi Desa/Kelurahan | Perdesaan |
| 12 | `kode_sls` | Pilihan Dropdown | 6. Kode SLS/Non-SLS/Sub-SLS | 000500 |
| 13 | `nama_sls` | Pilihan Dropdown | 7. Nama SLS/Non-SLS | RT 005 RW 002 DUSUN BATU PERAK |
| 14 | `ubah_sls` | Pilihan Dropdown | 8. Apakah mengalami perubahan SLS (pemekaran/penggabungan/perubahan nama?) |  |
| 15 | `sudah` | Angka/Tersembunyi | sudah | True |
| 16 | `nama_sls_lap` | Pilihan Dropdown | 9. Nama SLS/Non-SLS Lapangan |  |
| 17 | `tahun_survei` | Angka/Tersembunyi | Tahun Survei | 2026 |
| 18 | `kodepos` | Pilihan Dropdown | 10. Kodepos |  |
| 19 | `has_kodepos` | Angka/Tersembunyi | has_kodepos | True |
| 20 | `has_ubah_sls` | Angka/Tersembunyi | has_ubah_sls | True |
| 21 | `tahun_lalu` | Angka/Tersembunyi | Tahun survei minus 1 | 2025 |
| 22 | `var_desa` | Angka/Tersembunyi | New Question | 6106030020 |

---

## 📁 SE2026 - P

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `is_keluarga` | Angka/Tersembunyi | Flag keluarga yang berasal dari prelist Terisi 1 Jika merupakan prelist keluarga | 1 |
| 2 | `nik_anggta_lain_prelist` | Angka/Tersembunyi | nik_anggta_lain_prelist | 6104025210940002 |
| 3 | `is_usaha` | Angka/Tersembunyi | Flag usaha yang berasal dari prelist Terisi 1 Jika merupakan prelist usaha/ umkm |  |
| 4 | `is_prelist` | Angka/Tersembunyi | Flag prelist yang diisikan pada proses pembuatan prelist Terisi 1 jika merupakan prelist | 1 |
| 5 | `ec_non_keluarga` | Angka/Tersembunyi | Enabling Untuk Rincian Bangunan/Usaha Lainnya mencakup : Usaha prelist, Bangunan Lainnya ditemukan dan Usaha/ Bangunan Baru | False |
| 6 | `ket_editable` | Angka/Tersembunyi | Keterangan/Catatan Kaki untuk predefined editable | Perbaiki jika terdapat kesalahan penulisan |
| 7 | `ub_prelist` | Angka/Tersembunyi | Status UB Prelist |  |
| 8 | `ub` | Angka/Tersembunyi | Status UB umkm |  |
| 9 | `jenis_prelist` | Angka/Tersembunyi | Jenis Prelist | keluarga |
| 10 | `flag_pbi` | Angka/Tersembunyi | PBI | 0 |
| 11 | `is_new` | Pilihan Dropdown | Tambah : Pilih jenis assignment yang akan ditambahkan |  |
| 12 | `pilih_umkm` | Pilihan Dropdown | Daftar Usaha Non Prelist Pilih "Tidak Ditemukan" jika nama usaha tidak ada di daftar usaha |  |
| 13 | `no_kk_prelist` | Angka/Tersembunyi | Nomor KK prelist untuk pembanding |  |
| 14 | `nik_prelist` | Angka/Tersembunyi | NIK prelist untuk pembanding | 6104020705940001 |
| 15 | `nama_lookup_umkm` | Angka/Tersembunyi | Nama dari Lookup |  |
| 16 | `nama_usaha_bang` | Pilihan Dropdown | Nama Bangunan/ Usaha/ Perusahaan $ket |  |
| 17 | `no_kk` | Pilihan Dropdown | Nomor KK $ket | 6104020608140004 |
| 18 | `alsan_tidak_kk` | Angka/Tersembunyi | Alasan Kode KK tidak dapat diberikan: |  |
| 19 | `nik` | Pilihan Dropdown | NIK $ket | 6104020705940001 |
| 20 | `nama_kk` | Pilihan Dropdown | Nama Kepala Keluarga (KK) $ket | RIKADIUS HANDOKO |
| 21 | `callnik_button_p` | Tombol (Radio) | CEK NIK |  |
| 22 | `hasilPemadananNIK_p` | Angka/Tersembunyi | Hasil Pengecekkan NIK |  |
| 23 | `nama_ak_lain` | Pilihan Dropdown | Nama Anggota Keluarga Lainnya $ket | LISARI |
| 24 | `alamat_lookup_umkm` | Angka/Tersembunyi | Alamat dari lookup |  |
| 25 | `alamat_klrg` | Angka/Tersembunyi | Alamat $ket | DUSUN BATU PERAK |
| 26 | `jumlah_usaha_prelist` | Pilihan Dropdown | Jumlah Usaha yang Dimiliki Seluruh Anggota Keluarga (Sumber: UMKM dan ST2023) | 1 |
| 27 | `kode_keberedaan_keluarga` | Angka/Tersembunyi | Pilihan kode keberadaan keluarga | [{"label": "0. Tidak Ditemukan", "value": "0"}, {"label":... |
| 28 | `kode_keluarga_new` | Angka/Tersembunyi | Pilihan Keberadaan Keluarga (new) | [{"label": "0. Tidak Ditemukan (STOP)", "value": "0"}, {"... |
| 29 | `kode_bangunan_new` | Angka/Tersembunyi | Pilihan Keberadaan Bangunan (new) | [{"label": "2. Baru", "value": "2"}] |
| 30 | `ada_keluarga` | Pilihan Dropdown | Keberadaan Keluarga | [{"label": "1. Ditemukan", "value": "1", "open": false}] |
| 31 | `ada_bang_usaha` | Pilihan Dropdown | Keberadaan Bangunan Lainnya/ Usaha |  |
| 32 | `alamat_prelist` | Isian Teks Panjang | Alamat (Prelist) | DUSUN BATU PERAK |
| 33 | `domisili` | Pilihan Dropdown | Apakah alamat tersebut sesuai dengan alamat pada Kartu Keluarga? | [{"description": "", "label": "1. Ya Sesuai KK", "value":... |
| 34 | `jalan_domisili` | Isian Teks Panjang | Nama Jalan/Gang/Komplek/Gedung/dll (Tuliskan dengan rinci) | DUSUN BATU PERAK |
| 35 | `nomor_domisili` | Pilihan Dropdown | Blok/Nomor Rumah (Jika tidak ada nomor rumah, tulis strip (-)) | - |
| 36 | `ec_keluarga` | Angka/Tersembunyi | Enabling Untuk Rincian Keluarga mencakup : Keluarga prelist ditemukan dan Keluarga Baru | True |
| 37 | `no_keluarga_terbesar` | Angka/Tersembunyi | NOMOR URUT KELUARGA TERBESAR: | 0 |
| 38 | `no_keluarga` | Isian Angka | Nomor Urut Keluarga | 4 |
| 39 | `no_bangunan_terbesar` | Angka/Tersembunyi | NOMOR URUT BANGUNAN TERBESAR: | 5 |
| 40 | `no_bang` | Isian Angka | Nomor Urut Bangunan | 5 |
| 41 | `kode_bang` | Pilihan Dropdown | Kode Penggunaan Bangunan | [{"label": "3. Bangunan Tempat Tinggal", "value": "3", "o... |
| 42 | `pilihan_kode_bang` | Angka/Tersembunyi | Options untuk kode_bang disesuaikan | [{"label": "2. Bangunan Campuran", "value": "2"}, {"label... |
| 43 | `geotag` | Geotag/GPS | Geotagging | [{"label": "https://maps.google.com/maps?q=-2.11157,110.7... |
| 44 | `foto_depan_p` | Upload Foto | Foto tampak depan (harus mencakup atap dan dinding) |  |
| 45 | `jumlah_ak_kk` | Isian Angka | Jumlah Anggota Keluarga Berdasarkan Kartu Keluarga | 4 |
| 46 | `jumlah_ak` | Pilihan Dropdown | Jumlah Anggota Keluarga Yang menetap di dalam bangunan tempat tinggal minimal 1 tahun, atau kurang dari 1 tahun dan berniat menetap | 4 |
| 47 | `usaha_kos` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK memiliki usaha penyewaan lahan atau kontrakan atau kos kosan? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 48 | `usaha_keliling` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK memiliki usaha keliling (pedagang sayur keliling, ojek keliling, tukang becak keliling, supir | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 49 | `usaha_online` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK memiliki usaha online contoh: menjual barang melalui tokopedia/ shopee/website/ instagram tanpa memiliki toko? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 50 | `usaha_bongkar` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK memiliki usaha di luar tempat tinggal, yang lokasi usahanya tetap tetapi peralatan/ perlengkapan usahanya dipindah/ dibawa pulang/ dibongkar pasang (misal: usaha kaki lima/ tenda seafood yang jika sudah tutup semua peralatan akan dibawa pulang, usaha dagang martabak gerobakan yang mangkal di pinggir jalan namun jika sudah selesai gerobak akan dibawa pulang, dan usaha lain yang sejenis) | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 51 | `usaha_konstruksi` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK memiliki usaha sebagai pemborong konstruksi/perusahaan konstruksi yang berlokasi di tempat tinggal ini atau penggalian perorangan? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 52 | `usaha_lain` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK memiliki usaha lain? Seperti mengajar privat dari rumah ke rumah, Freelance, YouTuber, Konten Kreator, Afiliator, dan semua usaha lainnya yang dilakukan dalam bangunan ini? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 53 | `tanaman_pangan` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Tanaman Pangan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? termasuk yang seluruhnya dikonsumsi sendiri (padi, jagung, kedelai, kacang tanah, kacang hijau, ubi kayu, ubi jalar, talas, ganyong, dan palawija lainnya) | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 54 | `hortikultura` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Hortikultura dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 55 | `perkebunan` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Perkebunan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? | [{"description": "", "label": "1. Ya", "value": "1", "ope... |
| 56 | `peternakan` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Peternakan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 57 | `kehutanan` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Kehutanan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 58 | `perikanan` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Perikanan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 59 | `jasa_pertanian` | Pilihan Dropdown | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Jasa Pertanian dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? | [{"description": "", "label": "2. Tidak", "value": "2", "... |
| 60 | `jumlah_usaha_ditemukan` | Angka/Tersembunyi | Jumlah usaha yang ditemukan Jumlah usaha akan terisi dengan meng-update keberadaan usaha | 1 |
| 61 | `daftar_nik_pengusaha` | Angka/Tersembunyi | daftar_nik_pengusaha | ["6104020705940001"] |
| 62 | `usaha_gabung` | Angka/Tersembunyi | List yang ditampilkan di se2026_nested | [{"id_pmss": "", "nousaha": 1, "label": "UTP PERKEBUNAN H... |
| 63 | `ec_ada_usaha` | Angka/Tersembunyi | Enabling Condition Keberadaan Usaha | True |
| 64 | `nama_usaha_prelist` | Angka/Tersembunyi | Nama Usaha Prelist | [{"id_art": "6106030020000500-001001001-001#01", "id_ruta... |
| 65 | `list_individu_dtsen_prelist` | Angka/Tersembunyi | List Individu Prelist | [{"nama_ak": "RIKADIUS HANDOKO", "label": "RIKADIUS HANDO... |
| 66 | `status_pegawai` | Angka/Tersembunyi | status_pegawai |  |
| 67 | `idsbr_all` | Angka/Tersembunyi | idsbr_all | 5 /  |
| 68 | `nib_all` | Angka/Tersembunyi | nib_all |  |
| 69 | `email_all` | Angka/Tersembunyi | email_all |  |
| 70 | `skala_usaha_all` | Angka/Tersembunyi | skala_usaha_all | UMKM / KELUARGA |
| 71 | `idunik_MSSD` | Angka/Tersembunyi | idunik_MSSD | 6DAB715A-1728-488E-8294-F4F27356592E |
| 72 | `jumlah_usaha` | Angka/Tersembunyi | jumlah_usaha | 1 |
| 73 | `ya_pertanian` | Angka/Tersembunyi | Jumlah Usaha Pertanian | 1 |
| 74 | `ya_nonpertanian` | Angka/Tersembunyi | Jumlah Usaha Non-Pertanian | 0 |
| 75 | `ya_gabung` | Angka/Tersembunyi | jum usaha gabung | 1 |
| 76 | `skala_usaha_prelist` | Angka/Tersembunyi | skala_usaha_prelist | UMKM |

---

## 📁 SE2026 - L BLOK I

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `label_usaha` | Angka/Tersembunyi | Label Usaha |      <ul style="list-style-type: disc; padding-left: 20px... |
| 2 | `prelist_dtsen` | Angka/Tersembunyi | Nama anggota keluarga |  |
| 3 | `tambah_dtsen` | Tabel Isian | Nama anggota keluarga | [{"label": "lastId#1", "value": "0"}] |
| 4 | `gabung_dtsen` | Angka/Tersembunyi | gabung_dtsen | [{"no_urut": 1, "label": "RIKADIUS HANDOKO", "value": 1, ... |
| 5 | `art_pengusaha` | Angka/Tersembunyi | art_pengusaha | [{"nik": "6104020705940001", "jk": [{"label": "1. Laki-la... |
| 6 | `art_keberadaan15` | Angka/Tersembunyi | art yg keberadaan kode 1 dan 5 | [{"label": "RIKADIUS HANDOKO", "value": "1"}, {"label": "... |
| 7 | `cek1` | Angka/Tersembunyi | cek jum art 15 | 4 |
| 8 | `jk_krt` | Angka/Tersembunyi | jk_krt | [{"gender": 1, "label": "RIKADIUS HANDOKO", "value": "1"}] |
| 9 | `umur_krt` | Angka/Tersembunyi | umur krt | 32 |
| 10 | `jum_anakmantucucu` | Angka/Tersembunyi | Jumlah anak mantu cucu | 2 |
| 11 | `jum_pasangan` | Angka/Tersembunyi | Jumlah pasangan suami / istri | 1 |
| 12 | `jum_art_semua` | Angka/Tersembunyi | jum_art_semua | 4 |
| 13 | `jum_art_1345` | Angka/Tersembunyi | jum_art_1345 | 4 |
| 14 | `jum_art_1345_umurkur10` | Angka/Tersembunyi | jum_art_1345_umurkur10 | 0 |
| 15 | `jum_kk_lebihdr10th` | Angka/Tersembunyi | jum_kk_lebihdr10th | 1 |
| 16 | `jum_kk` | Angka/Tersembunyi | jum_kk | 1 |
| 17 | `nested_dtsen` | Tabel (Datagrid) | Keterangan Anggota Keluarga |  |
| 18 | `isprelistart` | Angka/Tersembunyi | Apakah prelist art |  |
| 19 | `no_urut_kk` | Angka/Tersembunyi | 5. Nomor urut anggota keluarga |  |
| 20 | `nama_dtsen` | Angka/Tersembunyi | 6. Nama anggota keluarga |  |
| 21 | `nik_dtsen` | Pilihan Dropdown | 7. Nomor Induk Kependudukan (NIK) $NAME$ (Tulis sesuai yang tercantum di KK atau KTP paling mutakhir) |  |
| 22 | `nik_dtsen_prelist` | Angka/Tersembunyi | nik_dtsen_prelist |  |
| 23 | `callnik_button` | Tombol (Radio) | CEK NIK |  |
| 24 | `hasilPemadananNIK` | Angka/Tersembunyi | Hasil Pengecekkan NIK |  |
| 25 | `hubungan` | Pilihan Dropdown | 8. Hubungan $NAME$ dengan Kepala Keluarga |  |
| 26 | `keberadaan_dtsen` | Pilihan Dropdown | 9. a. Keberadaan anggota keluarga |  |
| 27 | `alamat_dn` | Pilihan Dropdown | 9. b. Alamat domisili: |  |
| 28 | `prov_dn` | Pilihan Dropdown | a. Provinsi |  |
| 29 | `kab_dn` | Pilihan Dropdown | b. Kabupaten/Kota |  |
| 30 | `domisili_ln` | Pilihan Dropdown | 10LN. Negara domisili Individu (luar negeri) |  |
| 31 | `status_kawin` | Pilihan Dropdown | 11. Apakah status perkawinan $NAME$ |  |
| 32 | `jk_prelist` | Angka/Tersembunyi | jk_prelist |  |
| 33 | `jk_dtsen` | Pilihan Dropdown | 12. Jenis Kelamin $NAME$ |  |
| 34 | `tgl_lahir` | Pilihan Dropdown | Tanggal Lahir |  |
| 35 | `bln_lahir` | Pilihan Dropdown | Bulan Lahir |  |
| 36 | `thn_lahir` | Isian Angka | Tahun Lahir |  |
| 37 | `umur_ak` | Isian Angka | 13. b. Umur $NAME$ |  |
| 38 | `art_ada_usaha` | Pilihan Dropdown | Apakah $NAME$ memiliki usaha berikut? $daftar_usaha |  |

---

## 📁 SE2026 - L BLOK II

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `nama_usaha_tambahan` | Tabel Isian | Nama Usaha Tambahan | [{"label": "lastId#0", "value": "0"}] |
| 2 | `se2026_nested` | Tabel (Datagrid) | Keterangan Usaha/Perusahaan |  |
| 3 | `pilih_umkm_options` | Angka/Tersembunyi | Opsi Pilih UMKM dalam satu SLS yang sama |  |
| 4 | `pilih_umkm_sls` | Pilihan Dropdown | Pilih UMKM dalam satu SLS yang sama |  |
| 5 | `prov_l` | Angka/Tersembunyi | 1. Provinsi |  |
| 6 | `kab_l` | Angka/Tersembunyi | 2. Kabupaten/Kota |  |
| 7 | `kec_l` | Angka/Tersembunyi | 3. Kecamatan |  |
| 8 | `desa_l` | Angka/Tersembunyi | 4. Kelurahan/Desa/Nagari |  |
| 9 | `kodesls_l` | Angka/Tersembunyi | Kode SLS/Sub-SLS |  |
| 10 | `sls_l` | Angka/Tersembunyi | Nama SLS/Sub-SLS |  |
| 11 | `no_bang_l` | Angka/Tersembunyi | 6. Nomor Bangunan |  |
| 12 | `no_usaha` | Angka/Tersembunyi | 7. Nomor Urut Usaha/Perusahaan |  |
| 13 | `nama_usaha` | Angka/Tersembunyi | 8. a. Nama usaha/perusahaan |  |
| 14 | `keberadaan_usaha` | Pilihan Dropdown | Keberadaan Usaha |  |
| 15 | `nama_usaha_edit` | Pilihan Dropdown | 8. a. Nama usaha/perusahaan Tulis perbaikan nama usaha, jika tidak ada perubahan tulis ulang nama usaha/perusahaan |  |
| 16 | `skala_usaha` | Angka/Tersembunyi | skala_usaha |  |
| 17 | `is_prelist2` | Angka/Tersembunyi | Is_Prelist2 |  |
| 18 | `id_pmss` | Angka/Tersembunyi | id_pmss |  |
| 19 | `idsbr` | Angka/Tersembunyi | ID SBR |  |
| 20 | `kode_keberadaan_usaha` | Angka/Tersembunyi | Pilihan untuk keberadaan Usaha |  |
| 21 | `nama_komersial` | Pilihan Dropdown | 8. b. Nama komersial usaha/perusahaan Jika tidak memiliki nama komersial, maka tuliskan nama usaha/perusahaan. |  |
| 22 | `alamat_usaha_view` | Isian Teks Panjang | 8.c. Alamat usaha/perusahaan |  |
| 23 | `alamat_usaha_var` | Angka/Tersembunyi | 8. c. Alamat usaha/perusahaan |  |
| 24 | `alamat_usaha` | Angka/Tersembunyi | alamat_usaha |  |
| 25 | `kp_nested` | Tabel (Datagrid) | Daftar Kantor Cabang |  |
| 26 | `kp_unit` | Pilihan Dropdown | Nama Kantor/ Unit |  |
| 27 | `kp_jenis` | Pilihan Dropdown | Jenis Unit |  |
| 28 | `kp_prov` | Pilihan Dropdown | Provinsi |  |
| 29 | `kp_kab` | Pilihan Dropdown | Kabupaten |  |
| 30 | `kp_produksi_lingkungan` | Pilihan Dropdown | Apakah perusahaan ini memproduksi barang/jasa yang ramah lingkungan? |  |
| 31 | `kp_perlindungan_lingkungan` | Pilihan Dropdown | Apakah perusahaan ini mengeluarkan biaya perlindungan lingkungan dan/atau pembelian barang dan jasa yang ramah lingkungan |  |
| 32 | `kp_tk` | Isian Angka | Tenaga Kerja (per 31 Desember 2025) (orang) |  |
| 33 | `kp_total_pengeluaran` | Isian Angka (Rupiah) | Pengeluaran Tahun 2025 (Rupiah) |  |
| 34 | `kp_total_pendapatan` | Isian Angka (Rupiah) | Pendapatan Tahun 2025 (Rupiah) |  |
| 35 | `rt` | Pilihan Dropdown | RT |  |
| 36 | `rw` | Pilihan Dropdown | RW |  |
| 37 | `kode_pos` | Angka/Tersembunyi | Kode Pos |  |
| 38 | `kode_area` | Pilihan Dropdown | Kode Area |  |
| 39 | `no_telp` | Pilihan Dropdown | Nomor Telepon |  |
| 40 | `eks` | Pilihan Dropdown | Ekstensi |  |
| 41 | `email` | Pilihan Dropdown | Email |  |
| 42 | `hp` | Pilihan Dropdown | Nomor HP/whatsapp: |  |
| 43 | `website` | Pilihan Dropdown | Homepage/website Alamat website diawali dengan www. Contoh : www.bps.go.id |  |
| 44 | `jenis_kawasan` | Pilihan Dropdown | 8. d. Jenis kawasan beroperasi |  |
| 45 | `nama_kek_ki` | Pilihan Dropdown | 8. e. Nama KEK/KI |  |
| 46 | `nama_kawasan` | Pilihan Dropdown | 8. e. Nama kawasan Contoh: KEK Mandalika, Kawasan Industri Jababeka, Stasiun Gambir, Bandara Soekarno-Hatta, Pelabuhan Tanjung Priok, Terminal Pulo Gebang, Rest Area KM 57 Tol Jakarta–Cikampek, Sentra Batik Laweyan, Kompleks Pertokoan ITC Mangga Dua |  |
| 47 | `jenis_usaha` | Pilihan Dropdown | 9. a. Apa jenis usaha/perusahaan ini? |  |
| 48 | `alamat_usaha_utama` | Isian Teks Panjang | 9. b1. Alamat/lokasi usaha utama |  |
| 49 | `prov_usaha_utama` | Pilihan Dropdown | 9. b2. Provinsi |  |
| 50 | `kab_usaha_utama` | Pilihan Dropdown | 9. b3. Kabupaten/Kota |  |
| 51 | `punya_nib` | Pilihan Dropdown | 10. a. Apakah memiliki Nomor Induk Berusaha (NIB)? |  |
| 52 | `nib` | Pilihan Dropdown | 10. b. Tuliskan NIB: |  |
| 53 | `hasilCekNIB` | Angka/Tersembunyi | ​ |  |
| 54 | `tidak_nib` | Pilihan Dropdown | 10. c. Apa alasan utama tidak memiliki NIB? |  |
| 55 | `nib_lainnya` | Pilihan Dropdown | 10. c. Lainnya, tuliskan.... |  |
| 56 | `badan_usaha` | Pilihan Dropdown | 11. a. Apa status badan usaha dari usaha/perusahaan ini? |  |
| 57 | `koperasi_kdkmp` | Pilihan Dropdown | 11. b. Apakah koperasi ini merupakan Koperasi Desa/Kelurahan Merah Putih (KDKMP)? |  |
| 58 | `jenis_koperasi` | Pilihan Dropdown | 11. c. Apa jenis koperasi ini berdasarkan layanannya? |  |
| 59 | `lap_keuangan` | Pilihan Dropdown | 11. d. Apakah mempunyai laporan/catatan keuangan? |  |
| 60 | `pengusaha_var_prelist` | Angka/Tersembunyi | pengusaha_var_prelist |  |
| 61 | `pengusaha_var` | Pilihan Dropdown | 12. a. Nama Pengusaha / Penanggung Jawab |  |
| 62 | `pengusaha` | Pilihan Dropdown | 12. a. Nama Pengusaha / Penanggung Jawab |  |
| 63 | `jk_var` | Angka/Tersembunyi | 12. b. Jenis Kelamin |  |
| 64 | `jk` | Pilihan Dropdown | 12. b. Jenis Kelamin |  |
| 65 | `umur_pj_var` | Angka/Tersembunyi | 12. c. Umur |  |
| 66 | `umur` | Isian Angka | 12. c. Umur |  |
| 67 | `nik_pengusaha_var` | Angka/Tersembunyi | 12. d. Nomor Induk Kependudukan (NIK ) |  |
| 68 | `nik_pengusaha` | Pilihan Dropdown | 12. d. Nomor Induk Kependudukan (NIK) |  |
| 69 | `callnik_button_l` | Tombol (Radio) | CEK NIK |  |
| 70 | `hasilPemadananNIK_l` | Angka/Tersembunyi | Hasil Pengecekkan NIK |  |
| 71 | `keg_utama` | Pilihan Dropdown | 13. a. Apa kegiatan utama usaha/perusahaan ini? Tuliskan selengkapnya |  |
| 72 | `jenis_kegiatan` | Angka/Tersembunyi | jenis_kegiatan |  |
| 73 | `produk_sendiri` | Pilihan Dropdown | 13. b1. Apakah memproduksi barang di lokasi ini? |  |
| 74 | `layanan_mamin` | Pilihan Dropdown | 13. b2. Apakah menyediakan layanan makan minum? Ciri: terdapat kegiatan peracikkan, pemanasan ulang, atau pembuatan produk berdasarkan pesanan/permintaan pelanggan |  |
| 75 | `keg_penjualan` | Pilihan Dropdown | 13. b3. Apakah melakukan penjualan barang? |  |
| 76 | `keg_jasa` | Pilihan Dropdown | 13. b4. Pilih salah satu aktivitas yang dilakukan: |  |
| 77 | `lokasi_usaha` | Pilihan Dropdown | 13. c. Di mana usaha tersebut biasa dilakukan? |  |
| 78 | `input` | Isian Teks Panjang | 13. d. Apa input yang digunakan? Contoh: daging ikan, tepung; daging kebab, kulit kebab, sayuran; bambu; jagung pipil; kaca; kain; kulit sapi; kayu bulat; rotan; kunci polos |  |
| 79 | `proses` | Isian Teks Panjang | 13. e. Bagaimana proses mengubah input tersebut menjadi produk output (beserta alatnya)? Contoh: menggiling daging ikan menjadi sosis; membuat kebab di rumah dan sudah dikemasi kemudian dititipkan di warung; penggaraman; pengasapan; pemindangan; pembekuan. |  |
| 80 | `produk` | Pilihan Dropdown | 13. f. Apa produk utama yang dihasilkan? |  |
| 81 | `genai_button` | Tombol (Radio) | DAPATKAN REKOMENDASI KBLI |  |
| 82 | `kbli_prelist` | Angka/Tersembunyi | kbli_prelist |  |
| 83 | `kbli_genai` | Pilihan Dropdown | 13. g. Kode KBLI |  |
| 84 | `kbli` | Pilihan Dropdown | Pilih dari Master KBLI |  |
| 85 | `kbli_genai_cawi` | Angka/Tersembunyi | kbli_genai_cawi |  |
| 86 | `kbli_cawi` | Angka/Tersembunyi | kbli_cawi |  |
| 87 | `kbli_akhir` | Angka/Tersembunyi | KBLI Akhir |  |
| 88 | `kategori_2025` | Angka/Tersembunyi | kategori_2025 |  |
| 89 | `kategori` | Angka/Tersembunyi | 13. h. Kategori Lapangan Usaha: |  |
| 90 | `klasifikasi` | Pilihan Dropdown | 13. i. Jika usaha/perusahaan merupakan akomodasi jangka pendek, apa klasifikasi usaha/perusahaan ini? |  |
| 91 | `jaringan` | Pilihan Dropdown | 14. a. Apa jaringan usaha dari usaha/perusahaan ini? |  |
| 92 | `jumlah_kc` | Isian Angka | 14. b. Berapa jumlah seluruh kantor cabang dan unit usaha yang berada di bawah kantor pusat? |  |
| 93 | `nama_kp` | Pilihan Dropdown | 15. a. Nama Kantor Pusat |  |
| 94 | `alamat_kp` | Isian Teks Panjang | 15. b. Alamat Kantor Pusat |  |
| 95 | `email_kp` | Pilihan Dropdown | 15. c. Email |  |
| 96 | `negara_kp` | Pilihan Dropdown | 15. d. Negara |  |
| 97 | `prov_kp` | Pilihan Dropdown | 15. e. Provinsi |  |
| 98 | `kab_kp` | Pilihan Dropdown | 15. f. Kabupaten/Kota |  |
| 99 | `internet` | Pilihan Dropdown | 16. a. Apakah usaha/perusahaan ini menggunakan internet dalam menjalankan usaha? |  |
| 100 | `internet_produksi` | Pilihan Dropdown | 16. b2. Produksi barang/jasa |  |
| 101 | `internet_pesanan` | Pilihan Dropdown | 16. b1. Menerima pesanan barang/jasa |  |
| 102 | `internet_distribusi` | Pilihan Dropdown | 16. b3. Distribusi barang/jasa |  |
| 103 | `internet_beli` | Pilihan Dropdown | 16. b4. Membeli bahan baku online |  |
| 104 | `internet_promosi` | Pilihan Dropdown | 16. b5. Promosi |  |
| 105 | `internet_lainnya` | Pilihan Dropdown | 16. b6. Lainnya |  |
| 106 | `digital` | Pilihan Dropdown | 16. c. Apakah usaha/perusahaan ini memanfaatkan teknologi digital Aritifical Intelligence (AI), Internet of Things (IoT), big data, printer 3D, blockchain, atau cloud computing? |  |
| 107 | `produksi_lingkungan` | Pilihan Dropdown | 17. a. Apakah usaha/perusahaan ini memproduksi barang/jasa yang ramah lingkungan? Contoh: Produk efisiensi energi (lampu atau mesin hemat listrik); Energi terbarukan (panel surya, turbin angin, biogas); Kendaraan ramah lingkungan (kendaraan listrik/ hybrid); Produk berbahan daur ulang (kertas/plastik daur ulang, kemasan ramah lingkungan); Jasa pengelolaan dan pembersihan limbah dan sampah (pengolahan sampah/ air limbah, daur ulang) |  |
| 108 | `perlindungan_lingkungan` | Pilihan Dropdown | 17. b. Apakah usaha/perusahaan ini menggunakan input untuk tujuan perlindungan lingkungan dan/atau pembelian barang dan jasa yang ramah lingkungan? Contoh: Pengeluaran untuk pengelolaan dan pembersihan limbah dan sampah, pengendalian polusi udara, perbaikan tanah/ air tanah, pengurangan kebisingan, pelestarian alam/keanekaragaman hayati, audit/ penilaian lingkungan |  |
| 109 | `produk_seni` | Pilihan Dropdown | 18. Apakah usaha/perusahaan ini menggunakan produk karya seni, sastra, desain, teknologi atau warisan budaya, baik diproduksi sendiri maupun oleh pihak lain? Contoh produk karya seni: lukisan, patung, kerajinan, musik, tari, foto, film, ilustrasi, animasi, board game, dll. Contoh produk sastra: puisi, cerpen, novel, naskah drama, dll. Contoh produk desain: arsitektur, desain produk, desain interior, desain komunikasi visual, desain fesyen, dll. Contoh produk teknologi: perangkat lunak (software), aplikasi digital, aplikasi gim, perangkat elektronik, dll. Contoh produk warisan budaya: makanan tradisional, peralatan tradisional, obat tradisional, dll. |  |
| 110 | `halal` | Pilihan Dropdown | 19. a. Apakah usaha/perusahaan ini menghasilkan produk bersertifikat halal? Rincian 19 hanya ditanyakan kepada kategori usaha/perusahaan khusus berdasarkan BPJPH. |  |
| 111 | `sudah_halal` | Isian Angka | 19. b. Berapa jumlah varian produk yang sudah bersertifikat halal BPJPH? |  |
| 112 | `belum_halal` | Isian Angka | 19. c. Berapa jumlah varian produk yang belum bersertifikat halal BPJPH? |  |
| 113 | `izin_edar` | Pilihan Dropdown | 20. a. Apakah usaha/perusahaan ini memiliki izin edar? Rincian 20 hanya ditanyakan kepada kategori usaha/perusahaan khusus berdasarkan BPOM. |  |
| 114 | `sudah_bpom` | Isian Angka | 20. b. Berapa jumlah varian produk yang sudah memiliki izin edar BPOM? |  |
| 115 | `belum_bpom` | Isian Angka | 20. c. Berapa jumlah varian produk yang belum memiliki izin edar BPOM? |  |
| 116 | `mitra_kdkmp` | Pilihan Dropdown | 21. Apakah usaha/perusahaan ini bermitra dengan Koperasi Desa/Kelurahan Merah Putih (KDKMP)? |  |
| 117 | `peran_mbg` | Pilihan Dropdown | 22. Apakah usaha/perusahaan ini terlibat dalam program Makan Bergizi Gratis (MBG)? |  |
| 118 | `barang_non_pddk` | Pilihan Dropdown | 23. a. Penjualan dan/atau pembelian barang |  |
| 119 | `jasa_non_pddk` | Pilihan Dropdown | 23. b. Penjualan jasa |  |
| 120 | `beli_jasa_non_pddk` | Pilihan Dropdown | 23. c. Pembelian jasa |  |
| 121 | `tk_laki` | Isian Angka | 24. a1. Pekerja laki-laki |  |
| 122 | `tk_pr` | Isian Angka | 24. b1. Pekerja perempuan |  |
| 123 | `total_tk_jk` | Isian Angka | 24. c1. Total pekerja (a1+b1) |  |
| 124 | `total_tk_jk_var` | Angka/Tersembunyi | total_tk_jk_var |  |
| 125 | `tk_dibayar` | Isian Angka | 24. a2. Pekerja dibayar |  |
| 126 | `tk_tdk_dibayar` | Isian Angka | 24. b2. Pekerja tidak dibayar |  |
| 127 | `total_tk_bayar` | Isian Angka | 24. c2. Total pekerja (a2+b2) |  |
| 128 | `total_tk_bayar_var` | Angka/Tersembunyi | total_tk_bayar_var |  |
| 129 | `tahun_operasi` | Isian Angka | 25. Tahun berapa usaha/perusahaan ini mulai beroperasi secara komersial? Tahun beroperasi komersial terdiri dari 4 angka. Contoh: 1990; 2025;dsb. |  |
| 130 | `gaji` | Isian Angka (Rupiah) | 26. a. Total upah dan gaji, serta jaminan sosial pegawai |  |
| 131 | `biaya_produksi` | Isian Angka (Rupiah) | 26. b. Biaya produksi |  |
| 132 | `biaya_pembelian` | Isian Angka (Rupiah) | 26. c. Biaya pembelian barang yang terjual |  |
| 133 | `operasional` | Isian Angka (Rupiah) | 26. d. Biaya operasional (air, listrik, gas, internet, pulsa, pemeliharaan, biaya angkutan, dll.) |  |
| 134 | `non_operasional` | Isian Angka (Rupiah) | 26. e. Biaya non-operasional |  |
| 135 | `total_pengeluaran_var` | Angka/Tersembunyi | total_pengeluaran_var |  |
| 136 | `total_pengeluaran` | Isian Angka (Rupiah) | 26. f. Total pengeluaran (a+b+c+d+e) |  |
| 137 | `nilai_pendapatan` | Isian Angka (Rupiah) | 27. a. Nilai $narasi barang dan jasa |  |
| 138 | `pendapatan_lain` | Isian Angka (Rupiah) | 27. b. Pendapatan lainnya yang dihasilkan perusahaan |  |
| 139 | `total_pendapatan` | Isian Angka (Rupiah) | 27. c. Total nilai $narasi (a+b) |  |
| 140 | `total_pendapatan_var` | Angka/Tersembunyi | total_pendapatan_var |  |
| 141 | `pendapatan_online` | Isian Angka | 27. d. Berapa persentase pendapatan yang dilakukan secara online ? |  |
| 142 | `aset_usaha_thn` | Isian Angka (Rupiah) | 28. a. Nilai aset tanah dan bangunan pada 31 Desember 2025 |  |
| 143 | `aset_lain_thn` | Isian Angka (Rupiah) | 28. b. Nilai aset selain tanah dan bangunan pada 31 Desember 2025 |  |
| 144 | `total_aset_thn` | Isian Angka (Rupiah) | 28. c. Nilai total aset pada 31 Desember 2025 |  |
| 145 | `total_aset_thn_var` | Angka/Tersembunyi | total_aset_thn_var |  |
| 146 | `rentang_aset_thn` | Pilihan Dropdown | 28. c1. Jika tidak dapat mengisikan nilai nominal, pilih nilai total aset dalam rentang berikut |  |
| 147 | `luas_tanah_thn` | Isian Angka | 28. d. Berapa luas tanah yang dikuasai dan digunakan untuk kegiatan usaha pada 31 Desember 2025 ? (m2) |  |
| 148 | `pribadi` | Isian Angka | 29. a. Pribadi/Perorangan |  |
| 149 | `non_profit` | Isian Angka | 29. b. Lembaga Nonprofit yang Melayani Rumah Tangga |  |
| 150 | `publik` | Isian Angka | 29. c. Korporasi Publik |  |
| 151 | `non_publik` | Isian Angka | 29. d. Korporasi Non Publik |  |
| 152 | `pemerintah` | Isian Angka | 29. e. Pemerintah |  |
| 153 | `asing` | Isian Angka | 29. f. Asing |  |
| 154 | `gaji_bln` | Isian Angka (Rupiah) | 30. a. Total upah dan gaji, serta jaminan sosial pegawai |  |
| 155 | `biaya_produksi_bln` | Isian Angka (Rupiah) | 30. b. Biaya produksi |  |
| 156 | `biaya_pembelian_bln` | Isian Angka (Rupiah) | 30. c. Biaya pembelian barang yang terjual |  |
| 157 | `operasional_bln` | Isian Angka (Rupiah) | 30. d. Biaya operasional (air, listrik, gas, internet, pulsa, pemeliharaan, biaya angkutan) |  |
| 158 | `non_operasional_bln` | Isian Angka (Rupiah) | 30. e. Biaya non-operasional |  |
| 159 | `total_pengeluaran_bln` | Isian Angka (Rupiah) | 30. f. Total pengeluaran (a+b+c+d+e) |  |
| 160 | `total_pengeluaran_bln_var` | Angka/Tersembunyi | total_pengeluaran_bln |  |
| 161 | `nilai_pendapatan_bln` | Isian Angka (Rupiah) | 31. a. Nilai $narasi barang dan jasa |  |
| 162 | `pendapatan_lain_bln` | Isian Angka (Rupiah) | 31. b. Pendapatan lainnya yang dihasilkan |  |
| 163 | `total_pendapatan_bln` | Isian Angka (Rupiah) | 31. c. Total nilai $narasi (a+b) |  |
| 164 | `total_pendapatan_bln_var` | Angka/Tersembunyi | total_pendapatan_bln_var |  |
| 165 | `pendapatan_online_bln` | Isian Angka | 31. d. Berapa persentase pendapatan yang dilakukan secara online ? |  |
| 166 | `bln_operasi` | Slider/Angka | 31. e. Bulan beroperasi selama tahun 2026 |  |
| 167 | `aset_tanah_bln` | Isian Angka (Rupiah) | 32. a. Nilai aset tanah dan bangunan pada akhir bulan yang lalu |  |
| 168 | `aset_lain_bln` | Isian Angka (Rupiah) | 32. b. Nilai aset selain tanah dan bangunan pada akhir bulan yang lalu |  |
| 169 | `total_aset_bln` | Angka/Tersembunyi | 32. c. Nilai total aset pada akhir bulan yang lalu* |  |
| 170 | `rentang_aset_bln` | Pilihan Dropdown | 32. c1. Jika tidak dapat mengisikan nilai nominal, pilih nilai total aset dalam rentang berikut: |  |
| 171 | `luas_tanah_bln` | Isian Angka | 32. d. Berapa luas tanah yang dikuasai dan digunakan untuk kegiatan usaha pada akhir bulan yang lalu (m2) ? |  |
| 172 | `pribadi_didirikan` | Isian Angka | 33. a. Pribadi/Perorangan |  |
| 173 | `nonprofit_didirikan` | Isian Angka | 33. b. Lembaga Nonprofit yang Melayani Rumah Tangga |  |
| 174 | `publik_didirikan` | Isian Angka | 33. c. Korporasi publik (%) |  |
| 175 | `nonpublik_didirikan` | Isian Angka | 33. d. Korporasi Non Publik |  |
| 176 | `pemerintah_didirikan` | Isian Angka | 33. e. Pemerintah |  |
| 177 | `asing_didirikan` | Isian Angka | 33. f. Asing |  |

---

## 📁 SE2026 - L BLOK III

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `dtsen_nama_kk` | Angka/Tersembunyi | 1. a. Nama Kepala Keluarga | RIKADIUS HANDOKO |
| 2 | `nik_kk` | Angka/Tersembunyi | 1. b. NIK Kepala Keluarga | 6104020705940001 |
| 3 | `dtsen_no_kk` | Angka/Tersembunyi | 1. c. Nomor kartu keluarga | 6104020608140004 |
| 4 | `jml_kk` | Angka/Tersembunyi | 2. a. Jumlah anggota keluarga sesuai KK | 4 |
| 5 | `jml_kk_asgbaru` | Pilihan Dropdown | 2. a. Jumlah anggota keluarga sesuai KK |  |
| 6 | `jml_kk_update` | Angka/Tersembunyi | 2. b. Jumlah anggota keluarga sesuai hasil pendataan | 4 |
| 7 | `prelist_dtsen_var` | Angka/Tersembunyi | Nama anggota keluarga prelist |  |
| 8 | `tambah_dtsen_var` | Angka/Tersembunyi | Nama anggota keluarga tambahan |  |
| 9 | `gabung_dtsen_var` | Angka/Tersembunyi | gabung_dtsen | [{"label": "RIKADIUS HANDOKO", "value": 1, "is_prelist": ... |
| 10 | `gabung_dtsen_2` | Angka/Tersembunyi | gabung_dtsen_2 | [{"no_urut": 1, "label": "RIKADIUS HANDOKO", "value": 1, ... |
| 11 | `total_pendapatan_keluarga_sebulan` | Angka/Tersembunyi | total_pendapatan_keluarga_sebulan (sudah dari semua anggota keluarga) | 2510000 |
| 12 | `nested_dtsen_var` | Tabel (Datagrid) | Keterangan Anggota Keluarga |  |
| 13 | `no_urut_kk_var` | Angka/Tersembunyi | Nomor urut anggota keluarga |  |
| 14 | `nama_dtsen_var` | Angka/Tersembunyi | Nama anggota keluarga |  |
| 15 | `sekolah_prelist` | Angka/Tersembunyi | Sekolah Prelist |  |
| 16 | `sekolah` | Pilihan Dropdown | 14. Partisipasi sekolah $NAME$ (usia 5 tahun ke atas) |  |
| 17 | `ijazah_prelist` | Angka/Tersembunyi | Ijazah Prelist |  |
| 18 | `ijazah` | Pilihan Dropdown | 15. Ijazah/STTB tertinggi yang dimiliki $NAME$ (usia 5 tahun ke atas) Ijazah/STTB tertinggi di prelist: $ijazah |  |
| 19 | `profesi` | Pilihan Dropdown | 16. Profesi Pekerjaan Utama $NAME$ (usia 10 tahun ke atas) |  |
| 20 | `profesi_lainnya` | Pilihan Dropdown | Profesi Pekerjaan Utama lainnya: |  |
| 21 | `status_kerja` | Pilihan Dropdown | 17. Status Kedudukan Dalam Pekerjaan Utama $NAME$ (usia 10 tahun ke atas) |  |
| 22 | `pendapatan_pekerjaan` | Pilihan Dropdown | 18. a. Pendapatan dari pekerjaan baik berupa uang maupun barang/jasa (gaji, tunjangan, uang makan, honor, lembur, dll) |  |
| 23 | `pend_gaji` | Isian Angka (Rupiah) | a. Upah/Gaji |  |
| 24 | `pend_tunjangan` | Isian Angka (Rupiah) | b. Tunjangan |  |
| 25 | `pend_uangmkn` | Isian Angka (Rupiah) | c. Uang Makan |  |
| 26 | `pend_honor` | Isian Angka (Rupiah) | d. Honor |  |
| 27 | `pend_lembur` | Isian Angka (Rupiah) | e. Lembur |  |
| 28 | `pend_lainnya` | Isian Angka (Rupiah) | f. Lainnya |  |
| 29 | `nilai_pend_pekerjaan` | Angka/Tersembunyi | 18. a1. Total Pendapatan (a+b+c+d+e+f) |  |
| 30 | `pendapatan_usaha` | Pilihan Dropdown | 18. b. Pendapatan dari usaha, baik offline (warung, kos-kosan, dll) maupun online (affiliate, online shop, endorse, youtuber, dll ): |  |
| 31 | `pend_usaha` | Isian Angka (Rupiah) | 18. b1. Total Pendapatan |  |
| 32 | `pend_usaha_lain` | Pilihan Dropdown | 18. c. Penerimaan pendapatan lain (transfer/pemberian/passive income seperti pensiunan, kupon SBN, Obligasi, dll ): |  |
| 33 | `nilai_pend_lain` | Isian Angka (Rupiah) | 18. c1. Total Pendapatan |  |
| 34 | `rekening` | Pilihan Dropdown | 19. Apakah $NAME$ memiliki rekening aktif atau dompet digital? (usia 5 tahun ke atas) |  |
| 35 | `dis_fisik` | Pilihan Dropdown | a. Disabilitas Fisik |  |
| 36 | `dis_mental` | Pilihan Dropdown | b. Disabilitas Mental |  |
| 37 | `dis_intelek` | Pilihan Dropdown | c. Disabilitas Intelektual |  |
| 38 | `dis_netra` | Pilihan Dropdown | d. Disabilitas Sensorik Netra |  |
| 39 | `dis_rungu` | Pilihan Dropdown | e. Disabilitas Sensorik Rungu |  |
| 40 | `dis_wicara` | Pilihan Dropdown | f. Disabilitas Sensorik Wicara |  |
| 41 | `sakit_hipertensi` | Pilihan Dropdown | a. Hipertensi (tekanan darah tinggi) |  |
| 42 | `sakit_rematik` | Pilihan Dropdown | b. Rematik |  |
| 43 | `sakit_asma` | Pilihan Dropdown | c. Asma |  |
| 44 | `sakit_jantung` | Pilihan Dropdown | d. Masalah jantung |  |
| 45 | `sakit_diabetes` | Pilihan Dropdown | e. Diabetes (kencing manis) |  |
| 46 | `sakit_tbc` | Pilihan Dropdown | f. Tuberkulosis (TBC) |  |
| 47 | `sakit_stroke` | Pilihan Dropdown | g. Stroke |  |
| 48 | `sakit_kanker` | Pilihan Dropdown | h. Kanker atau tumor ganas |  |
| 49 | `sakit_hemofilia` | Pilihan Dropdown | j. Hemofilia |  |
| 50 | `sakit_ginjal` | Pilihan Dropdown | i. Gagal ginjal |  |
| 51 | `sakit_hiv` | Pilihan Dropdown | k. HIV/AIDS |  |
| 52 | `sakit_kolestrol` | Pilihan Dropdown | l. Kolestrol |  |
| 53 | `sakit_sirosis` | Pilihan Dropdown | m. Sirosis hati |  |
| 54 | `sakit_talasemia` | Pilihan Dropdown | n. Talasemia |  |
| 55 | `sakit_leukemia` | Pilihan Dropdown | o. Leukemia |  |
| 56 | `sakit_alzheimer` | Pilihan Dropdown | p. Alzheimer |  |
| 57 | `sakit_lainnya` | Pilihan Dropdown | q. Lainnya |  |

---

## 📁 SE2026 - L BLOK IV

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `total_pengeluaran_keluarga_sebulan` | Angka/Tersembunyi | total_pengeluaran_keluarga_sebulan | 2671428.571428572 |
| 2 | `jns_bangunan` | Pilihan Dropdown | 1. a. Apa jenis bangunan tempat tinggal yang ditempati? | [{"description": "", "label": "1. Rumah tunggal", "value"... |
| 3 | `jns_bangunan_lain` | Pilihan Dropdown | 1. a. Jenis bangunan tempat tinggal kode 5.Lainnya: ................. |  |
| 4 | `nm_apt` | Pilihan Dropdown | 1. b. Jika apartemen/rumah susun, sebutkan Nama/Nomor Lantai: . |  |
| 5 | `jml_ak_tinggal` | Isian Angka | 2. a. Berapa jumlah keluarga yang tinggal dalam 1 rumah/tempat tinggal? | 1 |
| 6 | `list_ak_tinggal` | Tabel Isian | 2. b. Sebutkan Nomor KK dari keluarga yang tinggal dalam 1 rumah/tempat tinggal! Selain yang disebutkan pada |  |
| 7 | `status_kepemilikan` | Pilihan Dropdown | 3. a. Apa status kepemilikan bangunan tempat tinggal yang ditempati? | [{"label": "Milik sendiri", "value": 1}] |
| 8 | `status_kepemilikan_lain` | Pilihan Dropdown | 3. a. Deskripsi status kepemilikan bangunan tempat tinggal yang ditempati lainnya |  |
| 9 | `bukti_kepemilikan` | Pilihan Dropdown | 3. b. Jika tempat tinggal milik sendiri, apa jenis bukti kepemilikan tanah bangunan tempat tinggal ini? | [{"description": "", "label": "4. Tidak Punya", "value": ... |
| 10 | `sewa_sendiri` | Isian Angka (Rupiah) | a. Jika milik sendiri/bebas sewa, perkiraan harga sewa sebulan: | 500000 |
| 11 | `sewa_kontrak` | Isian Angka (Rupiah) | b. Jika kontrak/sewa , nilai kontrak sebulan: |  |
| 12 | `sewa_dinas` | Isian Angka (Rupiah) | c. Jika dinas atau lainnya, perkiraan nilai sewa sebulan: |  |
| 13 | `luas_lantai` | Isian Angka | 5. Berapa luas lantai bangunan tempat tinggal? (m²) | 77 |
| 14 | `jns_lantai` | Pilihan Dropdown | 6. a. Apakah bahan bangunan utama lantai rumah terluas? | [{"label": "Keramik", "value": 2}] |
| 15 | `kondisi_lantai` | Pilihan Dropdown | 6. b. Kondisi Lantai | [{"description": "", "label": "1. Baik", "value": "1", "o... |
| 16 | `jns_dinding` | Pilihan Dropdown | 7. a. Apakah bahan bangunan utama dinding rumah terluas? | [{"label": "Tembok", "value": 1}] |
| 17 | `kondisi_dinding` | Pilihan Dropdown | 7. b. Kondisi Dinding | [{"description": "", "label": "1. Baik", "value": "1", "o... |
| 18 | `jns_atap` | Pilihan Dropdown | 8. a. Apakah bahan bangunan utama atap rumah terluas? | [{"label": "Seng", "value": 3}] |
| 19 | `kondisi_atap` | Pilihan Dropdown | 8. b. Kondisi Atap | [{"description": "", "label": "1. Baik", "value": "1", "o... |
| 20 | `tempat_bab` | Pilihan Dropdown | 9. Apakah memiliki fasilitas tempat buang air besar dan siapa saja yang menggunakan? | [{"description": "", "label": "1. Ada, digunakan oleh ang... |
| 21 | `jns_closet` | Pilihan Dropdown | 10. Apakah jenis kloset yang digunakan? | [{"description": "", "label": "4. Cemplung/cubluk", "valu... |
| 22 | `buang_tinja` | Pilihan Dropdown | 11. Di manakah tempat pembuangan akhir tinja? | [{"description": "", "label": "4. Lubang tanah", "value":... |
| 23 | `air_minum` | Pilihan Dropdown | 12. Apakah sumber air utama yang digunakan keluarga untuk minum? | [{"label": "05. Sumur terlindung", "value": "05"}] |
| 24 | `sumber_penerangan` | Pilihan Dropdown | 13. Apakah sumber utama penerangan rumah tangga ini? | [{"description": "", "label": "1. Listrik PLN dengan mete... |
| 25 | `jml_meteran` | Isian Angka | 14. a. Jika listrik PLN dengan meteran, berapa jumlah meteran listrik yang terpasang di rumah ini? | 1 |
| 26 | `nested_meteran` | Tabel (Datagrid) | 14. b. Berapa daya yang terpasang di rumah ini? |  |
| 27 | `urutan_meteran_lain` | Angka/Tersembunyi | Meteran ke- |  |
| 28 | `daya_terpasang` | Pilihan Dropdown | 14. b. Berapa daya yang terpasang di rumah ini? |  |
| 29 | `id_pln_pilih` | Pilihan Dropdown | 14. c. Sebutkan ID Pelanggan PLN atau Nomor Meteran |  |
| 30 | `id_pelanggan` | Pilihan Dropdown | ID Pelanggan PLN |  |
| 31 | `hasilCekIdPel` | Angka/Tersembunyi | ​ |  |
| 32 | `no_meteran` | Pilihan Dropdown | Nomor Meteran |  |
| 33 | `hasilCekMeteran` | Angka/Tersembunyi | ​ |  |
| 34 | `listrik_sebulan` | Isian Angka (Rupiah) | 15. a. Berapa nilai pengeluaran listrik sebulan? (Dapat menggunakan pertanyaan seperti: biasanya, rata-rata, atau sebulan terakhir) | 250000 |
| 35 | `pulsa_sebulan` | Isian Angka (Rupiah) | 15. b. Berapa pengeluaran pulsa dan internet seluruh anggota keluarga sebulan? (Dapat menggunakan pertanyaan seperti: biasanya, rata-rata, atau sebulan terakhir) | 150000 |
| 36 | `pengeluaran_makanan_mingguan` | Isian Angka (Rupiah) | 16. a. Berapa rata-rata pengeluaran makanan keluarga seminggu? | 250000 |
| 37 | `jml_meteran_var` | Angka/Tersembunyi | jml_meteran_var | 1 |
| 38 | `pengeluaran_non_makan_bulanan` | Isian Angka (Rupiah) | 16. b. Berapa rata-rata pengeluaran bukan makanan rutin keluarga bulanan? | 800000 |
| 39 | `pengeluaran_non_makan_tahunan` | Isian Angka (Rupiah) | 16. c. Berapa rata-rata pengeluaran bukan makanan rutin keluarga tahunan? | 9600000 |
| 40 | `jumlah_tabung3kg` | Angka/Tersembunyi | jumlah_tabung3kg_prelist |  |
| 41 | `jumlah_tabung3kg_new` | Isian Angka | a. Tabung gas 3 kg (unit) | 1 |
| 42 | `jumlah_tabung5kg` | Angka/Tersembunyi | jumlah_tabung5kg_prelist |  |
| 43 | `jumlah_tabung5kg_new` | Isian Angka | b. Tabung gas 5,5 kg atau lebih (unit) | 0 |
| 44 | `jumlah_kulkas` | Angka/Tersembunyi | jumlah_kulkas_prelist | 1 |
| 45 | `jumlah_kulkas_new` | Isian Angka | c. Lemari es/kulkas (unit) | 1 |
| 46 | `jumlah_ac` | Angka/Tersembunyi | jumlah_ac_prelist | 2 |
| 47 | `jumlah_ac_new` | Isian Angka | d. Air Conditioner (AC) (unit) | 0 |
| 48 | `jumlah_emas` | Angka/Tersembunyi | jumlah_emas_prelist | 0 |
| 49 | `jumlah_emas_new` | Isian Angka | e. Emas/perhiasan (gram) | 2 |
| 50 | `jumlah_laptop` | Angka/Tersembunyi | jumlah_laptop_prelist | 1 |
| 51 | `jumlah_laptop_new` | Isian Angka | f. Komputer/laptop/tablet: (unit) | 0 |
| 52 | `jumlah_motor` | Angka/Tersembunyi | jumlah_motor_prelist | 1 |
| 53 | `jumlah_motor_new` | Isian Angka | g. i. Sepeda motor (termasuk sepeda motor listrik): | 1 |
| 54 | `nilai_motor` | Isian Angka (Rupiah) | g. ii. Total nilai aset sepeda motor (rupiah) | 8000000 |
| 55 | `jumlah_mobil` | Angka/Tersembunyi | jumlah_mobil_prelist | 1 |
| 56 | `jumlah_mobil_new` | Isian Angka | h. i. Mobil (termasuk mobil listrik): | 0 |
| 57 | `nilai_mobil` | Isian Angka (Rupiah) | h. ii. Total nilai aset mobil (rupiah) |  |
| 58 | `jumlah_lahan` | Angka/Tersembunyi | jumlah_lahan_prelist |  |
| 59 | `jumlah_lahan_new` | Isian Angka | a. i. Jumlah tanah/lahan di tempat lain (selain yang ditempati): | 1 |
| 60 | `nilai_lahan` | Isian Angka (Rupiah) | a. ii. Total nilai harga jual tanah/lahan di tempat lain (selain yang ditempati): | 15000000 |
| 61 | `jumlah_rumah` | Angka/Tersembunyi | jumlah_rumah_prelist |  |
| 62 | `jumlah_rumah_new` | Isian Angka | b. i. Jumlah rumah/bangunan di tempat lain (selain yang ditempati): | 0 |
| 63 | `nilai_rumah` | Isian Angka (Rupiah) | b. ii. Total nilai harga jual rumah/bangunan di tempat lain (selain yang ditempati): |  |
| 64 | `foto_depan` | Upload Foto | Foto tampak depan (harus mencakup atap dan dinding) | [{"filename": "b00cf5df-c3f6-42d6-96a0-3b5aa6a6fcf9__foto... |
| 65 | `foto_ruang_tamu` | Upload Foto | Foto ruang tamu (harus mencakup dinding dan lantai) | [{"filename": "b00cf5df-c3f6-42d6-96a0-3b5aa6a6fcf9__foto... |

---

## 📁 KETERANGAN PEMBERI JAWABAN

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `nama_info_list` | Pilihan Dropdown | Nama Pemberi Informasi | [{"no_urut": 1, "label": "RIKADIUS HANDOKO", "value": 1, ... |
| 2 | `nama_info` | Angka/Tersembunyi | nama_info_cawi |  |
| 3 | `ak_info` | Angka/Tersembunyi | ak_info | [{"no_urut": 1, "label": "RIKADIUS HANDOKO", "value": 1, ... |
| 4 | `nama_lain` | Pilihan Dropdown | Nama Lain |  |
| 5 | `telp_info` | Pilihan Dropdown | Nomor HP/Telepon | 081254912301 |
| 6 | `email_info` | Pilihan Dropdown | E-mail |  |
| 7 | `tanda_info` | Tanda Tangan | Tanda Tangan | [{"signature": [{"compositeOperation": "source-over", "ve... |

---

## 📁 CATATAN

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `catatan` | Isian Teks Panjang | Catatan |  |
| 2 | `idsbr_keluarga` | Angka/Tersembunyi | ID SBR keluarga |  |
| 3 | `idsbr_match` | Angka/Tersembunyi | ID SBR Match | None |
| 4 | `id_l1_umkm` | Angka/Tersembunyi | New Question |  |
| 5 | `id_l2_umkm` | Angka/Tersembunyi | New Question |  |
| 6 | `id_keluarga` | Angka/Tersembunyi | New Question | 6104020608140004 |
| 7 | `id_regsosek` | Angka/Tersembunyi | New Question |  |
| 8 | `waktu_selesai` | Waktu (Datetime) | Waktu Selesai | 2026-06-20T13:43:15 |
| 9 | `daftar_anomali` | Angka/Tersembunyi | daftar_anomali |  |

---

## 📁 ANOMALI

| No | Variabel | Tipe Input | Pertanyaan / Keterangan | Contoh Isian |
|:--:|----------|:----------:|------------------------|-------------|
| 1 | `custom_script_table` | Angka/Tersembunyi | custom_script_table |  |
| 2 | `tanggal_anomali` | Angka/Tersembunyi | tanggal_anomali |  |
| 3 | `tanggal_selesai_anomali` | Angka/Tersembunyi | tanggal_selesai_anomali |  |
| 4 | `anomali_1_check` | Slider/Angka | Apakah data di atas sesuai kondisi lapangan? |  |
| 5 | `anomali_1_penjelasan` | Isian Teks Panjang | Penjelasan Anomali 1 |  |
| 6 | `anomali_2_check` | Slider/Angka | Apakah data di atas sesuai kondisi lapangan? |  |
| 7 | `anomali_2_penjelasan` | Isian Teks Panjang | Penjelasan Anomali 2 |  |
| 8 | `anomali_3_check` | Slider/Angka | Apakah data di atas sesuai kondisi lapangan? |  |
| 9 | `anomali_3_penjelasan` | Isian Teks Panjang | Penjelasan Anomali 3 |  |
| 10 | `anomali_4_check` | Slider/Angka | Apakah data di atas sesuai kondisi lapangan? |  |
| 11 | `anomali_4_penjelasan` | Isian Teks Panjang | Penjelasan Anomali 4 |  |
| 12 | `anomali_5_check` | Slider/Angka | Apakah data di atas sesuai kondisi lapangan? |  |
| 13 | `anomali_5_penjelasan` | Isian Teks Panjang | Penjelasan Anomali 5 |  |
| 14 | `anomali_6_check` | Slider/Angka | Apakah data di atas sesuai kondisi lapangan? |  |
| 15 | `anomali_6_penjelasan` | Isian Teks Panjang | Penjelasan Anomali 6 |  |
| 16 | `anomali_7_check` | Slider/Angka | Apakah data di atas sesuai kondisi lapangan? |  |
| 17 | `anomali_7_penjelasan` | Isian Teks Panjang | Penjelasan Anomali 7 |  |


---
*Dokumen ini diekstrak otomatis dari API Template Designer FASIH BPS.*
