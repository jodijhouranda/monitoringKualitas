# Struktur Kuesioner FASIH
Berikut adalah susunan pertanyaan berdasarkan urutan asli (termasuk sidebar/blok) pada aplikasi pengisian:

## PENGANTAR

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `pengantar` | `3` | SENSUS EKONOMI 2026
    
    
        PENDATAAN LENGKAP USAHA/PERUSAHAAN |
| `keterangan` | `3` | PENGANTAR

    
        
            Tujuan
            SE2026 bertujuan untuk menyediakan data dasar yang terpercaya untuk seluruh kegiatan ekonomi.
        

        

        
            Dasar Hukum
            
                
                    Undang-Undang No. 16 Tahun 1997 tentang Statistik.
                
                
                    Peraturan Pemerintah RI No. 51 Tahun 1999 tentang Penyelenggaraan Statistik.
                
            
        

        

        
            Kerahasiaan
            Kerahasiaan data yang diberikan dijamin oleh Undang-Undang No. 16 Tahun 1997 pasal 21.
        

        

        
            Layanan Informasi
            Untuk bantuan pengisian daftar isian, dapat menghubungi Sekretariat Sensus Ekonomi Tahun 2026 - Badan Pusat Statistik
            
            Email: halose2026@bps.go.id
        
    

    
        Pendataan ini tidak ada hubungannya dengan pajak dan tidak dipungut biaya apapun. |
| `mulai` | `35` | Waktu Mulai |
| `cawi_identifier` | `4` | cawi_identifier |
| `is_cawi` | `4` | is_cawi |
| `is_from_cawi` | `4` | is_from_cawi |
| `kunjungan_1` | `35` | Waktu Kunjungan I |
| `catatan_1` | `30` | Catatan Kunjungan I |
| `kunjungan_2` | `35` | Waktu Kunjungan II |
| `catatan_2` | `30` | Catatan Kunjungan II |
| `kunjungan_3` | `35` | Waktu Kunjungan III |
| `alasan_nr` | `26` | Alasan Nonrespon |
| `catatan_3` | `30` | Catatan Kunjungan III |
| `kunjungan_pml` | `35` | Waktu Kunjungan PML |
| `geotag_pml` | `33` | Geotaging oleh PML |
| `catatan_pml` | `30` | Catatan Kunjungan PML |
| `ec_mulai` | `4` | New Question |
| `mode` | `4` | Mode |
| `nama_principal` | `4` | Nama Keluarga/Bangunan/Usaha untuk principal |

## IDENTITAS WILAYAH

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `b1_head` | `3` | BLOK I. IDENTITAS WILAYAH |
| `prov` | `25` | 1. Provinsi |
| `kab` | `25` | 2. Kabupaten/Kota |
| `kec` | `25` | 3. Kecamatan |
| `desa` | `25` | 4. Desa/Kelurahan |
| `ubah_wilayah` | `26` | Apakah Terdapat Perubahan Wilayah? |
| `kab_baru` | `27` | 2. Kabupaten/Kota |
| `kec_baru` | `27` | 3. Kecamatan |
| `desa_baru` | `27` | 4. Desa/Kelurahan |
| `kode_prov` | `4` | kode_prov |
| `prov_kab` | `4` | prov_kab |
| `klas_desa` | `25` | 5. Klasifikasi Desa/Kelurahan |
| `kode_sls` | `25` | 6. Kode SLS/Non-SLS/Sub-SLS |
| `nama_sls` | `25` | 7. Nama SLS/Non-SLS |
| `ubah_sls` | `26` | 8. Apakah mengalami perubahan SLS (pemekaran/penggabungan/perubahan nama?) |
| `sudah` | `4` | sudah |
| `nama_sls_lap` | `25` | 9. Nama SLS/Non-SLS Lapangan |
| `tahun_survei` | `4` | Tahun Survei |
| `kodepos` | `25` | 10. Kodepos |
| `has_kodepos` | `4` | has_kodepos |
| `has_ubah_sls` | `4` | has_ubah_sls |
| `tahun_lalu` | `4` | Tahun survei minus 1 |
| `var_desa` | `4` | New Question |

