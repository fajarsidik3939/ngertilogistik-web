---
id: L14
slug: selisih-stok-gudang
judul: "Stok di Sistem Beda dengan di Rak? Ini Penyebab Selisih Stok"
seo_title: "Selisih Stok Gudang: Penyebab dan Cara Mengatasinya"
deskripsi: "Stok di sistem beda dengan di rak? Kenali 4 penyebab selisih stok gudang, cara menelusurinya, dan cara memulai cycle count agar akurasi stok terjaga."
kategori: manajemen-gudang
kata_kunci: ["selisih stok gudang", "stok fisik dan sistem berbeda", "penyebab selisih stok", "cycle count adalah", "akurasi stok gudang", "inventory discrepancy", "phantom inventory", "cara mengatasi selisih stok"]
terbit: 2026-11-02
intinya: "Selisih stok kebanyakan berasal dari **pencatatan**, bukan barang hilang. Kuncinya: **scan setiap pergerakan saat itu juga** dan lakukan **cycle count**."
faq:
  - q: "Kenapa stok di sistem berbeda dengan stok fisik?"
    a: "Penyebab yang paling sering adalah pencatatan yang tidak sesuai kejadian di lapangan: barang dipindah lokasi tanpa dicatat, barang rusak atau retur tidak diinput, salah ambil varian saat picking, atau barang masuk dan keluar tanpa di-scan. Kehilangan karena pencurian memang bisa terjadi, tapi jangan langsung menyimpulkan itu sebelum pencatatannya ditelusuri."
  - q: "Apa itu cycle count?"
    a: "Cycle count adalah teknik audit akurasi persediaan dengan menghitung sebagian stok secara terjadwal dan bergiliran, bukan menghitung semuanya sekaligus setahun sekali. Hasil hitungan dibandingkan dengan catatan sistem, lalu setiap selisih dicari penyebabnya sebelum angkanya dikoreksi."
  - q: "Apa bedanya cycle count dan stock opname?"
    a: "Stock opname biasanya menghitung seluruh stok sekaligus, sering dengan menghentikan aktivitas gudang. Cycle count menghitung sebagian barang setiap hari atau setiap minggu secara bergiliran, sehingga operasional tetap berjalan dan selisih lebih cepat ketahuan."
  - q: "Bagaimana cara mengatasi selisih stok gudang?"
    a: "Telusuri dulu penyebabnya: cek lokasi di sekitar, varian yang mirip, transaksi terakhir, serta catatan retur dan barang rusak. Setelah penyebab ketemu, koreksi angkanya dan perbaiki prosesnya, misalnya dengan mewajibkan scan di setiap pergerakan barang. Lalu jalankan cycle count rutin agar selisih berikutnya cepat terdeteksi."
sumber:
  - judul: "Wijaya & Febrianti (2024), Evaluasi Kebijakan Cycle Count Inventory Menggunakan Metode Cycle Counting, Manajemen IKM 19(1)"
    url: "https://journal.ipb.ac.id/index.php/jurnalmpi/article/view/56445/28309"
    catatan: "Cycle counting sebagai teknik audit akurasi persediaan dengan siklus terjadwal, bukan sekali setahun; penyebab inventory record inaccuracy: shrinkage, spoilage, misplaced inventory, transaction errors; pengelompokan ABC berdasarkan perbandingan nilai barang."
  - judul: "Setijadi (2015), Fungsi dan Aktivitas Pergudangan (Warehousing), Supply Chain Indonesia"
    url: "https://ftp.idu.ac.id/wp-content/uploads/ebook/ip/LOGISTIK/SCM/5._Fungsi_dan_Aktivitas_Pergudangan_2015.pdf"
    catatan: "Definisi put away (penempatan barang pada lokasi penyimpanan) dan picking (penyiapan barang sesuai surat pesanan)."
---
Selisih stok gudang terjadi ketika jumlah barang di sistem berbeda dengan jumlah di rak. Penyebabnya kebanyakan bukan barang hilang, tapi pencatatan: barang dipindah lokasi tanpa dicatat, barang rusak atau retur tidak diinput, salah ambil varian, dan barang keluar-masuk tanpa di-scan.

