---
id: L13
slug: lead-time-vs-transit-time
judul: "Lead Time vs Transit Time: Jangan Sampai Stok Habis karena Salah Hitung"
seo_title: "Lead Time vs Transit Time: Bedanya dan Cara Menghitung"
deskripsi: "Lead time dan transit time sering tertukar, padahal bedanya bisa bikin stok habis. Pahami komponen lead time, contoh hitung, dan cara mengukurnya sendiri."
kategori: kamus-logistik
kata_kunci: ["lead time adalah", "perbedaan lead time dan transit time", "transit time adalah", "cara menghitung lead time", "komponen lead time", "lead time pemasok", "lead time pengiriman"]
terbit: 2026-11-02
intinya: "**Transit time** = waktu barang di jalan. **Lead time** = dari pesanan dibuat sampai barang siap dipakai. Rencanakan stok dengan lead time."
faq:
  - q: "Apa perbedaan lead time dan transit time?"
    a: "Transit time adalah waktu barang di perjalanan, dari dikirim sampai tiba. Lead time lebih panjang, yaitu dari pesanan dibuat sampai barang siap dipakai atau dijual. Transit time hanyalah salah satu bagian dari lead time."
  - q: "Bagaimana cara menghitung lead time?"
    a: "Catat tanggal pesanan (PO) dibuat dan tanggal barang selesai dicek di gudang dan siap dipakai, lalu hitung selisih harinya. Lakukan untuk beberapa pesanan terakhir dari pemasok yang sama. Dari situ, lihat rata-ratanya dan yang paling lama, lalu perbarui angkanya secara berkala."
  - q: "Apa saja komponen lead time?"
    a: "Secara sederhana, lead time terdiri dari waktu proses pesanan, waktu produksi atau penyiapan barang, waktu pengiriman (transit), dan waktu penerimaan serta pengecekan di gudang. Setiap komponen bisa molor, jadi semuanya perlu dihitung, bukan hanya waktu di jalan."
  - q: "Apa arti lead time dalam pengiriman barang?"
    a: "Dalam pengiriman, lead time adalah total waktu dari pesanan dibuat sampai barang diterima dan siap dipakai. Angka yang sering dijanjikan penyedia jasa kirim, misalnya dua atau tiga hari, biasanya adalah transit time. Untuk perencanaan stok, Anda perlu lead time yang lengkap."
sumber:
  - judul: "Taufiqur Rachman, EMA402 Manajemen Rantai Pasokan #4: Konsep Lead Time SCM (Universitas Esa Unggul)"
    url: "https://digilib.esaunggul.ac.id/public/UEU-paper-6492-EMA402-4-Konsep-Lead-Time-SCM.pdf"
    catatan: "Lead time: waktu yang diperlukan dari proses awal pemesanan sampai barang diterima oleh pemesan; komponen order to delivery cycle meliputi proses pemesanan, pencatatan pesanan, pembuatan/penyiapan barang, dan pengangkutan."
  - judul: "IBM Think: Apa itu Stok Pengaman?"
    url: "https://www.ibm.com/id-id/think/topics/safety-stock"
    catatan: "Rumus rata-rata-maks stok pengaman: (penggunaan harian maksimum × waktu tunggu maksimum) - (penggunaan harian rata-rata × waktu tunggu rata-rata)."
---
Lead time adalah total waktu dari pesanan dibuat sampai barang siap dipakai. Transit time adalah waktu barang di perjalanan, dari dikirim sampai tiba. Keduanya sering tertukar, padahal kalau Anda merencanakan stok dengan transit time, stok bisa habis sebelum barang baru datang.

## Lead time vs transit time dalam satu kalimat

**Transit time** adalah waktu di jalan, sedangkan **lead time** adalah waktu dari pesan sampai siap pakai. Transit time hanya satu potongan di dalam lead time.

| | Transit time | Lead time |
|---|---|---|
| Mulai dihitung | Saat barang dikirim | Saat pesanan dibuat |
| Selesai dihitung | Saat barang tiba | Saat barang siap dipakai atau dijual |
| Yang dicakup | Perjalanan saja | Proses pesanan, penyiapan, perjalanan, penerimaan |
| Dipakai untuk | Memilih layanan kirim | Merencanakan kapan pesan ulang |

## Apa itu transit time?

Transit time adalah lama barang berada di perjalanan. Hitungannya dimulai ketika barang diserahkan ke pengangkut dan berakhir ketika barang tiba di tujuan. Angka "estimasi 2 sampai 3 hari" yang Anda lihat saat memilih layanan kirim biasanya adalah transit time.

Transit time dipengaruhi jarak, moda transportasi, dan berapa kali barang singgah. Paket yang singgah di beberapa titik pemilahan bisa lebih lama, seperti dibahas di artikel tentang [transit di hub kurir](L18).

## Lead time adalah waktu dari pesan sampai siap pakai

Dalam materi kuliah manajemen rantai pasok Universitas Esa Unggul, lead time dijelaskan sebagai waktu yang diperlukan dari proses awal pemesanan sampai barang diterima oleh pemesan. Dalam praktik gudang, saya menghitungnya sampai barang benar-benar siap dipakai, karena barang yang baru tiba belum tentu bisa langsung dijual. Ada empat komponen utama.

### Waktu proses pesanan

Pesanan Anda perlu diterima, dicek, dan disetujui oleh pemasok. Kadang menunggu konfirmasi harga, ketersediaan, atau pembayaran.

### Waktu produksi atau penyiapan

Kalau barangnya ada di gudang pemasok, tinggal disiapkan dan dikemas. Kalau harus dibuat dulu, waktunya bisa jauh lebih lama.