## SE2026 - P

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `b5_head` | `3` | KETERANGAN KELUARGA DAN USAHA |
| `banner_id_sbr_match` | `3` | ⚠️ Usaha ini sudah digunakan pada usaha keluarga $nama |
| `is_keluarga` | `4` | Flag keluarga yang  berasal dari prelist
Terisi 1 Jika merupakan prelist keluarga |
| `nik_anggta_lain_prelist` | `4` | nik_anggta_lain_prelist |
| `is_usaha` | `4` | Flag usaha yang  berasal dari prelist
Terisi 1 Jika merupakan prelist usaha/ umkm |
| `is_prelist` | `4` | Flag prelist yang diisikan pada proses pembuatan prelist
Terisi 1 jika merupakan prelist |
| `set_is_prelist` | `4` | set_is_prelist |
| `ec_non_keluarga` | `4` | Enabling Untuk Rincian Bangunan/Usaha Lainnya mencakup :
Usaha prelist, Bangunan Lainnya ditemukan dan Usaha/ Bangunan Baru |
| `ket_editable` | `4` | Keterangan/Catatan Kaki untuk predefined editable |
| `ub_prelist` | `4` | Status UB Prelist |
| `ub` | `4` | Status UB umkm |
| `jenis_prelist` | `4` | Jenis Prelist |
| `flag_pbi` | `4` | PBI |
| `is_new` | `26` | Tambah :
Pilih jenis assignment yang akan ditambahkan |
| `pilih_umkm` | `27` | Daftar Usaha Non Prelist
Pilih "Tidak Ditemukan"  jika nama usaha tidak ada di daftar usaha |
| `no_kk_prelist` | `4` | Nomor KK prelist untuk pembanding |
| `nik_prelist` | `4` | NIK prelist untuk pembanding |
| `nama_lookup_umkm` | `4` | Nama dari Lookup |
| `nama_usaha_bang` | `25` | Nama Bangunan/ Usaha/ Perusahaan
$ket |
| `set_nama_usaha_bang` | `4` | set_nama_usaha_bang |
| `no_kk` | `25` | Nomor KK
$ket |
| `alsan_tidak_kk` | `4` | Alasan Kode KK tidak dapat diberikan: |
| `nik` | `25` | NIK
$ket |
| `nama_kk` | `25` | Nama Kepala Keluarga (KK)
$ket |
| `banner_pemadanan_nik` | `3` | Silakan lakukan pengecekan NIK dengan menekan tombol CEK NIK di bawah ini. |
| `callnik_button_p` | `6` | CEK NIK |
| `hasilPemadananNIK_p` | `4` | Hasil Pengecekkan NIK |
| `htmlHasilPemadananNIK2_p` | `4` | Hasil Pengecekan NIK |
| `htmlHasilPemadananNIK_p` | `4` | ‎ Hasil Pengecekan NIK |
| `result_callnik_p` | `4` | ‎ |
| `nama_ak_lain` | `25` | Nama Anggota Keluarga Lainnya
$ket |
| `alamat_lookup_umkm` | `4` | Alamat dari lookup |
| `alamat_klrg` | `4` | Alamat
$ket |
| `jumlah_usaha_prelist` | `25` | Jumlah Usaha yang Dimiliki Seluruh Anggota Keluarga  (Sumber: UMKM dan ST2023) |
| `kode_keberedaan_keluarga` | `4` | Pilihan kode keberadaan keluarga |
| `kode_keluarga_new` | `4` | Pilihan Keberadaan Keluarga (new) |
| `kode_bangunan_new` | `4` | Pilihan Keberadaan Bangunan (new) |
| `ada_keluarga` | `26` | Keberadaan Keluarga |
| `ada_bang_usaha` | `26` | Keberadaan Bangunan Lainnya/ Usaha |
| `set_ada_bang_usaha` | `4` | set_ada_bang_usaha |
| `alamat_prelist` | `30` | Alamat  (Prelist) |
| `domisili` | `26` | Apakah alamat tersebut sesuai dengan alamat pada Kartu Keluarga? |
| `alamat_domisili` | `3` | Alamat |
| `jalan_domisili` | `30` | Nama Jalan/Gang/Komplek/Gedung/dll (Tuliskan dengan rinci) |
| `nomor_domisili` | `25` | Blok/Nomor Rumah
(Jika tidak ada nomor rumah, tulis strip (-)) |
| `ec_keluarga` | `4` | Enabling Untuk Rincian Keluarga mencakup :
Keluarga prelist ditemukan dan Keluarga Baru |
| `no_keluarga_terbesar` | `4` | NOMOR URUT KELUARGA TERBESAR: |
| `no_keluarga` | `28` | Nomor Urut Keluarga |
| `no_bangunan_terbesar` | `4` | NOMOR URUT BANGUNAN TERBESAR: |
| `no_bang` | `28` | Nomor Urut Bangunan |
| `kode_bang` | `26` | Kode Penggunaan Bangunan |
| `pilihan_kode_bang` | `4` | Options untuk kode_bang disesuaikan |
| `geotag` | `33` | Geotagging |
| `foto_depan_p` | `32` | Foto tampak depan (harus mencakup atap dan dinding) |
| `jumlah_ak_kk` | `28` | Jumlah Anggota Keluarga Berdasarkan Kartu Keluarga |
| `jumlah_ak` | `25` | Jumlah Anggota Keluarga Yang menetap di dalam bangunan tempat tinggal minimal 1 tahun, atau kurang dari 1 tahun dan berniat menetap |
| `usaha_kos` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK memiliki usaha penyewaan lahan atau kontrakan atau kos kosan? |
| `usaha_keliling` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK memiliki usaha keliling (pedagang sayur keliling, ojek keliling, tukang becak keliling, supir |
| `usaha_online` | `26` | Apakah $namaKK  atau anggota keluarga dari $namaKK  memiliki usaha online contoh: menjual barang melalui tokopedia/ shopee/website/ instagram tanpa memiliki toko? |
| `usaha_bongkar` | `26` | Apakah $namaKK  atau anggota keluarga dari $namaKK   memiliki usaha di luar tempat tinggal, yang lokasi usahanya tetap tetapi peralatan/ perlengkapan usahanya dipindah/ dibawa pulang/ dibongkar pasang (misal: usaha kaki lima/ tenda seafood yang jika sudah tutup semua peralatan akan dibawa pulang, usaha dagang martabak gerobakan yang mangkal di pinggir jalan namun jika sudah selesai gerobak akan dibawa pulang, dan usaha lain yang sejenis) |
| `usaha_konstruksi` | `26` | Apakah  $namaKK atau anggota keluarga dari $namaKK memiliki usaha sebagai pemborong konstruksi/perusahaan konstruksi yang berlokasi di tempat tinggal ini atau penggalian perorangan? |
| `usaha_lain` | `26` | Apakah  $namaKK atau anggota keluarga dari $namaKK memiliki usaha lain? Seperti mengajar privat dari rumah ke rumah, Freelance, YouTuber, Konten Kreator, Afiliator, dan semua usaha lainnya yang dilakukan dalam bangunan ini? |
| `pertanian_head` | `3` | Identifikasi Usaha Pertanian yang Dilakukan Keluarga |
| `tanaman_pangan` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Tanaman Pangan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar?

termasuk yang seluruhnya dikonsumsi sendiri (padi, jagung, kedelai, kacang tanah, kacang hijau, ubi kayu, ubi jalar, talas, ganyong, dan palawija lainnya) |
| `hortikultura` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Hortikultura dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? |
| `perkebunan` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Perkebunan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? |
| `peternakan` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Peternakan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? |
| `kehutanan` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Kehutanan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? |
| `perikanan` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Perikanan dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? |
| `jasa_pertanian` | `26` | Apakah $namaKK atau anggota keluarga dari $namaKK selama setahun yang lalu mengelola usaha pertanian Jasa Pertanian dengan tujuan sebagian atau seluruh hasilnya untuk dijual/ditukar? |
| `jumlah_usaha_ditemukan` | `4` | Jumlah usaha yang ditemukan
Jumlah usaha akan terisi dengan meng-update keberadaan usaha |
| `daftar_nik_pengusaha` | `4` | daftar_nik_pengusaha |
| `usaha_gabung` | `4` | List yang ditampilkan di se2026_nested |
| `ec_ada_usaha` | `4` | Enabling Condition Keberadaan Usaha |
| `nama_usaha_prelist` | `4` | Nama Usaha Prelist |
| `list_individu_dtsen_prelist` | `4` | List Individu Prelist |
| `status_pegawai` | `4` | status_pegawai |
| `idsbr_all` | `4` | idsbr_all |
| `nib_all` | `4` | nib_all |
| `email_all` | `4` | email_all |
| `skala_usaha_all` | `4` | skala_usaha_all |
| `hidden_p` | `3` | ℹ️ Halaman ini tidak memerlukan pengisian karena tidak terdapat pertanyaan yang ditujukan kepada responden pada bagian ini. Silakan lanjutkan ke halaman berikutnya sesuai petunjuk yang tersedia. |
| `idunik_MSSD` | `4` | idunik_MSSD |
| `jumlah_usaha` | `4` | jumlah_usaha |
| `ya_pertanian` | `4` | Jumlah Usaha Pertanian |
| `ya_nonpertanian` | `4` | Jumlah Usaha Non-Pertanian |
| `ya_gabung` | `4` | jum usaha gabung |
| `skala_usaha_prelist` | `4` | skala_usaha_prelist |

## SE2026 - L BLOK I

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `ak_head` | `3` | KETERANGAN ANGGOTA KELUARGA |
| `set_nik_kk` | `4` | Set NIK KK |
| `label_usaha` | `4` | Label Usaha |
| `prelist_dtsen` | `4` | Nama anggota keluarga |
| `info_tambah_ak` | `3` | Format Penulisan Anggota Keluarga Baru:
     Klik "+ Tambah Baru" untuk menambahkan anggota keluarga baru
     Nama Anggota Keluarga hanya boleh terisi karakter: A-Z, a-z, spasi. |
| `tambah_dtsen` | `21` | Nama anggota keluarga |
| `gabung_dtsen` | `4` | gabung_dtsen |
| `art_pengusaha` | `4` | art_pengusaha |
| `art_keberadaan15` | `4` | art yg keberadaan kode 1 dan 5 |
| `cek1` | `4` | cek jum art 15 |
| `jk_krt` | `4` | jk_krt |
| `umur_krt` | `4` | umur krt |
| `jum_anakmantucucu` | `4` | Jumlah anak mantu cucu |
| `jum_pasangan` | `4` | Jumlah pasangan suami / istri |
| `jum_art_semua` | `4` | jum_art_semua |
| `jum_art_1345` | `4` | jum_art_1345 |
| `jum_art_1345_umurkur10` | `4` | jum_art_1345_umurkur10 |
| `jum_kk_lebihdr10th` | `4` | jum_kk_lebihdr10th |
| `jum_kk` | `4` | jum_kk |
| `nested_dtsen_instruction_2` | `3` | 🔍 Untuk melanjutkan pengisian Blok Keterangan Anggota Keluarga, silakan klik tombol Lihat pada bagian di bawah ini. |
| `nested_dtsen` | `2` | Keterangan Anggota Keluarga |
| `head_ak` | `3` | KETERANGAN ANGGOTA KELUARGA |
| `isprelistart` | `4` | Apakah prelist art |
| `no_urut_kk` | `4` | 5. Nomor urut anggota keluarga |
| `nama_dtsen` | `4` | 6. Nama anggota keluarga |
| `nik_dtsen` | `25` | 7. Nomor Induk Kependudukan (NIK) $NAME$

(Tulis sesuai yang tercantum di KK atau KTP paling mutakhir) |
| `set_nik_dtsen_prelist` | `4` | set_nik_dtsen_prelist |
| `nik_dtsen_prelist` | `4` | nik_dtsen_prelist |
| `banner_cek_nik_2` | `3` | Silakan lakukan pengecekan NIK dengan menekan tombol CEK NIK di bawah ini. |
| `callnik_button` | `6` | CEK NIK |
| `hasilPemadananNIK` | `4` | Hasil Pengecekkan NIK |
| `htmlHasilPemadananNIK2` | `4` | . |
| `htmlHasilPemadananNIK` | `4` | Hasil Pengecekan NIK |
| `result_callnik` | `4` | . |
| `ec_anggota_keluarga` | `4` | Enabling anggota keluarga |
| `hubungan` | `26` | 8. Hubungan $NAME$ dengan Kepala Keluarga |
| `keberadaan_dtsen` | `26` | 9. a. Keberadaan anggota keluarga |
| `alamat_dn` | `26` | 9. b. Alamat domisili: |
| `domisili_dn` | `3` | 10DN. Domisili Dalam Negeri |
| `prov_dn` | `27` | a. Provinsi |
| `kab_dn` | `27` | b. Kabupaten/Kota |
| `domisili_ln` | `27` | 10LN.  Negara domisili Individu (luar negeri) |
| `status_kawin` | `26` | 11. Apakah status perkawinan $NAME$ |
| `set_jk_prelist` | `4` | set_jk_prelist |
| `jk_prelist` | `4` | jk_prelist |
| `jk_dtsen` | `26` | 12. Jenis Kelamin $NAME$ |
| `tgl_bln_thn_lahir` | `3` | 13. a. Tanggal Lahir $NAME$ |
| `tgl_lahir` | `25` | Tanggal Lahir |
| `bln_lahir` | `27` | Bulan Lahir |
| `thn_lahir` | `24` | Tahun Lahir |
| `set_umur_ak` | `4` | set_umur_ak |
| `umur_ak` | `28` | 13. b. Umur $NAME$ |
| `art_ada_usaha` | `26` | Apakah $NAME$ memiliki usaha berikut? 

$daftar_usaha |

## SE2026 - L BLOK II

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `header_l` | `3` | SE2026-L
    
        Blok terkait Pendataan Variabel Usaha, hanya ditanyakan ketika keluarga memiliki usaha atau bangunan usaha |
| `info_tambah` | `3` | Silakan klik + Tambah Baru untuk menambahkan usaha keluarga |
| `nama_usaha_tambahan` | `21` | Nama Usaha Tambahan |
| `se2026_nested_instruction` | `3` | 🔍 Untuk melanjutkan pengisian Blok Keterangan Usaha/Perusahaan, silakan klik tombol Lihat pada bagian di bawah ini. |
| `se2026_nested` | `2` | Keterangan Usaha/Perusahaan |
| `head_l` | `3` | SE2026-L
  
  Blok terkait Pendataan Variabel Usaha, hanya ditanyakan ketika keluarga memiliki usaha atau bangunan usaha |
| `b1` | `3` | BLOK II : IDENTITAS USAHA/PERUSAHAAN |
| `pilih_umkm_options` | `4` | Opsi Pilih UMKM dalam satu SLS yang sama |
| `pilih_umkm_sls` | `27` | Pilih UMKM dalam satu SLS yang sama |
| `prov_l` | `4` | 1. Provinsi |
| `kab_l` | `4` | 2. Kabupaten/Kota |
| `kec_l` | `4` | 3. Kecamatan |
| `desa_l` | `4` | 4. Kelurahan/Desa/Nagari |
| `sls_info` | `3` | 5. Nama dan Nomor SLS/Sub-SLS |
| `kodesls_l` | `4` | Kode SLS/Sub-SLS |
| `sls_l` | `4` | Nama SLS/Sub-SLS |
| `no_bang_l` | `4` | 6. Nomor Bangunan |
| `no_usaha` | `4` | 7. Nomor Urut Usaha/Perusahaan |
| `ec_mulai_L` | `4` | New Question |
| `head_nama_usaha` | `3` | 8. Nama dan Alamat Usaha/Perusahaan |
| `nama_usaha` | `4` | 8. a. Nama usaha/perusahaan |
| `keberadaan_usaha` | `26` | Keberadaan Usaha |
| `set_keberadaan_usaha` | `4` | set_keberadaan_usaha |
| `nama_usaha_edit` | `25` | 8. a. Nama usaha/perusahaan
Tulis perbaikan nama usaha, jika tidak ada perubahan tulis  ulang nama usaha/perusahaan |
| `skala_usaha` | `4` | skala_usaha |
| `is_prelist2` | `4` | Is_Prelist2 |
| `id_pmss` | `4` | id_pmss |
| `idsbr` | `4` | ID SBR |
| `kode_keberadaan_usaha` | `4` | Pilihan untuk keberadaan Usaha |
| `nama_komersial` | `25` | 8. b. Nama komersial usaha/perusahaan

Jika tidak memiliki nama komersial, maka tuliskan nama usaha/perusahaan. |
| `alamat_usaha_view` | `30` | 8.c. Alamat usaha/perusahaan |
| `alamat_usaha_var` | `4` | 8. c. Alamat usaha/perusahaan |
| `alamat_usaha` | `4` | alamat_usaha |
| `tampilan_alamat` | `3` | Petunjuk Rincian 8c. Alamat usaha/perusahaan
    
    
        
            <!--
            <!--    
            <!--        Termasuk:
            <!--        Tidak termasuk:
            <!--    
            <!--
            
                
                    
                        
                            Khusus usaha: 
                            1) di dalam bangunan tempat tinggal (contoh: usaha online , catering , les privat, dsb, yang dilakukan di tempat tinggal); 
                            2) keliling; 
                            3) usaha di luar bangunan tempat tinggal dengan lokasi tetap dan perlengkapan usaha dipindah/dibongkar pasang;
