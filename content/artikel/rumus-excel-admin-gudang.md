---
id: L28
slug: rumus-excel-admin-gudang
judul: "3 Rumus Excel untuk Admin Gudang: SUMIF, XLOOKUP, dan Pivot Table"
seo_title: "Rumus Excel untuk Admin Gudang: SUMIF, XLOOKUP, Pivot"
deskripsi: "Rumus Excel untuk admin gudang yang paling sering dipakai: SUMIF untuk total stok, XLOOKUP untuk cari data SKU, dan pivot table untuk rekap laporan."
kategori: karier-logistik
kata_kunci: ["rumus excel untuk admin gudang", "rumus excel admin gudang", "skill excel admin gudang", "rumus SUMIF stok barang", "VLOOKUP dan XLOOKUP", "pivot table rekap stok", "laporan stok barang excel", "rekap barang keluar excel"]
terbit: 2026-11-13
intinya: "Tiga rumus Excel yang paling sering dipakai admin gudang: **SUMIF** untuk menjumlah dengan syarat, **VLOOKUP atau XLOOKUP** untuk mencari data dari tabel lain, dan **pivot table** untuk merangkum ribuan baris jadi laporan ringkas."
faq:
  - q: "Rumus Excel apa yang wajib dikuasai admin gudang?"
    a: "Tiga yang paling sering dipakai adalah SUMIF, VLOOKUP atau XLOOKUP, dan pivot table. SUMIF menjumlahkan angka dengan syarat, misalnya total barang keluar untuk satu SKU. XLOOKUP mencari data dari tabel lain, dan pivot table merangkum ribuan baris transaksi menjadi tabel ringkas."
  - q: "Apa bedanya VLOOKUP dan XLOOKUP?"
    a: "VLOOKUP hanya bisa mencari di kolom paling kiri tabel dan butuh nomor kolom untuk hasilnya. XLOOKUP memakai kolom cari dan kolom hasil yang terpisah, jadi bisa mencari ke arah mana saja, dan secara bawaan langsung mencari yang sama persis. Kekurangannya, XLOOKUP tidak tersedia di Excel 2016 dan 2019."
  - q: "Kenapa VLOOKUP saya hasilnya salah atau #N/A?"
    a: "Penyebab paling umum adalah argumen terakhir tidak diisi FALSE, sehingga Excel mencari nilai yang mendekati, bukan yang sama persis. #N/A biasanya berarti kode yang dicari memang tidak ditemukan, misalnya karena ada spasi tambahan atau penulisan kode berbeda. Cek juga apakah kode yang dicari ada di kolom paling kiri tabel."
  - q: "Kenapa pivot table tidak berubah padahal data sudah ditambah?"
    a: "Pivot table tidak memperbarui dirinya sendiri saat data sumber berubah. Klik kanan di dalam pivot table lalu pilih Refresh. Supaya baris baru ikut terbaca, simpan data sumber dalam format tabel Excel."
  - q: "Bagaimana cara cepat belajar Excel untuk admin gudang?"
    a: "Mulai dari satu rumus dan langsung pakai di data kerja Anda sendiri, misalnya data barang keluar minggu lalu. Setelah lancar, tambah rumus berikutnya. Belajar dari pekerjaan sehari-hari biasanya lebih cepat menempel daripada menghafal daftar rumus."
sumber:
  - judul: "Microsoft Support, SUMIF function"
    url: "https://support.microsoft.com/en-gb/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b"
    catatan: "SUMIF menjumlahkan nilai dalam rentang yang memenuhi kriteria; sintaks SUMIF(range, criteria, [sum_range]); kriteria teks diapit tanda kutip ganda; wildcard ? dan *; untuk banyak syarat gunakan SUMIFS."
  - judul: "Microsoft Support, VLOOKUP function"
    url: "https://support.microsoft.com/en-us/Excel/vlookup-function"
    catatan: "Sintaks VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup]); nilai yang dicari harus ada di kolom pertama; FALSE atau 0 untuk pencocokan persis; bila dikosongkan bawaannya TRUE (perkiraan); #N/A biasanya berarti tidak ditemukan."
  - judul: "Microsoft Support, Fungsi XLOOKUP"
    url: "https://support.microsoft.com/id-id/office/fungsi-xlookup-b7fd680e-6d10-43e6-84f9-88eae8bf5929"
    catatan: "XLOOKUP mencari di satu rentang dan mengembalikan nilai dari rentang lain di sisi mana pun; argumen if_not_found opsional (tanpa itu hasilnya #N/A); match_mode bawaan pencocokan persis; VLOOKUP hanya bisa mencari ke kanan; catatan bahwa XLOOKUP tidak tersedia di Excel 2016 dan Excel 2019."
  - judul: "Microsoft Support, Create a PivotTable to analyze worksheet data"
    url: "https://support.microsoft.com/office/18fb0032-b01a-4c99-9a5f-7ab09edde05a"
    catatan: "PivotTable menghitung, merangkum, dan menganalisis data; data sebaiknya rapi berbentuk tabel dengan satu baris judul kolom yang unik, tanpa sel gabung; format sebagai tabel Excel; buat lewat Insert > PivotTable; area Rows, Columns, Values; angka di Values bawaannya SUM, teks dihitung COUNT; tidak diperbarui otomatis, gunakan Refresh."
  - judul: "MrExcel, Commas Stop Working in Formulas"
    url: "https://mrexcel.com/excel-tips/commas-stop-working-in-formulas"
    catatan: "Pemisah argumen rumus Excel mengikuti pengaturan List Separator di Windows; bila pemisah desimal berupa koma, Excel memakai titik koma sebagai pemisah argumen."