## Jawaban singkat: kebanyakan selisih berasal dari pencatatan

Bayangkan sistem mencatat 10 unit, tapi di rak hanya ada 7. Reaksi pertama biasanya "barangnya hilang". Padahal sering kali barangnya masih ada di gudang, hanya catatannya yang tidak mengikuti kejadian sebenarnya.

Sebuah studi di jurnal Manajemen IKM IPB mengelompokkan penyebab ketidakakuratan catatan stok menjadi empat: shrinkage (barang berkurang, misalnya karena dicuri atau rusak), spoilage (kerusakan barang), misplaced inventory (barang ada di gudang tapi tidak ditemukan di lokasi simpannya), dan transaction errors (salah catat jumlah saat barang masuk dan keluar). Dua kelompok terakhir murni soal pencatatan dan penempatan.

## 4 penyebab selisih stok yang paling sering

### Barang dipindah lokasi tanpa dicatat

Barang digeser ke rak lain karena raknya penuh, atau ditaruh sementara di dekat area kemas. Sistem masih mencatat lokasi lama. Saat dicari di lokasi lama, barang "tidak ada". Inilah yang disebut misplaced inventory. Kebiasaan [mencatat lokasi saat putaway](L16), yaitu saat barang ditempatkan ke lokasi simpan, adalah pencegahan pertamanya.

### Barang rusak atau retur tidak diinput

Barang pecah dipisahkan ke pojok, atau barang retur dari pelanggan ditumpuk menunggu dicek. Kalau tidak dicatat, sistem masih menganggap barang rusak itu siap jual, atau barang retur belum masuk ke stok.

### Salah ambil saat picking

Picking adalah proses mengambil barang dari rak sesuai pesanan. Kalau varian tertukar, misalnya ukuran M terambil padahal yang dipesan ukuran L, dua catatan langsung salah sekaligus: stok M di sistem terlalu banyak, stok L terlalu sedikit. Memahami [SKU dan varian](L03) membantu mencegah salah ambil seperti ini.

### Barang masuk atau keluar tanpa di-scan

Barang dipinjam untuk foto produk, dikirim mendadak tanpa dokumen, atau diterima pemasok tanpa dicatat. Pergerakan fisiknya terjadi, tapi sistem tidak tahu.

## Dampaknya: pesanan diterima padahal barang tidak ada

Kalau sistem mencatat stok lebih banyak dari yang sebenarnya, toko atau tim penjualan akan menerima pesanan untuk barang yang tidak ada. Kondisi ini sering disebut phantom inventory: barangnya ada di sistem, tapi tidak ada di rak. Akibatnya pesanan dibatalkan, pelanggan kecewa, dan tim gudang membuang waktu mencari barang yang tidak ada.

Sebaliknya, kalau sistem mencatat stok lebih sedikit, Anda bisa memesan ulang barang yang sebenarnya masih ada. Ujungnya stok menumpuk tanpa disadari.

## Cara menelusuri selisih langkah demi langkah

Sebelum mengoreksi angka di sistem, telusuri dulu penyebabnya dengan daftar periksa ini:

1. **Cek lokasi di sekitar.** Lihat rak di atas, bawah, kiri, dan kanan, serta area transit dan area kemas.
2. **Cek varian yang mirip.** Apakah ada kelebihan di ukuran, warna, atau tipe yang mirip? Kalau iya, kemungkinan tertukar saat picking.
3. **Cek transaksi terakhir.** Lihat pergerakan barang beberapa hari terakhir: penerimaan, pengiriman, pindah lokasi. Cari yang janggal.
4. **Cek retur dan barang rusak.** Apakah ada barang di area karantina atau retur yang belum diinput?
5. **Catat penyebabnya.** Setelah ketemu, tulis penyebabnya. Catatan ini berharga untuk memperbaiki proses.

Ilustrasi berikut fiktif, untuk menunjukkan cara kerja daftar periksa ini.