4) konstruksi perorangan, pertambangan dan penggalian perorangan; 
5) persewaan rumah/kamar/kantor;
→ yang dicatat adalah alamat tempat tinggal pemilik usaha. |
| `kp_nested` | `2` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Daftar Kantor Cabang |
| `kp_head` | `3` | KETERANGAN KANTOR CABANG/UNIT DI BAWAH KENDALI KANTOR PUSAT |
| `kp_ket` | `3` | Lengkapi informasi kantor pusat dan kantor cabang/unit di bawah kendali kantor pusat |
| `kp_unit` | `25` | Nama Kantor/
Unit |
| `kp_jenis` | `26` | Jenis Unit |
| `kp_prov` | `27` | Provinsi |
| `kp_kab` | `27` | Kabupaten |
| `kp_produksi_lingkungan` | `26` | Apakah perusahaan ini memproduksi barang/jasa yang ramah lingkungan? |
| `kp_perlindungan_lingkungan` | `26` | Apakah perusahaan ini mengeluarkan biaya perlindungan lingkungan dan/atau pembelian barang dan jasa yang ramah lingkungan |
| `kp_tk` | `28` | Tenaga Kerja (per 31 Desember 2025) (orang) |
| `kp_total_pengeluaran` | `20` | Pengeluaran Tahun 2025 (Rupiah) |
| `kp_total_pendapatan` | `20` | Pendapatan Tahun 2025 (Rupiah) |
| `rt` | `25` | RT |
| `rw` | `25` | RW |
| `kode_pos` | `4` | Kode Pos |
| `head_telp` | `3` | Nomor Telepon |
| `kode_area` | `25` | Kode Area |
| `no_telp` | `25` | Nomor Telepon |
| `eks` | `25` | Ekstensi |
| `email` | `25` | Email |
| `hp` | `25` | Nomor HP/whatsapp: |
| `website` | `25` | Homepage/website

Alamat website diawali dengan www. Contoh : www.bps.go.id |
| `jenis_kawasan` | `26` | 8. d. Jenis kawasan beroperasi |
| `nama_kek_ki` | `27` | 8. e. Nama KEK/KI |
| `nama_kawasan` | `25` | 8. e. Nama kawasan


Contoh: KEK Mandalika, Kawasan Industri Jababeka, Stasiun Gambir, Bandara Soekarno-Hatta, Pelabuhan Tanjung Priok, Terminal Pulo Gebang, Rest Area KM 57 Tol Jakarta–Cikampek, Sentra Batik Laweyan, Kompleks Pertokoan ITC Mangga Dua |
| `ec_usaha_respons` | `4` | Enabling Condition Usaha Respons di Roster |
| `info_usaha_campuran` | `3` | Khusus usaha/perusahaan di bangunan campuran atau yang dicatat di tempat tinggal. |
| `jenis_usaha` | `26` | 9. a. Apa jenis usaha/perusahaan ini? |
| `head_lokasi` | `3` | 9. b. Lokasi usaha utama |
| `alamat_usaha_utama` | `30` | 9. b1. Alamat/lokasi usaha utama |
| `prov_usaha_utama` | `27` | 9. b2. Provinsi |
| `kab_usaha_utama` | `27` | 9. b3. Kabupaten/Kota |
| `punya_nib` | `26` | 10. a. Apakah memiliki Nomor Induk Berusaha (NIB)? |
| `nib` | `25` | 10. b. Tuliskan NIB: |
| `banner_cek_nib` | `3` | Silakan lakukan pengecekan NIB dengan menekan tombol CEK NIB di bawah ini. |
| `cek_nib` | `6` | CEK NIB |
| `hasilCekNIB` | `4` | ​ |
| `htmlHasilCekNIB` | `4` | Hasil Pengecekan NIB |
| `result_callnib` | `4` | result_callnib |
| `tidak_nib` | `26` | 10. c. Apa alasan utama tidak memiliki NIB? |
| `nib_lainnya` | `25` | 10. c. Lainnya, tuliskan.... |
| `badan_usaha` | `26` | 11. a. Apa status badan usaha dari usaha/perusahaan ini? |
| `koperasi_kdkmp` | `26` | 11. b. Apakah koperasi ini merupakan Koperasi Desa/Kelurahan Merah Putih (KDKMP)? |
| `jenis_koperasi` | `26` | 11. c. Apa jenis koperasi ini berdasarkan layanannya? |
| `lap_keuangan` | `26` | 11. d. Apakah mempunyai laporan/catatan keuangan? |
| `pengusaha_var_prelist` | `4` | pengusaha_var_prelist |
| `pengusaha_var` | `27` | 12. a. Nama Pengusaha / Penanggung Jawab |
| `set_pengusaha_var` | `4` | set_pengusaha_var |
| `set_default_pengusaha_var` | `4` | set_default_pengusaha_var |
| `pengusaha` | `25` | 12. a. Nama Pengusaha / Penanggung Jawab |
| `jk_var` | `4` | 12. b. Jenis Kelamin |
| `jk` | `26` | 12. b. Jenis Kelamin |
| `umur_pj_var` | `4` | 12. c. Umur |
| `umur` | `28` | 12. c. Umur |
| `nik_pengusaha_var` | `4` | 12. d. Nomor Induk Kependudukan (NIK ) |
| `nik_pengusaha` | `25` | 12. d. Nomor Induk Kependudukan (NIK) |
| `banner_pemadanan_nik_2` | `3` | Silakan lakukan pengecekan NIK dengan menekan tombol CEK NIK di bawah ini. |
| `callnik_button_l` | `6` | CEK NIK |
| `hasilPemadananNIK_l` | `4` | Hasil Pengecekkan NIK |
| `htmlHasilPemadananNIK2_l` | `4` | ​ |
| `htmlHasilPemadananNIK_l` | `4` | Hasil Pengecekan NIK |
| `result_callnik_l` | `4` | ​ |
| `head_keg_utama` | `3` | 13. Kegiatan utama dan produk utama usaha/perusahaan: |
| `keg_utama` | `25` | 13. a. Apa kegiatan utama usaha/perusahaan ini? Tuliskan selengkapnya |
| `kegutama_detail` | `3` | Petunjuk Rincian 13a. Kegiatan Utama
    
    
        
            <!--
            <!--    
            <!--        Termasuk:
            <!--        Tidak termasuk:
            <!--    
            <!--
            
                
                    
                        
                            Contoh: 
                            o membudidayakan tanaman padi;
                            o membudidayakan cabai;
                            o membudidayakan tanaman tembakau;
                            o membudidayakan udang di air payau;
                            o membibitkan ayam ras;
                            o menangkap ikan konsumsi di sungai;
                            o memungut madu di hutan;
                            o menggiling daging ikan menjadi sosis dan dijual di rumah/online; 
                            o membuat kebab di rumah dan dititipkan di warung; 
                            o jasa borongan/konstruksi rumah; 
                            o menjual mobil bekas di showroom; 
                            o menjual kaset video game yang dibeli dari pihak lain di marketplace; 
                            o angkutan bus antarkota antarprovinsi; 
                            o membuat sosis dari ikan, disajikan dengan pembakaran, dijual di depan rumah/online; 
                            o menyewakan kos bulanan;
o menyewakan kamar hotel bintang 5; 
o membuat kebab berdasarkan pesanan langsung di gerobak depan alfamart; 
o menjual perangkat lunak video gim yang dikembangkan sendiri; 
o penyediaan telekomunikasi internet tanpa kabel; 
o membuat rumah kemudian dipasarkan sendiri;
o menyewakan rumah dengan periode tahunan; 
o membuat desain kemasan botol minuman; 
o sekolah menengah pertama negeri; 
o rumah sakit pemerintah; 
o membuat seni lukisan yang dipajang untuk dijual; 
o membuat kunci duplikat di pinggir jalan; 
o menulis cerpen; 
o membuat desain interior rumah; 
o pengembangan aplikasi video gim; 
o meracik jamu secara langsung untuk siap konsumsi di sebuah kedai |
| `jenis_kegiatan` | `4` | jenis_kegiatan |
| `usaha_info` | `3` | 13. b. Pilih yang paling sesuai dengan kegiatan utama usaha/perusahaan ini: |
| `produk_sendiri` | `26` | 13. b1. Apakah memproduksi barang di lokasi ini? |
| `layanan_mamin` | `26` | 13. b2. Apakah menyediakan layanan makan minum?

Ciri: terdapat kegiatan peracikkan, pemanasan ulang, atau pembuatan produk berdasarkan pesanan/permintaan pelanggan |
| `keg_penjualan` | `26` | 13. b3. Apakah melakukan penjualan barang? |
| `keg_jasa` | `26` | 13. b4. Pilih salah satu aktivitas yang dilakukan: |
| `lokasi_usaha` | `26` | 13. c. Di mana usaha tersebut biasa dilakukan? |
| `input` | `30` | 13. d. Apa input yang digunakan?
Contoh: daging ikan, tepung; daging kebab, kulit kebab, sayuran; bambu; jagung pipil; kaca; kain; kulit sapi; kayu bulat; rotan; kunci polos |
| `proses` | `30` | 13. e. Bagaimana proses mengubah input tersebut menjadi produk output (beserta alatnya)?
Contoh: menggiling daging ikan menjadi sosis; membuat kebab di rumah dan sudah dikemasi kemudian dititipkan di warung; penggaraman; pengasapan; pemindangan; pembekuan. |
| `produk` | `25` | 13. f. Apa produk utama yang dihasilkan? |
| `tampilan_13f` | `3` | Petunjuk Rincian 13f. Produk utama
    
    
        
            <!--
            <!--    
            <!--        Termasuk:
            <!--        Tidak termasuk:
            <!--    
            <!--
            
                
                    
                        
                             Contoh: padi; tembakau; udang; ayam ras; ikan segar konsumsi; ayam ras; madu hutan; sosis; kebab yang sudah dikemas; jasa renovasi/ membuat rumah; jasa perdagangan mobil bekas; jasa perdagangan kaset video gim; jasa angkutan bus antarkota antarprovinsi; sosis ikan yang dibakar; jasa sewa kos bulanan; jasa penyediaan akomodasi hotel bintang 5;