---
Rumus Excel untuk admin gudang sebenarnya tidak perlu banyak. Tiga yang paling sering dipakai adalah **SUMIF** untuk menjumlah angka dengan syarat, **VLOOKUP atau XLOOKUP** untuk mencari data dari tabel lain, dan **pivot table** untuk merangkum ribuan baris jadi laporan ringkas. Dengan tiga alat ini, sebagian besar laporan stok harian sudah bisa dikerjakan.

Artikel ini versi lengkap dari video 60 detik Ngerti Logistik tentang skill Excel untuk admin gudang.

![Ringkasan tiga rumus Excel untuk admin gudang: SUMIF untuk menjumlah dengan syarat, XLOOKUP untuk mencari data, pivot table untuk merangkum laporan](/img/ilustrasi/rumus-excel-admin-gudang/1-tiga-rumus.webp){width="960" height="595" loading="lazy" style="border-radius:16px"}

## Kenapa admin gudang perlu Excel?

Salah satu tugas utama admin gudang adalah mencatat transaksi dan menyusun laporan. Peran ini dibahas di artikel [tugas staf gudang](L10). Setiap hari ada barang masuk, barang keluar, dan pertanyaan dari atasan: "Stok barang ini tinggal berapa?" atau "Minggu ini barang apa yang paling banyak keluar?"

Kalau datanya ada ratusan sampai ribuan baris, menjumlah manual pakai kalkulator rawan salah dan makan waktu. Rumus membuat pekerjaan ini cepat dan bisa diulang setiap hari.

Supaya ketiga rumus di bawah bekerja dengan baik, siapkan dua jenis tabel:

- **Tabel transaksi**: satu baris untuk satu transaksi, misalnya tanggal, kode [SKU](L03), jumlah, dan jenis (masuk atau keluar).
- **Tabel master barang**: satu baris untuk satu SKU, berisi nama barang, kategori, dan lokasi rak.

## 1. SUMIF: menjumlah dengan syarat

Menurut Microsoft Support, SUMIF menjumlahkan nilai dalam sebuah rentang yang memenuhi kriteria yang Anda tentukan. Di gudang, ini cocok untuk pertanyaan seperti "berapa total barang keluar untuk SKU tertentu?"

Bentuk rumusnya:

`=SUMIF(rentang_syarat, syarat, rentang_dijumlah)`

- **rentang_syarat**: kolom yang dicek, misalnya kolom kode SKU.
- **syarat**: nilai yang dicari. Kalau berupa teks, apit dengan tanda kutip ganda.
- **rentang_dijumlah**: kolom angka yang mau dijumlah, misalnya kolom jumlah keluar.

> **CONTOH** Tabel barang keluar punya lima baris. Kode SKU ada di kolom B, jumlah keluar di kolom D. SKU-A01 muncul tiga kali dengan jumlah 12, 8, dan 20; dua baris lain milik SKU-B07 dengan jumlah 5 dan 15. Rumus `=SUMIF(B2:B6,"SKU-A01",D2:D6)` menghasilkan **40**. Data ini fiktif, hanya untuk menunjukkan cara kerja rumus.

Lebih praktis lagi, ketik kode SKU di satu sel, misalnya G2, lalu pakai `=SUMIF(B2:B6,G2,D2:D6)`. Cukup ganti isi G2, totalnya langsung berubah.

Microsoft Support juga menyebut SUMIF mendukung karakter wildcard: tanda `*` untuk sembarang deretan karakter dan `?` untuk satu karakter. Jadi `"SKU-A*"` akan menjumlah semua SKU yang diawali "SKU-A". Kalau syaratnya lebih dari satu, misalnya SKU tertentu **dan** bulan tertentu, gunakan SUMIFS.

![Contoh cara kerja SUMIF: dari lima baris transaksi, hanya baris SKU-A01 yang dijumlah sehingga totalnya 40](/img/ilustrasi/rumus-excel-admin-gudang/2-contoh-sumif.webp){width="960" height="632" loading="lazy" style="border-radius:16px"}

## 2. VLOOKUP atau XLOOKUP: mencari data dari tabel lain

Rumus kedua dipakai saat Anda punya kode SKU dan ingin tahu informasi lain dari tabel master, misalnya nama barang atau lokasi raknya.

### VLOOKUP

`=VLOOKUP(kode_dicari, tabel_master, nomor_kolom, FALSE)`