### Waktu pengiriman (transit)

Inilah transit time: barang di jalan, dari gudang pemasok ke gudang Anda.

### Waktu penerimaan dan pengecekan

Barang yang tiba perlu dibongkar, dihitung, dicek kondisinya, dan dicatat sebelum boleh dijual. Bagian ini sering dilupakan. Pelajari lebih lanjut soal [waktu penerimaan barang](L08) di gudang.

## Contoh: kirim 3 hari, tapi lead time 10 hari

Ilustrasi berikut fiktif, untuk menunjukkan selisihnya.

> **CONTOH** Anda memesan barang hari Senin. Garis waktunya:
> - Hari 1 sampai 2: pemasok memproses pesanan dan menunggu konfirmasi pembayaran.
> - Hari 3 sampai 6: barang disiapkan dan dikemas.
> - Hari 7 sampai 9: barang di perjalanan (transit time 3 hari).
> - Hari 10: barang dibongkar, dicek, dan dicatat, lalu siap dijual.
>
> Pemasok bilang "kirim 3 hari", tapi lead time sebenarnya 10 hari.

Kalau Anda memesan ulang dengan anggapan barang datang dalam 3 hari, ada 7 hari ketika stok bisa habis sementara barang baru belum siap.

## Kenapa pesan ulang harus memakai lead time

Titik pesan ulang pada dasarnya menjawab satu pertanyaan: berapa stok yang dibutuhkan selama menunggu barang baru siap? Jawabannya adalah rata-rata pemakaian per hari dikali lead time.

Lead time juga dipakai untuk menghitung [safety stock](L19), yaitu cadangan untuk berjaga dari lonjakan permintaan atau keterlambatan. Salah satu rumus yang dijelaskan IBM memakai selisih antara pemakaian harian maksimum dikali waktu tunggu maksimum, dengan pemakaian harian rata-rata dikali waktu tunggu rata-rata. Artinya, makin tidak menentu lead time pemasok, makin besar cadangan yang dibutuhkan.

Sebaliknya, kalau lead time ditaksir terlalu panjang, Anda memesan terlalu awal dan terlalu banyak. Ini membawa [risiko stok berlebih](L11).

## Cara mengukur lead time pemasok sendiri

Anda tidak perlu software khusus untuk mulai. Tabel sederhana sudah cukup.

### Catat tanggal PO dan tanggal barang siap pakai

Untuk setiap pesanan, catat dua tanggal: saat pesanan (PO) dikirim ke pemasok, dan saat barang selesai dicek dan siap dipakai. Selisihnya adalah lead time pesanan itu.

### Hitung rata-rata dan yang terlama

Setelah terkumpul beberapa pesanan, hitung rata-ratanya. Catat juga lead time terlama, karena angka ini yang menentukan seberapa besar risiko Anda kehabisan stok.

### Perbarui berkala

Lead time bisa berubah, misalnya menjelang hari raya, saat pemasok ganti gudang, atau saat cuaca buruk. Tinjau ulang angkanya secara berkala dan pisahkan per pemasok.

Berikut ilustrasi tabel pencatatannya. Angkanya fiktif.

> **CONTOH** Catatan 4 pesanan terakhir dari satu pemasok:
>
> | Pesanan | Tanggal PO | Tanggal siap pakai | Lead time |
> |---|---|---|---|
> | 1 | 2 Agustus | 11 Agustus | 9 hari |
> | 2 | 16 Agustus | 26 Agustus | 10 hari |
> | 3 | 1 September | 9 September | 8 hari |
> | 4 | 15 September | 28 September | 13 hari |
>
> Rata-ratanya (9 + 10 + 8 + 13) ÷ 4 = 10 hari. Lead time terlamanya 13 hari. Kalau Anda hanya memakai angka rata-rata, pesanan seperti nomor 4 tetap bisa membuat stok habis. Di sinilah safety stock berperan.

Dari tabel seperti ini, Anda juga bisa melihat pola. Misalnya, apakah pesanan yang dibuat di akhir bulan selalu lebih lama, atau apakah satu pemasok jauh lebih stabil dari yang lain.

## Pertanyaan yang perlu diajukan ke pemasok

Saat pemasok menyebut "kirim 3 hari", ajukan pertanyaan berikut:

- Berapa hari pesanan diproses sebelum barang disiapkan?
- Apakah barang tersedia di gudang, atau harus diproduksi dulu?
- Kapan barang biasanya diserahkan ke pengangkut setelah pesanan dikonfirmasi?
- Berapa lama transit time ke lokasi saya?
- Apakah ada masa tertentu ketika waktu proses lebih lama?

## Kesalahan umum

- **Memakai janji transit time sebagai lead time.** Ini kesalahan paling sering dan paling cepat membuat stok habis.
- **Tidak menghitung waktu cek di gudang.** Barang yang sudah tiba tapi belum dicatat belum bisa dijual.
- **Memakai satu angka untuk semua pemasok.** Setiap pemasok punya kecepatan proses dan jarak yang berbeda.
- **Hanya memakai rata-rata.** Rata-rata menyembunyikan pesanan yang telat. Perhatikan juga lead time terlama.

## Ringkasan

- Lead time adalah waktu dari pesanan dibuat sampai barang siap dipakai; transit time hanya waktu di jalan.
- Komponen lead time: proses pesanan, penyiapan atau produksi, transit, serta penerimaan dan pengecekan.
- Rencanakan pesan ulang dan safety stock dengan lead time, bukan transit time.
- Ukur lead time per pemasok dari tanggal PO sampai barang siap pakai, lalu perbarui berkala.
- Lanjutkan dengan membaca cara menentukan safety stock.