jasa penyajian kebab; jasa pengembangan perangkat lunak video gim; jasa telekomunikasi internet tanpa kabel; jasa penjualan rumah yang
dibangun sendiri; jasa penyediaan rumah dengan periode tahunan; jasa pendidikan sekolah menengah pertama negeri; jasa kesehatan oleh
rumah sakit pemerintah; jasa pembuatan kunci duplikat; lukisan, patung, kerajinan, musik, tari, foto, film, ilustrasi, animasi, board game, puisi,
cerpen, novel, naskah drama; desain arsitektur, desain produk, desain interior, desain komunikasi visual, desain fesyen, pembuatan perangkat
lunak (software ), aplikasi digital, aplikasi gim, perangkat elektronik, inovasi berbasis kecerdasan buatan; rendang, gudeg; gamelan, angklung. |
| `info_genai` | `3` | Silahkan klik 
Dapatkan Rekomendasi KBLI
untuk mendapatkan kbli dan kategori rekomendasi 
dari GEN AI |
| `genai_button` | `6` | DAPATKAN REKOMENDASI KBLI |
| `var_kbli` | `4` | Pilihan untuk KBLI |
| `result_gen_ai` | `4` | Result Gen AI |
| `kbli_prelist` | `4` | kbli_prelist |
| `kbli_genai` | `26` | 13. g. Kode KBLI |
| `kbli` | `27` | Pilih dari Master KBLI |
| `kbli_genai_cawi` | `4` | kbli_genai_cawi |
| `kbli_cawi` | `4` | kbli_cawi |
| `set_kbli_cawi` | `4` | set_kbli_cawi |
| `kbli_akhir` | `4` | KBLI Akhir |
| `kategori_2025` | `4` | kategori_2025 |
| `kategori` | `4` | 13. h. Kategori Lapangan Usaha: |
| `kat_detail` | `3` | Petunjuk Rincian 13h. Kategori Lapangan Usaha
    

    
        
            
                
                    
                        

                            Petunjuk:

                            
                                
                                    KATEGORI KBLI 2025, yang berisikan list kategori usaha.
                                
                            
                            
                                
                                    Kategori A : Pertanian, Kehutanan, dan Perikanan
                                
                                
                                    Kategori B : Pertambangan dan Penggalian
                                
                                
                                    Kategori C : Industri
                                
                                
                                    Kategori D : Pengadaan Listrik, Gas, Uap/Air Panas dan Udara Dingin
                                
                                
                                    Kategori E : Penyediaan Air, Pengelolaan Air Limbah, Penanganan limbah, dan Remediasi
                                
                                
                                    Kategori F : Konstruksi
                                
                                
                                    Kategori G : Perdagangan Besar dan Eceran
                                
                                
                                    Kategori H : Transportasi dan Penyimpanan
                                
                                
                                    Kategori I : Aktivitas Penyediaan Akomodasi dan Makan Minum
                                
                                
                                    Kategori J : Aktivitas Penerbitan, Penyiaran, serta Produksi dan Distribusi Konten
                                
                                
                                    Kategori K : Aktivitas Telekomunikasi, Pemrograman Komputer, Konsultansi, Infrastruktur Komputasi, dan Jasa Informasi Lainnya
                                
                                
                                    Kategori L : Aktivitas Keuangan dan Asuransi
                                
                                
                                    Kategori M : Aktivitas Real Estat
                                
                                
                                    Kategori N : Aktivitas Profesional, Ilmiah dan Teknis
                                
                                
                                    Kategori O : Aktivitas Administratif dan Penunjang Usaha
                                
                                
                                    Kategori P : Administrasi Pemerintahan, Pertahanan dan Jaminan Sosial Wajib
                                
                                                                
                                    Kategori Q : Pendidikan
                                
                                
                                    Kategori R : Aktivitas Kesehatan Manusia dan Aktivitas Sosial
                                
                                
                                    Kategori S : Kesenian, Olahraga, dan Rekreasi
                                
                                
                                    Kategori T : Aktivitas Jasa Lainnya
                                
                                
                                    Kategori U : Aktivitas Rumah Tangga Sebagai Pemberi Kerja dan Aktivitas Produksi Barang dan Jasa
                                
                                  
                                    Kategori V : Aktivitas Badan Internasional dan Badan Ekstra Internasional Lainnya |
| `msg_error_kategori` | `4` | &nbsp |
| `html_msg_error` | `4` | Error: $ket |
| `cek_kbli_pml` | `26` | &nbsp;&nbsp;
Cek Kategori & KBLI  (Diisi oleh PML) |
| `var_hiden_pml` | `4` | New Question |
| `klasifikasi` | `26` | 13. i. Jika usaha/perusahaan merupakan akomodasi jangka pendek, apa klasifikasi usaha/perusahaan ini? |
| `jaringan` | `26` | 14. a. Apa jaringan usaha dari usaha/perusahaan ini? |
| `jumlah_kc` | `28` | 14. b. Berapa jumlah seluruh kantor cabang dan unit usaha yang berada di bawah kantor pusat? |
| `kp_header` | `3` | KHUSUS KANTOR PUSAT
    Apabila perusahaan ini merupakan kantor pusat, lanjutkan pengisian informasi kantor cabang dan
unit yang berada di bawah kendali kantor pusat melalui kuesioner SE2026-L.KP |
| `kc_info` | `3` | 15. Informasi Kantor Pusat: |
| `ec_usaha_lanjutan` | `4` | Enabling Condition untuk Usaha Ditemukan selain penunjang dan pusat |
| `nama_kp` | `25` | 15. a. Nama Kantor Pusat |
| `alamat_kp` | `30` | 15. b. Alamat Kantor Pusat |
| `email_kp` | `25` | 15. c. Email |
| `negara_kp` | `27` | 15. d. Negara |
| `prov_kp` | `27` | 15. e. Provinsi |
| `kab_kp` | `27` | 15. f. Kabupaten/Kota |
| `internet` | `26` | 16. a. Apakah usaha/perusahaan ini menggunakan internet dalam menjalankan usaha? |
| `internet_info` | `3` | 16. b. Tujuan penggunaan internet: |
| `internet_produksi` | `26` | 16. b2. Produksi barang/jasa |
| `internet_pesanan` | `26` | 16. b1. Menerima pesanan barang/jasa |
| `internet_distribusi` | `26` | 16. b3. Distribusi barang/jasa |
| `internet_beli` | `26` | 16. b4. Membeli bahan baku online |
| `internet_promosi` | `26` | 16. b5. Promosi |
| `internet_lainnya` | `26` | 16. b6. Lainnya |
| `digital` | `26` | 16. c. Apakah usaha/perusahaan ini memanfaatkan teknologi digital Aritifical Intelligence (AI), Internet of Things (IoT), big data, printer 3D, blockchain, atau cloud computing? |
| `produksi_lingkungan` | `26` | 17. a. Apakah usaha/perusahaan ini memproduksi barang/jasa yang ramah lingkungan?
Contoh: Produk efisiensi energi (lampu atau mesin hemat listrik); Energi terbarukan (panel surya, turbin angin, biogas);
Kendaraan ramah lingkungan (kendaraan listrik/ hybrid); Produk berbahan daur ulang (kertas/plastik daur ulang, kemasan 
ramah lingkungan); Jasa pengelolaan dan pembersihan limbah dan sampah (pengolahan sampah/ air limbah, daur ulang) |
| `perlindungan_lingkungan` | `26` | 17. b.  Apakah usaha/perusahaan ini menggunakan input untuk tujuan perlindungan lingkungan
dan/atau pembelian barang dan jasa yang ramah lingkungan?
Contoh: Pengeluaran untuk pengelolaan dan pembersihan limbah dan sampah, pengendalian polusi udara, perbaikan tanah/ air tanah, pengurangan kebisingan, pelestarian alam/keanekaragaman hayati, audit/ penilaian lingkungan |
| `produk_seni` | `26` | 18. Apakah usaha/perusahaan ini menggunakan produk karya seni, sastra, desain, teknologi atau warisan budaya, baik diproduksi sendiri maupun oleh pihak lain?



Contoh produk karya seni: lukisan, patung, kerajinan, musik, tari, foto, film, ilustrasi, animasi, board game, dll.
Contoh produk sastra: puisi, cerpen, novel, naskah drama, dll.
Contoh produk desain: arsitektur, desain produk, desain interior, desain komunikasi visual, desain fesyen, dll.
Contoh produk teknologi: perangkat lunak (software), aplikasi digital, aplikasi gim, perangkat elektronik, dll.
Contoh produk warisan budaya: makanan tradisional, peralatan tradisional, obat tradisional, dll. |
| `ec_halal` | `4` | ec_halal |
| `halal` | `26` | 19. a. Apakah usaha/perusahaan ini menghasilkan produk bersertifikat halal?

Rincian 19 hanya ditanyakan kepada kategori usaha/perusahaan khusus berdasarkan BPJPH. |
| `sudah_halal` | `28` | 19. b. Berapa jumlah varian produk yang sudah bersertifikat halal BPJPH? |
| `belum_halal` | `28` | 19. c. Berapa jumlah varian produk yang belum bersertifikat halal BPJPH? |
| `ec_bpom` | `4` | ec_bpom |
| `izin_edar` | `26` | 20. a. Apakah usaha/perusahaan ini memiliki izin edar?

Rincian 20 hanya ditanyakan kepada kategori usaha/perusahaan khusus berdasarkan BPOM. |
| `sudah_bpom` | `28` | 20. b. Berapa jumlah varian produk yang sudah memiliki izin edar BPOM? |
| `belum_bpom` | `28` | 20. c. Berapa jumlah varian produk yang belum memiliki izin edar BPOM? |
| `mitra_kdkmp` | `26` | 21. Apakah usaha/perusahaan ini bermitra dengan Koperasi Desa/Kelurahan Merah Putih (KDKMP)? |
| `peran_mbg` | `26` | 22. Apakah usaha/perusahaan ini terlibat dalam program Makan Bergizi Gratis (MBG)? |
| `transaksi_non_pddk` | `3` | 23. Apakah usaha/perusahaan melakukan penjualan/pembelian kepada bukan penduduk Indonesia selama periode 1 Mei 2024 s.d. 31 Agustus 2026? |
| `barang_non_pddk` | `26` | 23. a.  Penjualan dan/atau pembelian barang |
| `jasa_non_pddk` | `26` | 23. b. Penjualan jasa |
| `beli_jasa_non_pddk` | `26` | 23. c. Pembelian jasa |
| `tampilan_23` | `3` | Petunjuk Rincian 23. Penjualan/pembelian kepada bukan penduduk Indonesia
    
    
        
            <!--
            <!--    
            <!--        Termasuk:
            <!--        Tidak termasuk:
            <!--    
            <!--
            
                
                    
                        
                             Bukan penduduk adalah orang atau badan yang pusat kegiatan ekonominya berada di luar Indonesia. Contoh orang yaitu turis wisatawan
  mancanegara yang berwisata kurang dari 1 tahun. 
  Contoh badan yaitu usaha/perusahaan yang tidak terdaftar badan usahanya di Indonesia.
 Contoh kegiatan:
 o Ekspor barang: Pengrajin perak di Bali mengirimkan aksesori dan perhiasan ke pembeli di luar negeri.
 o Impor barang: Toko elektronik Indonesia mengimpor smartphone dari Tiongkok untuk dijual kembali.