> **CONTOH** Sistem mencatat 10 kaus ukuran L, tapi di rak hanya ada 7. Petugas mengecek rak di sekitarnya dan tidak menemukan apa-apa. Lalu ia mengecek varian mirip: ukuran M ternyata lebih 3 dari catatan sistem. Transaksi terakhir menunjukkan ada 3 pesanan ukuran M kemarin. Kesimpulannya, saat picking, kaus L terambil untuk pesanan M. Barangnya tidak hilang, hanya tertukar dan sudah terkirim ke pelanggan.

Dari contoh ini, perbaikannya bukan sekadar mengoreksi angka, tapi juga memeriksa kenapa ukuran L dan M bisa tertukar. Mungkin labelnya mirip, letaknya bersebelahan, atau picking tidak memakai scan.

## Cara mencegah: scan saat itu juga

Pencegahan paling efektif sederhana: setiap pergerakan barang dicatat atau di-scan saat itu juga, bukan nanti sore atau besok. Barang masuk, dipindah, diambil, dikirim, rusak, atau diretur, semuanya dicatat ketika terjadi.

Ini juga berarti tidak ada "jalan pintas" di [alur proses gudang](L04). Barang yang dipinjam sebentar tetap dicatat keluar. Barang yang dipindah sementara tetap dicatat lokasinya.

## Cycle count: hitung sebagian setiap hari

### Apa itu cycle count

Cycle count adalah teknik audit akurasi persediaan dengan menghitung sebagian stok secara terjadwal dan bergiliran. Jurnal Manajemen IKM IPB menekankan bahwa penghitungan dilakukan dengan siklus terjadwal, bukan hanya sekali setahun. Hasilnya, selisih ketemu lebih cepat, sehingga penyebabnya masih mudah dilacak.

### Cara memulai cycle count sederhana

1. Bagi seluruh lokasi atau SKU menjadi beberapa kelompok kecil.
2. Tentukan jadwal: setiap hari hitung satu kelompok.
3. Hitung saat barang tidak sedang bergerak, misalnya pagi sebelum picking dimulai.
4. Bandingkan hasil hitung dengan sistem.
5. Telusuri setiap selisih dengan daftar periksa di atas, baru koreksi angkanya.

### Barang mana yang dihitung lebih sering

Tidak semua barang perlu dihitung dengan frekuensi yang sama. Studi di jurnal IPB tadi memakai pengelompokan ABC berdasarkan perbandingan nilai tiap barang. Prinsip praktisnya: barang bernilai tinggi dan barang yang paling sering bergerak dihitung lebih sering, karena dampak selisihnya lebih besar dan peluang salah catatnya lebih tinggi. Anda bisa membaca [istilah cycle count](L20) bersama istilah gudang lain untuk memperkuat dasar.

## Kesalahan umum

- **Langsung menyesuaikan angka tanpa mencari penyebab.** Angka jadi benar hari ini, tapi selisih yang sama akan muncul lagi.
- **Menghitung saat barang sedang bergerak.** Barang yang sedang diambil atau baru diterima membuat hasil hitungan tidak bisa dibandingkan dengan sistem.
- **Menyalahkan orang, bukan proses.** Kalau staf takut disalahkan, selisih cenderung disembunyikan. Fokuslah pada celah di proses pencatatan.
- **Hanya menghitung saat stock opname tahunan.** Selisih yang menumpuk setahun jauh lebih sulit dilacak penyebabnya.

## Ringkasan

- Selisih stok gudang adalah beda antara jumlah di sistem dan di rak, dan kebanyakan berasal dari pencatatan.
- Empat penyebab umum: pindah lokasi tanpa dicatat, rusak atau retur tidak diinput, salah ambil varian, dan barang keluar-masuk tanpa scan.
- Telusuri penyebab dulu, baru koreksi angka.
- Cegah dengan scan setiap pergerakan saat itu juga, dan jalankan cycle count rutin.
- Akurasi stok bukan soal menghitung lebih sering, tapi mencatat dengan disiplin.