Microsoft Support menjelaskan dua hal penting tentang VLOOKUP:

- Kode yang dicari **harus ada di kolom paling kiri** tabel master.
- Argumen terakhir isi **FALSE** supaya mencari yang sama persis. Kalau dikosongkan, Excel memakai pencocokan perkiraan, dan hasilnya bisa salah tanpa terlihat.

### XLOOKUP

`=XLOOKUP(kode_dicari, kolom_kode, kolom_hasil, "Tidak ada")`

Menurut Microsoft Support, XLOOKUP memakai kolom cari dan kolom hasil yang terpisah, jadi kolom hasil boleh berada di kiri maupun kanan kolom kode. Pencocokannya secara bawaan sudah sama persis. Argumen keempat bersifat opsional: teks yang muncul kalau kode tidak ditemukan. Tanpa argumen itu, hasilnya `#N/A`.

> **CONTOH** Tabel master berisi kode SKU di kolom A dan lokasi rak di kolom C. Rumus `=XLOOKUP("SKU-B07",A2:A50,C2:C50,"Tidak ada")` menampilkan lokasi rak SKU-B07, misalnya R-02-03. Kalau kodenya salah ketik, yang muncul tulisan "Tidak ada". Data ini fiktif.

Mana yang dipakai? Kalau Excel Anda mendukung XLOOKUP, pakai itu karena lebih sedikit jebakannya. Microsoft Support mencatat XLOOKUP tidak tersedia di Excel 2016 dan Excel 2019. Di versi itu, tetap pakai VLOOKUP dengan FALSE di akhir.

Satu sumber `#N/A` yang sering terjadi di gudang: kode SKU di dua tabel ditulis berbeda, misalnya ada spasi tambahan. Rapikan penulisan kode sejak awal.

## 3. Pivot table: merangkum ribuan baris

Microsoft Support menyebut pivot table sebagai alat untuk menghitung, merangkum, dan menganalisis data, sehingga pola dan tren lebih mudah terlihat. Untuk admin gudang, ini cara tercepat membuat rekap seperti:

- Total barang keluar per kategori.
- Barang keluar per minggu.
- Jumlah transaksi per SKU.

Langkah dasarnya:

1. Pastikan data rapi: satu baris judul kolom, setiap judul unik dan tidak kosong, tanpa sel yang digabung (merge).
2. Ubah data menjadi tabel Excel lewat **Insert > Table**, supaya baris baru ikut terbaca.
3. Pilih data, lalu **Insert > PivotTable**, dan tentukan lokasinya.
4. Tarik kolom kategori ke area **Rows** dan kolom jumlah ke area **Values**.

Microsoft Support menjelaskan bahwa kolom angka di area Values secara bawaan dijumlah (SUM). Kalau Excel membaca kolom itu sebagai teks, yang muncul justru hitungan baris (COUNT). Jadi jangan campur angka dan teks di kolom jumlah.

Satu hal yang sering terlupa: pivot table **tidak berubah sendiri** saat data sumber berubah. Klik kanan di dalam pivot table, lalu pilih **Refresh**.

![Langkah membuat pivot table untuk rekap stok: rapikan data, ubah jadi tabel, sisipkan pivot table, lalu refresh setiap ada data baru](/img/ilustrasi/rumus-excel-admin-gudang/3-langkah-pivot.webp){width="960" height="489" loading="lazy" style="border-radius:16px"}

## Cara cepat menguasainya

Jangan coba hafal semua sekaligus. Urutan belajar yang praktis:

1. **Minggu pertama: SUMIF.** Hitung total barang keluar per SKU dari data minggu lalu.
2. **Minggu kedua: XLOOKUP atau VLOOKUP.** Tambahkan kolom nama barang dan lokasi rak ke tabel transaksi.
3. **Minggu ketiga: pivot table.** Buat rekap barang keluar per kategori.

Pakai data kerja Anda sendiri. Angka yang Anda kenal membuat Anda cepat sadar kalau hasil rumus terlihat janggal. Hasil rekap ini juga berguna saat membandingkan stok sistem dengan hasil hitung fisik, yang dibahas di artikel [stock opname vs cycle count](L23).

Kalau Excel menolak rumus yang Anda ketik persis seperti di artikel ini, coba ganti tanda koma di antara argumen dengan titik koma. Pemisah argumen mengikuti pengaturan regional komputer: kalau pemisah desimal Anda berupa koma, Excel biasanya memakai titik koma sebagai pemisah argumen.

## Ringkasan

- SUMIF menjumlahkan angka dengan syarat, misalnya total barang keluar untuk satu SKU.
- VLOOKUP dan XLOOKUP mencari data dari tabel lain; di VLOOKUP, selalu isi FALSE di akhir.
- XLOOKUP lebih fleksibel, tapi tidak tersedia di Excel 2016 dan 2019.
- Pivot table merangkum ribuan baris jadi laporan ringkas; jangan lupa Refresh setelah data berubah.
- Belajar satu rumus dulu, langsung dengan data kerja Anda sendiri.