o  Ekspor jasa: Konsultan Indonesia memberikan jasa pelatihan secara online ke perusahaan luar negeri; Hotel di Indonesia melayani
 tamu wisatawan mancanegara
 o Impor jasa: Usaha/perusahaan Indonesia berlangganan layanan digital berbayar dari perusahaan luar negeri (Canva, Microsoft 365,
Google Cloud, Adobe, ChatGPT, dll.); Perusahaan Indonesia menggunakan jasa Konsultan asing |
| `tk_header` | `3` | 24. Pekerja |
| `tampilan_24` | `3` | Petunjuk Rincian 24. Pekerja
    
    
        
            <!--
            <!--    
            <!--        Termasuk:
            <!--        Tidak termasuk:
            <!--    
            <!--
            
                
                    
                        
                              1. Jika beroperasi tahun 2026, isikan rata-rata pekerja per bulan di tahun 2026. 
                              2. Jika beroperasi sebelum tahun 2026:
a. isikan pekerja per 31 Desember 2025, atau
b. jika tidak tersedia, isikan rata-rata pekerja per bulan di tahun 2025. |
| `tk_laki` | `28` | 24. a1. Pekerja laki-laki |
| `tk_pr` | `28` | 24. b1. Pekerja perempuan |
| `total_tk_jk` | `28` | 24. c1. Total pekerja (a1+b1) |
| `total_tk_jk_var` | `4` | total_tk_jk_var |
| `cek_tk_jk_pml` | `26` | &nbsp;&nbsp;
Cek Pekerja (c1) (Diisi oleh PML) |
| `tk_dibayar` | `28` | 24. a2. Pekerja dibayar |
| `tk_tdk_dibayar` | `28` | 24. b2. Pekerja tidak dibayar |
| `total_tk_bayar` | `28` | 24. c2. Total pekerja (a2+b2) |
| `total_tk_bayar_var` | `4` | total_tk_bayar_var |
| `cek_tk_bayar_pml` | `26` | &nbsp;&nbsp;
Cek Pekerja (24. c2) (Diisi oleh PML) |
| `ec_usaha_bulan` | `4` | enabling condition pertanyaan 25 s.d 28 |
| `ec_usaha_tahun` | `4` | enabling condition pertanyaan 21s.d 24 |
| `tahun_operasi` | `24` | 25. Tahun berapa usaha/perusahaan ini mulai beroperasi secara komersial?
Tahun beroperasi komersial terdiri dari 4 angka. Contoh: 1990; 2025;dsb. |
| `head_pengeluaran` | `3` | PENGELUARAN, PENDAPATAN, DAN ASET TAHUN 2025
  
              [Rincian 26-29 hanya ditanyakan jika usaha/perusahaan beroperasi secara komersial SEBELUM tahun 2026] |
| `info_pengeluaran` | `3` | 26. Rincian Pengeluaran Tahun 2025 |
| `gaji` | `20` | 26. a. Total upah dan gaji, serta jaminan sosial pegawai |
| `biaya_produksi` | `20` | 26. b. Biaya produksi |
| `biaya_pembelian` | `20` | 26. c. Biaya pembelian barang yang terjual |
| `operasional` | `20` | 26. d. Biaya operasional (air, listrik, gas, internet, pulsa, pemeliharaan, biaya angkutan, dll.) |
| `non_operasional` | `20` | 26. e. Biaya non-operasional |
| `total_pengeluaran_var` | `4` | total_pengeluaran_var |
| `total_pengeluaran` | `20` | 26. f. Total pengeluaran (a+b+c+d+e) |
| `cek_output26f_pml` | `26` | &nbsp;&nbsp;
Cek Rincian Pengeluaran 2025 (Diisi oleh PML) |
| `tampilan_26` | `3` | Petunjuk Rincian 26. Pengeluaran
    

    
        
            
                
                    
                        

                            Petunjuk:

                            
                                a. Total upah dan gaji, serta jaminan sosial pegawai
                            

                            Termasuk:
                            
                                
                                    Upah dan gaji pegawai/karyawan yang telah dikeluarkan
                                    ringkasan pembayarannya (group certificate)
                                
                                
                                    Komisi, tips, dan bonus untuk pegawai/karyawan
                                
                                
                                    Pembayaran cuti tahunan dan jenis cuti lainnya
                                
                            

                            Tidak termasuk:
                            
                                Upah dan gaji yang dikapitalisasi
                                
                                    Pembayaran untuk konsultan dan kontraktor yang berusaha sendiri
                                    (bukan karyawan perusahaan) yang dibayarkan dengan komisi
                                
                            

                            
                                
                                    b. Biaya produksi (pemakaian bahan baku dan penolong)
                                
                            

                            Catatan:
                            
                                Mencakup seluruh nilai barang dan jasa yang digunakan sebagai
                                bahan baku dan biaya langsung dalam proses produksi barang dan jasa,
                                tidak termasuk aset tetap.
                            

                            
                                Pada usaha pertanian, ongkos/biaya yang dicatat adalah biaya dari
                                barang/jasa yang benar-benar dibeli/dibayarkan dan telah digunakan
                                (tidak termasuk yang disimpan, diberikan ke pihak lain, dan sebagainya).
                            

                            
                                Untuk usaha jasa, biaya produksi yang dimaksud meliputi biaya-biaya
                                yang dikeluarkan secara langsung untuk menghasilkan jasa.
                            

                            Contoh:

                            
                                Biaya produksi usaha tanaman pangan, hortikultura, perkebunan,
                                peternakan, kehutanan, dan perikanan meliputi benih, bibit, pupuk,
                                pestisida, vaksin, vitamin, obat-obatan, pakan, umpan, wadah,
                                tali, es, garam, konsumsi, awak kapal, dan lain-lain.
                            

                            
                                Biaya produksi jasa transportasi meliputi biaya bahan bakar.
                                Biaya produksi usaha perbankan meliputi beban bunga, provisi,
                                dan komisi. Biaya produksi usaha asuransi meliputi klaim asuransi.
                                Biaya produksi usaha sewa kos-kosan atau kontrakan meliputi
                                air bersih dan listrik yang ditanggung pemilik.
                            

                            
                                c. Biaya pembelian barang yang dijual
                            

                            
                                Mencakup seluruh nilai pembelian barang perdagangan yang terjual.
                                Contoh: nilai pembelian beras yang terjual, nilai pembelian tepung
                                yang terjual, dan sebagainya.
                            

                            
                                
                                    d. Biaya operasional (air, listrik, gas, internet, pulsa,
                                    pemeliharaan, biaya angkutan)
                                
                            

                            Catatan:

                            
                                Mencakup biaya-biaya yang tidak secara langsung terkait dalam
                                proses produksi seperti air, listrik, gas, pemeliharaan,
                                serta biaya angkutan.
                            

                            Termasuk:

                            
                                Pengeluaran listrik, bahan bakar, dan air
                                Pembelian bahan perkantoran umum
                                
                                    Pembelian komponen dan bahan bakar untuk kendaraan bermotor
                                
                                
                                    Pembayaran ke pihak lain untuk kargo, delivery,
                                    dan jasa angkutan
                                
                                
                                    Pembayaran sewa operasi (dengan atau tanpa operator)
                                
                                
                                    Biaya lisensi software komputer yang berumur kurang dari
                                    satu tahun (termasuk biaya instalasi oleh provider eksternal)
                                
                                Biaya bank selain bunga
                            

                            Tidak termasuk:

                            
                                Pemeliharaan besar
                            

                            
                                e. Biaya non-operasional
                            

                            Catatan:

                            
                                Mencakup biaya bunga, biaya pajak, biaya administrasi,
                                biaya hukum, biaya donasi, biaya restrukturisasi,
                                biaya kerugian di awal, dan biaya lain-lain yang tidak terkait
                                dengan kegiatan operasional, seperti biaya perjalanan yang
                                tidak terkait dengan bisnis. |
| `info_pendapatan` | `3` | 27. Rincian Nilai $narasi Tahun 2025 |
| `var_narasi` | `4` | Narasi Pendapatan |
| `nilai_pendapatan` | `20` | 27. a. Nilai $narasi barang dan jasa |
| `pendapatan_lain` | `20` | 27. b. Pendapatan lainnya yang dihasilkan perusahaan |
| `total_pendapatan` | `20` | 27. c. Total nilai $narasi (a+b) |
| `total_pendapatan_var` | `4` | total_pendapatan_var |
| `cek_input27c_pml` | `26` | &nbsp;&nbsp;
Cek Rincian Pendapatan 2025 (Diisi oleh PML) |
| `pendapatan_online` | `28` | 27. d. Berapa persentase pendapatan yang dilakukan secara online ? |
| `tampilan_27` | `3` | Petunjuk Rincian 27. Produksi/Penjualan/Pendapatan
    

    
        
            
                
                    
                        

                            Petunjuk:

                            
                                
                                    a. Nilai produksi/penjualan/pendapatan barang dan jasa
                                
                            

                            Termasuk:

                            
                                
                                    Barang yang dijual baik yang diproduksi sendiri maupun tidak
                                
                                
                                    Penjualan ekspor (FOB - Free On Board)
                                
                                
                                    Penjualan atau transfer ke rekan bisnis/organisasi atau cabang di luar negeri
                                
                                
                                    Pendapatan yang diperoleh dari pengangkutan barang yang tidak dijual perusahaan
                                
                                
                                    Pendapatan jasa perbaikan dan layanan
                                
                                
                                    Pendapatan dari kontrak, subkontrak, dan komisi
                                
                                
                                    Pendapatan manajemen dari perusahaan/organisasi terkait maupun tidak
                                
                                
                                    Pendapatan dari jasa pemasangan
                                
                                
                                    Pendapatan dari jasa berlangganan dan keanggotaan
                                
                                
                                    Pendapatan dari jasa iklan
                                
                                
                                    Pendapatan royalti (hak cipta, hak paten, waralaba, dan lain-lain)
                                
                                
                                    Pendapatan dari sewa operasi
                                
                                
                                    Pendapatan bunga (khusus jasa keuangan)
                                
                            

                            Tidak termasuk:

                            
                                Penjualan aset
                                
                                    Royalti dari penggunaan lahan di bawah pengaturan sewa mineral
                                
                            

                            Catatan:

                            
                                Pada usaha pertanian, nilai produksi yang dicatat yaitu nilai produksi
                                yang dipanen, dikonsumsi sendiri (termasuk yang digunakan untuk bibit),
                                diolah sendiri, dijual, disimpan, digunakan sebagai upah/gaji pekerja,
                                diberikan kepada pihak lain, hilang, pertambahan bobot ternak,
                                serta nilai pembesaran tanaman kehutanan selama periode tahun 2025
                                sesuai dengan jenis dan satuan produksi pada masing-masing subsektor
                                yang diusahakan.
                            

                            
                                Nilai produksi yang dicakup termasuk nilai produksi ikutan yang dijual.
                            

                            
                                b. Pendapatan lainnya yang dihasilkan
                            

                            Termasuk:

                            
                                Sewa/royalti sumber daya alam
                                Pendapatan bunga
                                Pendapatan dividen
                                
                                    Pendanaan dari Pemerintah (subsidi, skema magang, dan pelatihan)
                                
                                Donasi
                            

                            Tidak termasuk:

                            
                                
                                    Pendanaan yang disediakan khusus untuk barang modal tertentu |
