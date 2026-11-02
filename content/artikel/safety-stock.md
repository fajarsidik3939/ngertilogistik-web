---
id: L19
slug: safety-stock
judul: "Safety Stock (Stok Pengaman): Cadangan Supaya Stok Tidak Habis"
seo_title: "Safety Stock Adalah: Arti Stok Pengaman dan Cara Hitung"
deskripsi: "Safety stock adalah stok cadangan saat permintaan naik atau pasokan telat. Pelajari faktor penentunya, rumus sederhana, dan contoh hitungnya untuk gudang."
kategori: kamus-logistik
kata_kunci: ["safety stock adalah", "stok pengaman", "rumus safety stock", "cara menghitung safety stock", "contoh safety stock", "safety stock dan reorder point", "buffer stock"]
terbit: 2026-11-02
intinya: "Safety stock = **cadangan untuk permintaan atau pasokan yang meleset** dari rencana. Bukan stok nganggur, tapi asuransi supaya pelanggan tetap terlayani."
faq:
  - q: "Apa itu safety stock?"
    a: "Safety stock atau stok pengaman adalah persediaan tambahan yang disimpan untuk mengurangi risiko kehabisan barang. Cadangan ini dipakai saat permintaan naik di luar perkiraan atau saat pasokan datang terlambat. Tanpa safety stock, stok bisa habis sebelum kiriman baru tiba."
  - q: "Bagaimana cara menghitung safety stock?"
    a: "Cara paling sederhana memakai rumus rata-rata-maksimum: (pemakaian harian maksimum x lead time maksimum) dikurangi (pemakaian harian rata-rata x lead time rata-rata). Datanya diambil dari catatan pemakaian dan riwayat kedatangan barang per SKU. Ada juga rumus statistik dengan Z-skor untuk perhitungan yang lebih rinci."
  - q: "Apa bedanya safety stock dan reorder point?"
    a: "Safety stock adalah jumlah cadangan, sedangkan reorder point adalah batas stok yang menandakan kapan harus memesan ulang. Keduanya berhubungan karena perhitungan reorder point memakai jumlah safety stock bersama variabel lain, seperti pemakaian selama lead time. Reorder point akan dibahas di artikel tersendiri."
  - q: "Apakah safety stock sama dengan buffer stock?"
    a: "Dalam banyak pemakaian sehari-hari, keduanya dianggap mirip. Artikel IBM berbahasa Indonesia, misalnya, menyebut stok pengaman sebagai persediaan penyangga. Sebagian literatur membedakan keduanya berdasarkan tujuan dan cara hitungnya, jadi pastikan Anda memakai definisi yang sama dengan tim Anda."
sumber:
  - judul: "IBM Think, Apa itu stok pengaman?"
    url: "https://www.ibm.com/id-id/think/topics/safety-stock"
    catatan: "Definisi 'Stok pengaman adalah inventaris tambahan dari barang yang disimpan untuk mengurangi risiko kehabisan stok barang'; 'persediaan penyangga yang disimpan selain stok siklus'; rumus rata-rata-maks (pemakaian harian maks x waktu tunggu maks) - (pemakaian harian rata-rata x waktu tunggu rata-rata) yang tidak memperhitungkan variabilitas permintaan; rumus Z-skor x σLT x Davg; ROP memakai jumlah stok pengaman dan variabel lain; stok pengaman berlebih meningkatkan biaya dan bisa berujung penurunan harga atau likuidasi; penyebab kebutuhan: peningkatan permintaan, gangguan rantai pasokan, kesalahan perkiraan."
---
Safety stock adalah stok cadangan yang sengaja disimpan untuk berjaga-jaga kalau permintaan atau pasokan meleset dari rencana. Dalam bahasa Indonesia, safety stock disebut stok pengaman. Cadangan ini menjaga agar barang tidak habis sebelum kiriman berikutnya datang.

Artikel ini versi lengkap dari video 60 detik Ngerti Logistik tentang safety stock.

## Safety stock adalah...

IBM, dalam artikel berbahasa Indonesia, mendefinisikan stok pengaman sebagai "inventaris tambahan dari barang yang disimpan untuk mengurangi risiko kehabisan stok barang". Artikel yang sama menyebutnya sebagai persediaan penyangga yang disimpan selain stok siklus.

Bayangkan stok di gudang terbagi dua:

- **Stok siklus (stok jalan):** stok yang memang dipakai sehari-hari dan habis sebelum barang baru datang.
- **Safety stock:** lapisan cadangan di bawahnya, yang baru tersentuh kalau ada kejutan.

Kalau semuanya berjalan sesuai rencana, safety stock nyaris tidak terpakai. Ia bekerja justru ketika rencana meleset.

## Kenapa gudang butuh safety stock

IBM menyebut beberapa penyebab bisnis membutuhkan stok pengaman, di antaranya peningkatan permintaan, gangguan rantai pasokan, dan kesalahan perkiraan. Dua yang paling sering terasa di gudang adalah berikut.

### Permintaan melonjak (promo, musim ramai)

Pembeli tiba-tiba memesan jauh lebih banyak dari biasanya karena promo, musim ramai, atau tren. Tanpa cadangan, stok habis lebih cepat dari jadwal pemesanan ulang.

### Pasokan terlambat

Truk pemasok datang terlambat, produksi pemasok tertunda, atau pengiriman tertahan di jalan. Selama menunggu, gudang tetap harus melayani pesanan. Safety stock yang menutup celah itu.

## Apa yang menentukan besarnya safety stock

Besarnya safety stock tidak ditebak. Ada tiga faktor utama:

1. **Naik-turunnya permintaan.** Makin tidak stabil pemakaian harian, makin besar cadangan yang dibutuhkan.
2. **Lama dan ketidakpastian lead time.** [Lead time](L13) adalah waktu dari memesan sampai barang siap dipakai. Makin panjang dan makin sering meleset, makin besar cadangannya.
3. **Target layanan.** Seberapa jarang Anda mau kehabisan stok. Target yang lebih tinggi membutuhkan cadangan yang lebih besar.

Karena faktor-faktor ini berbeda untuk tiap barang, safety stock sebaiknya dihitung [per SKU](L03), bukan disamaratakan.

## Rumus sederhana dan contoh hitungnya

### Rumus rata-rata-maksimum

Rumus yang paling mudah dipahami pemula adalah rumus rata-rata-maksimum, seperti yang dimuat IBM:

**Safety stock = (pemakaian harian maksimum x lead time maksimum) − (pemakaian harian rata-rata x lead time rata-rata)**

Logikanya sederhana. Bagian pertama adalah kebutuhan pada skenario terburuk: pemakaian sedang tinggi dan barang datang paling lambat. Bagian kedua adalah kebutuhan pada kondisi normal. Selisihnya adalah cadangan yang perlu disiapkan.

Perlu dicatat, IBM menyebut rumus ini memperhitungkan variasi waktu tunggu, tetapi tidak memperhitungkan variasi permintaan secara statistik. Untuk awal belajar, rumus ini sudah cukup memberi gambaran.

### Contoh hitung langkah demi langkah

Angka di bawah ini adalah ilustrasi, bukan data nyata.

> **CONTOH** Sebuah SKU punya data berikut: pemakaian harian rata-rata 10 unit, pemakaian harian tertinggi 15 unit, lead time rata-rata 10 hari, dan lead time terlama 12 hari.
>
> 1. Skenario terburuk: 15 unit x 12 hari = 180 unit.
> 2. Kondisi normal: 10 unit x 10 hari = 100 unit.
> 3. Safety stock: 180 − 100 = **80 unit**.

Artinya, gudang menyimpan 80 unit di atas kebutuhan normal selama lead time, untuk berjaga-jaga kalau pemakaian sedang tinggi dan barang datang terlambat.

## Sekilas rumus statistik (untuk yang ingin lebih dalam)

Bagian ini tidak wajib dipahami pemula. Perusahaan yang datanya sudah rapi sering memakai rumus berbasis statistik. Salah satu versi yang dimuat IBM adalah Z-skor x deviasi standar lead time x permintaan rata-rata. Z-skor mewakili target layanan, sedangkan deviasi standar mengukur seberapa jauh data biasanya menyimpang dari rata-rata. Ada beberapa variasi rumus statistik, dan pilihannya tergantung variabel mana yang paling tidak pasti.

## Terlalu kecil vs terlalu besar

| Kondisi | Akibat |
|---|---|
| Terlalu kecil | Stok mudah habis saat ada lonjakan atau keterlambatan. Pesanan tertunda dan pelanggan kecewa. |
| Terlalu besar | Uang tertahan di gudang, biaya simpan naik, dan barang berisiko rusak atau kedaluwarsa. |

IBM mencatat bahwa stok pengaman yang terlalu banyak meningkatkan biaya, dan di ritel kelebihan persediaan bisa berujung pada penurunan harga atau likuidasi stok. Penjelasan lebih lengkap ada di artikel [dampak overstock](L11).

## Safety stock bukan stok nganggur

Ada anggapan bahwa safety stock adalah barang yang "diam saja" di gudang. Sebenarnya safety stock adalah asuransi. Ia memang tidak terpakai setiap hari, tapi melindungi pelanggan saat kondisi meleset.

Beberapa prinsip penggunaannya:

- **Boleh dipakai saat dibutuhkan.** Itulah gunanya. Kalau permintaan melonjak atau pasokan telat, pakai cadangannya.
- **Segera isi ulang.** Setelah terpakai, pastikan pesanan berikutnya mengembalikan cadangan ke tingkat semula.
- **Tetap dirotasi.** Untuk barang berkedaluwarsa, safety stock tetap ikut aturan keluar-masuk, supaya cadangan tidak membusuk di rak.
- **Tinjau ulang berkala.** Pola permintaan dan lead time berubah. Angka yang tepat tahun lalu belum tentu tepat sekarang.

Safety stock juga hanya berguna kalau catatan stoknya benar. Tanpa [akurasi stok](L14), Anda bisa merasa punya cadangan padahal barangnya tidak ada.

## Kesalahan umum

- **Memakai transit time, bukan lead time.** Transit time hanya waktu perjalanan. Lead time mencakup juga proses pesan, produksi pemasok, dan penerimaan di gudang.
- **Menyamaratakan semua SKU.** Barang laris dan barang lambat butuh cadangan yang berbeda.
- **Tidak pernah ditinjau.** Angka dihitung sekali, lalu dibiarkan bertahun-tahun.
- **Menganggap safety stock tidak boleh disentuh.** Akibatnya pelanggan kehabisan barang padahal cadangannya ada.

## Ringkasan

- Safety stock adalah stok cadangan untuk berjaga-jaga saat permintaan naik atau pasokan terlambat.
- Besarnya ditentukan oleh naik-turunnya permintaan, lama dan ketidakpastian lead time, serta target layanan.
- Rumus sederhana: (pemakaian maksimum x lead time maksimum) − (pemakaian rata-rata x lead time rata-rata).
- Terlalu kecil membuat stok mudah habis; terlalu besar membuat uang tertahan.
- Lanjutkan ke artikel [lead time](L13) karena angka ini menjadi bahan utama perhitungan safety stock.