| `aset_usaha_thn` | `20` | 28. a. Nilai aset tanah dan bangunan pada 31 Desember 2025 |
| `aset_lain_thn` | `20` | 28. b. Nilai aset selain tanah dan bangunan pada 31 Desember 2025 |
| `total_aset_thn` | `20` | 28. c. Nilai total aset pada 31 Desember 2025 |
| `total_aset_thn_var` | `4` | total_aset_thn_var |
| `rentang_aset_thn` | `26` | 28. c1. Jika tidak dapat mengisikan nilai nominal, pilih nilai total aset dalam rentang berikut |
| `luas_tanah_thn` | `28` | 28. d. Berapa luas tanah yang dikuasai dan digunakan untuk kegiatan usaha pada 31 Desember 2025 ? (m2) |
| `cek_asetThn_pml` | `26` | &nbsp;&nbsp;
Cek Rincian Aset 31 Des 2025 (Diisi oleh PML) |
| `info_modal` | `3` | 29. Bagaimana susunan kepemilikan modal di usaha/perusahaan ini pada 31 Desember 2025? |
| `pribadi` | `28` | 29. a. Pribadi/Perorangan |
| `non_profit` | `28` | 29. b. Lembaga Nonprofit yang Melayani Rumah Tangga |
| `publik` | `28` | 29. c. Korporasi Publik |
| `non_publik` | `28` | 29. d. Korporasi Non Publik |
| `pemerintah` | `28` | 29. e. Pemerintah |
| `asing` | `28` | 29. f. Asing |
| `info_total_var` | `4` | info_total_var |
| `info_total` | `28` | 29. g. Total (a+b+c+d+e+f)    =    100 % |
| `head_pengeluaran_bln` | `3` | PENGELUARAN, PENDAPATAN, DAN ASET SATU BULAN TERAKHIR
  
  
      [Rincian 30-33 hanya ditanyakan jika usaha/perusahaan beroperasi secara komersial pada tahun 2026] |
| `info_pengeluaran_bln` | `3` | 30. Rincian Pengeluaran Selama Satu Bulan Terakhir


Contoh: Usaha/perusahaan beroperasi komersial bulan Juni 2026, maka nilai yang dicatat adalah data sebulan penuh tanggal 1-31 Mei 2026. |
| `gaji_bln` | `20` | 30. a. Total upah dan gaji, serta jaminan sosial pegawai |
| `biaya_produksi_bln` | `20` | 30. b. Biaya produksi |
| `biaya_pembelian_bln` | `20` | 30. c. Biaya pembelian barang yang terjual |
| `operasional_bln` | `20` | 30. d. Biaya operasional (air, listrik, gas, internet, pulsa, pemeliharaan, biaya angkutan) |
| `non_operasional_bln` | `20` | 30. e. Biaya non-operasional |
| `cek_output30f_pml` | `26` | &nbsp;&nbsp;
Cek Rincian Pengeluaran di satu bulan terakhir (Diisi oleh PML) |
| `total_pengeluaran_bln` | `20` | 30. f. Total pengeluaran (a+b+c+d+e) |
| `total_pengeluaran_bln_var` | `4` | total_pengeluaran_bln |
| `tampilan_30` | `3` | Petunjuk 30. Rincian Pengeluaran
    
    
        
            <!--
            <!--    
            <!--        Termasuk:
            <!--        Tidak termasuk:
            <!--    
            <!--
            
                
                    
                        
                               Petunjuk:
a. Total upah dan gaji, serta jaminan sosial pegawai.
Termasuk: 
o Upah dan gaji pegawai/karyawan yang telah dikeluarkan ringkasan pembayarannya (group sertificate)
o Komisi dan tips untuk pegawai/karyawan Bonus
o Pembayaran Cuti tahunan dan jenis cuti lainnya
Tidak Termasuk: 
o Upah dan gaji yang dikapitalisasi
o Pembayaran untuk konsultan dan kontraktor yang berusaha sendiri (bukan karyawan perusahaan),
yang dibayarkan dengan komisi

b. Biaya produksi (pemakaian bahan baku dan penolong)
Catatan: Mencakup seluruh nilai barang dan jasa yang digunakan sebagai bahan baku dalam proses produksi, tidak termasuk aset tetap. 
Pada usaha pertanian, ongkos/biaya yang dicatat adalah biaya dari barang/jasa yang benar-benar DIBELI/DIBAYARKAN dan 
TELAH DIGUNAKAN (tidak termasuk yang disimpan, diberikan ke pihak lain, dsb) untuk usaha tanaman pangan, hortikultura,
perkebunan, peternakan, kehutanan, dan perikanan selama periode tahun 2025. Biaya produksi meliputi benih, bibit, pupuk, 
pestisida, vaksin, vitamin, obat-obatan, pakan, umpan, wadah, tali, es, garam, konsumsi awak kapal, dll.
Termasuk: Pembelian bahan yang digunakan dalam proses produksi dan pengemasan
Tidak Termasuk: Pembelian barang yang dikapitalisasi,Perubahan persediaan
, Pembelian barang jadi untuk dijual kembali

c. Biaya pembelian barang yang dijual
Mencakup seluruh nilai pembelian barang perdagangan yang terjual. Contoh: nilai pembelian beras yang terjual, nilai pembelian tepung yang terjual, dsb.

d. Biaya operasional (air, listrik, gas, internet, pulsa, pemeliharaan, biaya angkutan)
Catatan: Mencakup biaya-biaya yang tidak secara langsung dalam proses produksi seperti air, listrik, gas, pemeliharaan, serta biaya angkutan 
Termasuk: 
o Pengeluaran listrik, bahan bakar dan air
o Pembelian bahan perkantoran umum
o Pembelian komponen dan bahan bakar untuk kendaraan bermotor
pembayaran ke pihak lain untuk kargo, delivery, dan jasa angkutan
o Pembayaran sewa operasi (dengan atau tanpa operator)
o Biaya lisensi software komputer yang berumur kurang dari satu tahun (termasuk biaya instalasi oleh provider eksternal) Biaya bank selain bunga
Tidak Termasuk: Pemeliharaan besar
e. Biaya non-operasional
Catatan: Mencakup biaya bunga, biaya pajak, biaya administrasi, biaya hukum, biaya donasi, biaya restrukturisasi, biaya kerugian di awal, dan biaya lain-lain yang tidak terkait dengan kegiatan operasional, seperti biaya perjalanan yang tidak terkait dengan bisnis. |
| `info_pendapatan_bln` | `3` | 31. Rincian Nilai $narasi Selama Satu Bulan Terakhir


Contoh: Usaha/perusahaan beroperasi komersial bulan Juni 2026, maka nilai yang dicatat adalah data sebulan penuh tanggal 1-31 Mei 2026. |
| `nilai_pendapatan_bln` | `20` | 31. a. Nilai $narasi barang dan jasa |
| `pendapatan_lain_bln` | `20` | 31. b. Pendapatan lainnya yang dihasilkan |
| `total_pendapatan_bln` | `20` | 31. c. Total nilai $narasi (a+b) |
| `total_pendapatan_bln_var` | `4` | total_pendapatan_bln_var |
| `cek_input31c_pml` | `26` | &nbsp;&nbsp;
Cek Rincian Pendapatan di satu bulan terakhir (Diisi oleh PML) |
| `pendapatan_online_bln` | `28` | 31. d. Berapa persentase pendapatan yang dilakukan secara online ? |
| `tampilan_31` | `3` | Petunjuk 31. Rincian  Produksi/Penjualan/Pendapatan
    
    
        
            <!--
            <!--    
            <!--        Termasuk:
            <!--        Tidak termasuk:
            <!--    
            <!--
            
                
                    
                        
                               Petunjuk:
a. Nilai produksi/penjualan/pendapatan barang dan jasa
Termasuk: 
o Barang yang dijual baik yang diproduksi sendiri maupun tidak
o Penjualan ekspor (FOB-Free On Board )
o Penjualan atau transfer ke rekan bisnis/ organisasi atau cabang di luar negeri
o Pendapatan yang diperoleh dari pengangkutan barang yang tidak dijual perusahaan
o Pendapatan jasa perbaikan dan layanan
o Pendapatan dari kontrak, subkontrak dan komisi
o Pendapatan manajemen dari perusahaan/organisasi terkait maupun tidak
o Pendapatan dari jasa pemasangan
o Pendapatan dari jasa berlangganan dan keanggotaan
o Pendapatan dari jasa iklan
o Pendapatan royalti (hak cipta, hak paten, waralaba, dll)
o Pendapatan dari sewa operasi
Tidak Termasuk: 
o Penjualan aset
o Royalti dari penggunaan lahan di bawah pengaturan sewa mineral
Catatan: Pada usaha pertanian, nilai produksi yang dicatat yaitu nilai produksi yang dipanen, dikonsumsi sendiri (termasuk yang digunakan 
untuk bibit), diolah sendiri, dijual, disimpan, digunakan sebagai upah/gaji pekerja, diberikan kepada pihak lain, hilang, pertambahan 
bobot ternak, serta nilai pembesaran tanaman kehutanan selama periode tahun 2025 sesuai dengan jenis dan satuan produksi 
pada masing-masing subsektor yang diusahakan. Nilai produksi yang dicakup termasuk nilai produksi ikutan yang dijual.

b. Pendapatan lainnya yang dihasilkan
Termasuk: 
o Sewa/royalti sumber daya alam
o Pendapatan bunga
o Pendapatan dividen
o Pendanaan dari Pemerintah (subsidi, skema magang dan pelatihan)
o Donasi
Tidak Termasuk: Pendanaan yang disediakan khusus untuk barang modal tertentu |
| `bln_operasi` | `29` | 31. e. Bulan beroperasi selama tahun 2026 |
| `aset_tanah_bln` | `20` | 32. a. Nilai aset tanah dan bangunan pada akhir bulan yang lalu |
| `aset_lain_bln` | `20` | 32. b. Nilai aset selain tanah dan bangunan pada akhir bulan yang lalu |
| `total_aset_bln` | `4` | 32. c. Nilai total aset pada akhir bulan yang lalu* |
| `rentang_aset_bln` | `26` | 32. c1. Jika tidak dapat mengisikan nilai nominal, pilih nilai total aset dalam rentang berikut: |
| `luas_tanah_bln` | `28` | 32. d. Berapa luas tanah yang dikuasai dan digunakan untuk kegiatan usaha
pada akhir bulan yang lalu (m2) ? |
| `cek_asetBln_pml` | `26` | Cek Rincian aset pada akhir bulan yang lalu (Diisi oleh PML) |
| `info_modal_bln` | `3` | 33. Bagaimana susunan kepemilikan modal di usaha/perusahaan ini pada saat didirikan? |
| `pribadi_didirikan` | `28` | 33. a. Pribadi/Perorangan |
| `nonprofit_didirikan` | `28` | 33. b. Lembaga Nonprofit yang Melayani Rumah Tangga |
| `publik_didirikan` | `28` | 33. c. Korporasi publik (%) |
| `nonpublik_didirikan` | `28` | 33. d. Korporasi Non Publik |
| `pemerintah_didirikan` | `28` | 33. e. Pemerintah |
| `asing_didirikan` | `28` | 33. f. Asing |
| `cek5` | `4` | New Question |
| `info_total_didirikan` | `28` | 33. g. Total (a+b+c+d+e+f)    =    100 % |
| `info_total_didirikan_var` | `4` | info_total_didirikan_var |
| `kp_nested_instruction` | `3` | 🔍 Untuk melanjutkan pengisian Keterangan Kantor Cabang/Unit, silakan klik tombol Lihat pada bagian di bawah ini. |

## SE2026 - L BLOK III

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `keluarga_head` | `3` | KETERANGAN IDENTITAS KELUARGA |
| `dtsen_nama_kk` | `4` | 1. a. Nama Kepala Keluarga |
| `nik_kk` | `4` | 1. b. NIK Kepala Keluarga |
| `dtsen_no_kk` | `4` | 1. c. Nomor kartu keluarga |
| `jml_kk` | `4` | 2. a. Jumlah anggota keluarga sesuai KK |
| `jml_kk_asgbaru` | `25` | 2. a. Jumlah anggota keluarga sesuai KK |
| `jml_kk_update` | `4` | 2. b. Jumlah anggota keluarga sesuai hasil pendataan |
| `inividu_head_new` | `3` | KETERANGAN ANGGOTA KELUARGA 
    
    
    
        (LANJUTAN) |
| `nested_dtsen_instruction` | `3` | 🔍 Untuk melanjutkan pengisian Blok Keterangan Anggota Keluarga Lanjutan, silakan klik tombol Lihat pada bagian di bawah ini. |
| `prelist_dtsen_var` | `4` | Nama anggota keluarga prelist |
| `tambah_dtsen_var` | `4` | Nama anggota keluarga tambahan |
| `gabung_dtsen_var` | `4` | gabung_dtsen |
| `gabung_dtsen_2` | `4` | gabung_dtsen_2 |
| `total_pendapatan_keluarga_sebulan` | `4` | total_pendapatan_keluarga_sebulan (sudah dari semua anggota keluarga) |
| `hidden_blok_3` | `3` | ℹ️ Halaman ini tidak memerlukan pengisian karena tidak terdapat pertanyaan yang ditujukan kepada responden pada bagian ini. Silakan lanjutkan ke halaman berikutnya sesuai petunjuk yang tersedia. |
| `nested_dtsen_var` | `2` | Keterangan Anggota Keluarga |
| `no_urut_kk_var` | `4` | Nomor urut anggota keluarga |
| `nama_dtsen_var` | `4` | Nama anggota keluarga |
| `head_ak_var` | `3` | KETERANGAN PENDIDIKAN, KETENAGAKERJAAN, DAN KEPEMILIKAN REKENING |
| `ec_art_dtsen` | `4` | ec_art_dtsen |
| `ec_art_pendapatan` | `4` | ec_art_pendapatan |
| `set_sekolah_prelist` | `4` | set_sekolah_prelist |
| `sekolah_prelist` | `4` | Sekolah Prelist |
| `sekolah` | `26` | 14. Partisipasi sekolah $NAME$
(usia 5 tahun ke atas) |
| `set_ijazah_prelist` | `4` | set_ijazah_prelist |
| `ijazah_prelist` | `4` | Ijazah Prelist |
| `ijazah` | `26` | 15. Ijazah/STTB tertinggi yang dimiliki $NAME$
(usia 5 tahun ke atas)
Ijazah/STTB tertinggi di prelist: $ijazah |
| `profesi` | `27` | 16. Profesi Pekerjaan Utama  $NAME$
(usia 10 tahun ke atas) |
| `profesi_lainnya` | `25` | &nbsp;&nbsp;Profesi Pekerjaan Utama lainnya: |
| `status_kerja` | `26` | 17. Status Kedudukan Dalam Pekerjaan Utama $NAME$
(usia 10 tahun ke atas) |
| `pendapatan_dtsen` | `3` | 18. Apakah $NAME$ biasanya memiliki pendapatan (tetap maupun tidak tetap dalam
sebulan) ? 
(usia 5 tahun ke atas) |
| `pendapatan_pekerjaan` | `26` | 18. a. Pendapatan dari pekerjaan baik berupa uang maupun barang/jasa (gaji, tunjangan,
uang makan, honor, lembur, dll) |
| `pend_gaji` | `20` | a. Upah/Gaji |
| `pend_tunjangan` | `20` | b. Tunjangan |
| `pend_uangmkn` | `20` | c. Uang Makan |
| `pend_honor` | `20` | d. Honor |
| `pend_lembur` | `20` | e. Lembur |
| `pend_lainnya` | `20` | f. Lainnya |
| `nilai_pend_pekerjaan` | `4` | 18. a1. Total Pendapatan (a+b+c+d+e+f) |
| `pendapatan_usaha` | `26` | 18. b. Pendapatan dari usaha, baik offline (warung, kos-kosan, dll) maupun
online (affiliate, online shop, endorse, youtuber, dll ): |
| `pend_usaha` | `20` | 18. b1. Total Pendapatan |
| `pend_usaha_lain` | `26` | 18. c. Penerimaan pendapatan lain (transfer/pemberian/passive income seperti
pensiunan, kupon SBN, Obligasi, dll ): |
| `nilai_pend_lain` | `20` | 18. c1. Total Pendapatan |
| `rekening` | `26` | 19. Apakah $NAME$ memiliki rekening aktif atau dompet digital?
(usia 5 tahun ke atas) |
| `head_disabilitas` | `3` | KETERANGAN DISABILITAS DAN PENYAKIT KRONIS |
| `isdisabilitas` | `3` | 20. Apakah $NAME$ memiliki keterbatasan dalam jangka waktu lama sehingga mengalami kesulitan dalam menjalankan aktivitas sehari-hari (disabilitas)? |
| `dis_fisik` | `26` | a. Disabilitas Fisik |
| `dis_mental` | `26` | b. Disabilitas Mental |
| `dis_intelek` | `26` | c. Disabilitas Intelektual |
| `dis_netra` | `26` | d. Disabilitas Sensorik Netra |
| `dis_rungu` | `26` | e. Disabilitas Sensorik Rungu |
| `dis_wicara` | `26` | f. Disabilitas Sensorik Wicara |
| `iskesehatan` | `3` | 21. Apakah $NAME$ memiliki keluhan kesehatan
kronis/menahun? |
| `sakit_hipertensi` | `26` | a. Hipertensi (tekanan darah tinggi) |
| `sakit_rematik` | `26` | b. Rematik |
| `sakit_asma` | `26` | c. Asma |
| `sakit_jantung` | `26` | d. Masalah jantung |
| `sakit_diabetes` | `26` | e. Diabetes (kencing manis) |
| `sakit_tbc` | `26` | f. Tuberkulosis (TBC) |
| `sakit_stroke` | `26` | g. Stroke |
| `sakit_kanker` | `26` | h. Kanker atau tumor ganas |
| `sakit_hemofilia` | `26` | j. Hemofilia |
| `sakit_ginjal` | `26` | i. Gagal ginjal |
| `sakit_hiv` | `26` | k. HIV/AIDS |
| `sakit_kolestrol` | `26` | l. Kolestrol |
| `sakit_sirosis` | `26` | m. Sirosis hati |
| `sakit_talasemia` | `26` | n. Talasemia |
| `sakit_leukemia` | `26` | o. Leukemia |
| `sakit_alzheimer` | `26` | p. Alzheimer |
| `sakit_lainnya` | `26` | q. Lainnya |

## SE2026 - L BLOK IV

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `perumahan_head1` | `3` | KETERANGAN PERUMAHAN |
| `total_pengeluaran_keluarga_sebulan` | `4` | total_pengeluaran_keluarga_sebulan |
| `jns_bangunan` | `26` | 1. a. Apa jenis bangunan tempat tinggal yang ditempati? |
| `jns_bangunan_lain` | `25` | 1. a. Jenis bangunan tempat tinggal kode 5.Lainnya: ................. |
| `nm_apt` | `25` | 1. b. Jika apartemen/rumah susun, sebutkan Nama/Nomor Lantai: . |
| `jml_ak_tinggal` | `28` | 2. a. Berapa jumlah keluarga yang tinggal dalam 1 rumah/tempat tinggal? |
| `list_ak_tinggal` | `21` | 2. b. Sebutkan Nomor KK dari keluarga yang tinggal dalam 1 rumah/tempat tinggal! Selain yang disebutkan pada |
| `status_kepemilikan` | `26` | 3. a. Apa status kepemilikan bangunan tempat tinggal yang ditempati? |
| `status_kepemilikan_lain` | `25` | 3. a. Deskripsi status kepemilikan bangunan tempat tinggal yang ditempati lainnya |
| `bukti_kepemilikan` | `26` | 3. b. Jika tempat tinggal milik sendiri, apa jenis bukti kepemilikan tanah bangunan tempat tinggal ini? |
| `nilai_sewa` | `3` | 4. Perkiraan nilai sewa/kontrak sebulan: |
| `sewa_sendiri` | `20` | &nbsp;&nbsp;a. Jika milik sendiri/bebas sewa, perkiraan harga sewa
sebulan: |
| `sewa_kontrak` | `20` | &nbsp;&nbsp;b. Jika kontrak/sewa , nilai kontrak sebulan: |
| `sewa_dinas` | `20` | &nbsp;&nbsp;c. Jika dinas atau lainnya, perkiraan nilai sewa sebulan: |
| `luas_lantai` | `28` | 5. Berapa luas lantai bangunan tempat tinggal? (m²) |
| `jns_lantai` | `26` | 6. a. Apakah bahan bangunan utama lantai rumah terluas? |
| `kondisi_lantai` | `26` | 6. b. Kondisi Lantai |
| `jns_dinding` | `26` | 7. a. Apakah bahan bangunan utama dinding rumah terluas? |
| `kondisi_dinding` | `26` | 7. b. Kondisi Dinding |
| `jns_atap` | `26` | 8. a. Apakah bahan bangunan utama atap rumah terluas? |
| `kondisi_atap` | `26` | 8. b. Kondisi Atap |
| `tempat_bab` | `26` | 9. Apakah memiliki fasilitas tempat buang air besar dan siapa saja yang menggunakan? |
| `jns_closet` | `26` | 10. Apakah jenis kloset yang digunakan? |
| `buang_tinja` | `26` | 11. Di manakah tempat pembuangan akhir tinja? |
| `air_minum` | `26` | 12.  Apakah sumber air utama yang digunakan keluarga untuk minum? |
| `sumber_penerangan` | `26` | 13. Apakah sumber utama penerangan rumah tangga ini? |
| `jml_meteran` | `28` | 14. a. Jika  listrik PLN dengan meteran, berapa jumlah meteran listrik yang terpasang di rumah ini? |
| `nested_meteran_instruction` | `3` | 🔍 Untuk melanjutkan pengisian Daya Meteran, silakan klik tombol Lihat pada bagian di bawah ini. |
| `nested_meteran` | `2` | 14. b. Berapa daya yang terpasang di rumah ini? |
| `urutan_meteran_lain` | `4` | Meteran ke- |
| `daya_terpasang` | `26` | 14. b. Berapa daya yang terpasang di rumah ini? |
| `id_pln_pilih` | `26` | 14. c. Sebutkan ID Pelanggan PLN atau Nomor Meteran |
| `id_pelanggan` | `25` | &nbsp;&nbsp;&nbsp;&nbsp;ID Pelanggan PLN |
| `banner_cek_idpel` | `3` | Silakan lakukan pengecekan ID Pelanggan dengan menekan tombol CEK ID PELANGGAN di bawah ini. |
| `cek_idpel` | `6` | CEK ID PELANGGAN |
| `hasilCekIdPel` | `4` | ​ |
| `htmlHasilCekIdPel` | `4` | ​ |
| `no_meteran` | `25` | &nbsp;&nbsp;&nbsp;&nbsp;Nomor Meteran |
| `result_cekidpel` | `4` | ​ |
| `banner_cek_no_meteran` | `3` | Silakan lakukan pengecekan nomor meteran dengan menekan tombol CEK NOMOR METERAN di bawah ini. |
| `cek_no_meteran` | `6` | CEK NOMOR METERAN |
| `htmlHasilCekMeteran` | `4` | ​ |
| `hasilCekMeteran` | `4` | ​ |
| `result_cekmeteran` | `4` | result_cekmeteran |
| `listrik_sebulan` | `20` | 15. a. Berapa nilai pengeluaran listrik sebulan? 
 (Dapat menggunakan pertanyaan seperti: biasanya, rata-rata, atau sebulan terakhir) |
| `pulsa_sebulan` | `20` | 15. b. Berapa pengeluaran pulsa dan internet seluruh anggota keluarga sebulan?
 (Dapat menggunakan pertanyaan seperti: biasanya, rata-rata, atau sebulan terakhir) |
| `pengeluaran_makanan_mingguan` | `20` | 16. a. Berapa rata-rata pengeluaran makanan keluarga seminggu? |
| `jml_meteran_var` | `4` | jml_meteran_var |
| `pengeluaran_non_makan_bulanan` | `20` | 16. b. Berapa rata-rata pengeluaran bukan makanan rutin keluarga bulanan? |
| `pengeluaran_non_makan_tahunan` | `20` | 16. c. Berapa rata-rata pengeluaran bukan makanan rutin keluarga tahunan? |
| `aset_head` | `3` | KETERANGAN KEPEMILIKAN ASET |
| `aset_bergerak` | `3` | 17. Apakah keluarga ini memiliki barang-barang sebagai berikut? Berapa jumlahnya? : |
| `jumlah_tabung3kg` | `4` | jumlah_tabung3kg_prelist |
| `jumlah_tabung3kg_new` | `28` | a. Tabung gas 3 kg (unit) |
| `jumlah_tabung5kg` | `4` | jumlah_tabung5kg_prelist |
| `jumlah_tabung5kg_new` | `28` | b. Tabung gas 5,5 kg atau lebih (unit) |
| `jumlah_kulkas` | `4` | jumlah_kulkas_prelist |
| `jumlah_kulkas_new` | `28` | c. Lemari es/kulkas (unit) |
| `jumlah_ac` | `4` | jumlah_ac_prelist |
| `jumlah_ac_new` | `28` | d. Air Conditioner (AC) (unit) |
| `jumlah_emas` | `4` | jumlah_emas_prelist |
| `jumlah_emas_new` | `28` | e. Emas/perhiasan (gram) |
| `jumlah_laptop` | `4` | jumlah_laptop_prelist |
| `jumlah_laptop_new` | `28` | f. Komputer/laptop/tablet: (unit) |
| `jumlah_motor` | `4` | jumlah_motor_prelist |
| `jumlah_motor_new` | `28` | g. i. Sepeda motor (termasuk sepeda motor listrik): |
| `nilai_motor` | `20` | g. ii. Total nilai aset sepeda motor (rupiah) |
| `jumlah_mobil` | `4` | jumlah_mobil_prelist |
| `jumlah_mobil_new` | `28` | h. i. Mobil (termasuk mobil listrik): |
| `nilai_mobil` | `20` | h. ii. Total nilai aset mobil (rupiah) |
| `aset_tidak_bergerak` | `3` | 18. Apakah Keluarga ini memiliki aset tidak bergerak sebagai berikut? |
| `jumlah_lahan` | `4` | jumlah_lahan_prelist |
| `jumlah_lahan_new` | `28` | a. i. Jumlah tanah/lahan di tempat lain (selain yang ditempati): |
| `nilai_lahan` | `20` | a. ii. Total nilai harga jual tanah/lahan di tempat lain (selain yang ditempati): |
| `jumlah_rumah` | `4` | jumlah_rumah_prelist |
| `jumlah_rumah_new` | `28` | b. i. Jumlah rumah/bangunan di tempat lain (selain yang ditempati): |
| `nilai_rumah` | `20` | b. ii. Total nilai harga jual rumah/bangunan di tempat lain (selain yang ditempati): |
| `foto_rumah` | `3` | 19. Foto rumah (2 buah yang mencerminkan kualitas bangunan) |
| `foto_depan` | `32` | Foto tampak depan (harus mencakup atap dan dinding) |
| `foto_ruang_tamu` | `32` | Foto ruang tamu (harus mencakup dinding dan lantai) |
| `hidden_blok_4` | `3` | ℹ️ Halaman ini tidak memerlukan pengisian karena tidak terdapat pertanyaan yang ditujukan kepada responden pada bagian ini. Silakan lanjutkan ke halaman berikutnya sesuai petunjuk yang tersedia. |
| `set_default_aset` | `4` | set_default_aset |

## KETERANGAN PEMBERI JAWABAN

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `jawaban_head` | `3` | KETERANGAN PEMBERI JAWABAN |
| `nama_info_list` | `27` | Nama Pemberi Informasi |
| `nama_info` | `4` | nama_info_cawi |
| `ak_info` | `4` | ak_info |
| `nama_lain` | `25` | Nama Lain |
| `telp_info` | `25` | Nomor HP/Telepon |
| `email_info` | `25` | E-mail |
| `tanda_info` | `36` | Tanda Tangan |

## CATATAN

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `catatan_head` | `3` | CATATAN |
| `catatan` | `30` | Catatan |
| `idsbr_keluarga` | `4` | ID SBR keluarga |
| `idsbr_match` | `4` | ID SBR Match |
| `id_l1_umkm` | `4` | New Question |
| `id_l2_umkm` | `4` | New Question |
| `id_keluarga` | `4` | New Question |
| `id_regsosek` | `4` | New Question |
| `waktu_selesai` | `35` | Waktu Selesai |
| `daftar_anomali` | `4` | daftar_anomali |

## ANOMALI

| Variabel | Tipe | Pertanyaan |
| --- | --- | --- |
| `anomali_head` | `3` | PENGECEKAN ANOMALI |
| `banner_anomali` | `3` | ⚠️ Langkah Pengecekan Anomali:
    
        Periksa setiap jenis anomali, silakan lakukan perbaikan data sampai usaha/keluarga hilang dari daftar anomali.
        Apabila data memang sesuai kondisi lapangan, berikan centang "Ya, Sesuai Kondisi Lapangan" lalu berikan penjelasan. |
| `banner_no_anomali` | `3` | ✅ Tidak Ditemukan Anomali
    

    
        Hasil pemeriksaan menunjukkan bahwa data usaha/perusahaan pada assignment ini tidak memiliki anomali berdasarkan aturan validasi yang diterapkan pada kuesioner SE2026. |
| `cek_anomali` | `4` | CEK ANOMALI |
| `custom_script_table` | `4` | custom_script_table |
| `tanggal_anomali` | `4` | tanggal_anomali |
| `tanggal_selesai_anomali` | `4` | tanggal_selesai_anomali |
| `anomali_1_deskripsi` | `3` | $tabel |
| `anomali_1_check` | `29` | Apakah data di atas sesuai kondisi lapangan? |
| `anomali_1_penjelasan` | `30` | Penjelasan Anomali 1 |
| `anomali_2_deskripsi` | `3` | $tabel |
| `anomali_2_check` | `29` | Apakah data di atas sesuai kondisi lapangan? |
| `anomali_2_penjelasan` | `30` | Penjelasan Anomali 2 |
| `anomali_3_deskripsi` | `3` | $tabel |
| `anomali_3_check` | `29` | Apakah data di atas sesuai kondisi lapangan? |
| `anomali_3_penjelasan` | `30` | Penjelasan Anomali 3 |
| `anomali_4_deskripsi` | `3` | $tabel |
| `anomali_4_check` | `29` | Apakah data di atas sesuai kondisi lapangan? |
| `anomali_4_penjelasan` | `30` | Penjelasan Anomali 4 |
| `anomali_5_deskripsi` | `3` | $tabel |
| `anomali_5_check` | `29` | Apakah data di atas sesuai kondisi lapangan? |
| `anomali_5_penjelasan` | `30` | Penjelasan Anomali 5 |
| `anomali_6_deskripsi` | `3` | $tabel |
| `anomali_6_check` | `29` | Apakah data di atas sesuai kondisi lapangan? |
| `anomali_6_penjelasan` | `30` | Penjelasan Anomali 6 |
| `anomali_7_deskripsi` | `3` | $tabel |
| `anomali_7_check` | `29` | Apakah data di atas sesuai kondisi lapangan? |
| `anomali_7_penjelasan` | `30` | Penjelasan Anomali 7 |
