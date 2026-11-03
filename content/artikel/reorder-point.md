---
id: L21
slug: reorder-point
judul: "Reorder Point: Kapan Harus Pesan Barang Lagi?"
seo_title: "Reorder Point Adalah: Rumus, Contoh, dan Cara Hitung"
deskripsi: "Reorder point adalah batas stok yang menandakan waktunya pesan ulang. Pelajari rumus pemakaian x lead time + safety stock, contoh hitung, dan kesalahannya."
kategori: kamus-logistik
kata_kunci: ["reorder point adalah", "rumus reorder point", "cara menghitung reorder point", "contoh reorder point", "titik pemesanan ulang", "ROP adalah", "kapan harus pesan barang lagi", "reorder point dan lead time"]
terbit: 2026-11-04
intinya: "Reorder point = **pemakaian harian x lead time + safety stock**. Begitu stok menyentuh angka ini, saatnya memesan, bukan menunggu stok habis."
faq:
  - q: "Apa itu reorder point?"
    a: "Reorder point (ROP) atau titik pemesanan ulang adalah tingkat stok yang menjadi tanda untuk memesan barang lagi. Begitu stok turun sampai angka ini, pesanan dibuat. Sisa stok yang ada dipakai untuk melayani pesanan selama menunggu barang baru datang."
  - q: "Bagaimana rumus reorder point?"
    a: "Rumus dasarnya adalah pemakaian rata-rata per hari dikali lead time dalam hari, lalu ditambah safety stock. Bagian pertama adalah kebutuhan selama menunggu barang datang, bagian kedua adalah cadangan untuk kejutan. Hasilnya dinyatakan dalam unit, karton, atau satuan stok lain yang Anda pakai."
  - q: "Apa beda reorder point dan safety stock?"
    a: "Safety stock adalah jumlah cadangan untuk berjaga-jaga kalau permintaan naik atau pasokan terlambat. Reorder point adalah batas stok yang memicu pemesanan ulang. Safety stock adalah salah satu komponen di dalam rumus reorder point, jadi keduanya saling terkait tetapi tidak sama."
  - q: "Kapan reorder point harus dihitung ulang?"
    a: "Hitung ulang setiap kali pemakaian rata-rata atau lead time berubah cukup jauh, misalnya karena ganti pemasok, musim ramai, atau barang mulai kurang laku. Angka yang tidak diperbarui bisa membuat pesanan terlambat atau stok menumpuk. Selain itu, jadwalkan peninjauan berkala, misalnya setiap bulan atau setiap kuartal."
sumber:
  - judul: "Wikipedia, Reorder point"
    url: "https://en.wikipedia.org/wiki/Reorder_point"
    catatan: "Definisi 'the level of inventory which triggers an action to replenish that particular inventory'; dihitung sebagai pemakaian selama lead time ditambah safety stock; rumus 'Reorder level = Average daily usage rate x lead-time in days'; lead time lebih panjang menaikkan reorder point; reorder point selalu di atas nol karena lead time tidak pernah nol; safety stock lebih besar menurunkan risiko kehabisan tapi menaikkan biaya simpan."
  - judul: "Farhana, Yahya & Mubarok (2025), Analisis Safety Stock dan Reorder Point Persediaan Produk Wheel-Grinding 4\" di PT XYZ, JATRI Jurnal Teknik Industri 3(1)"
    url: "https://e-journals2.unmul.ac.id/index.php/jatri/article/download/2304/1036/8949"
    catatan: "ROP sebagai kondisi saat perusahaan wajib melakukan pemesanan; rumus ROP = safety stock + (lead time x pemakaian rata-rata per hari); lead time sebagai jeda waktu antara pemesanan dan penerimaan barang."
  - judul: "IBM Think, Apa itu stok pengaman?"
    url: "https://www.ibm.com/id-id/think/topics/safety-stock"
    catatan: "Rumus titik pemesanan ulang (ROP) memakai jumlah stok pengaman dan variabel lain untuk menentukan waktu produk baru harus dipesan agar tidak kehabisan."
---
Reorder point adalah batas stok yang menandakan bahwa sudah waktunya memesan barang lagi. Rumus dasarnya: pemakaian rata-rata per hari dikali lead time, lalu ditambah safety stock. Begitu stok di gudang turun sampai angka itu, pesanan ulang dibuat, jadi barang baru datang sebelum stok habis.

Artikel ini versi lengkap dari video 60 detik Ngerti Logistik tentang reorder point.

## Reorder point adalah titik pemesanan ulang

Reorder point sering disingkat ROP. Dalam bahasa Indonesia biasa disebut titik pemesanan ulang atau titik pemesanan kembali. Wikipedia mendefinisikannya sebagai tingkat persediaan yang memicu tindakan untuk mengisi ulang persediaan tersebut. Sebuah studi di JATRI Jurnal Teknik Industri (2025) menyebut ROP sebagai kondisi ketika perusahaan wajib melakukan pemesanan.

Intinya sederhana: jangan menunggu stok habis untuk memesan. Barang yang dipesan hari ini tidak datang hari ini. Ada jeda waktu, dan selama jeda itu gudang tetap harus melayani pesanan. Reorder point memastikan sisa stok cukup untuk menutup masa tunggu tersebut.

## Kenapa tidak pesan saat stok habis saja?

Bayangkan Anda baru memesan ketika rak sudah kosong. Selama menunggu kiriman pemasok, setiap pesanan pelanggan untuk barang itu tidak bisa dipenuhi. Pesanan tertunda, dibatalkan, atau pelanggan pindah ke penjual lain.

Sebaliknya, kalau Anda memesan terlalu cepat dan terlalu sering, barang menumpuk. Uang tertahan di gudang dan biaya simpan naik. Masalah ini dibahas di artikel [dampak overstock](L11).

Reorder point berada di tengah: pesan tidak terlalu cepat, tidak terlalu lambat.

## Rumus reorder point

Rumus dasarnya adalah:

**Reorder point = (pemakaian rata-rata per hari x lead time dalam hari) + safety stock**

Rumus yang sama dipakai dalam studi JATRI tadi, dan Wikipedia menjelaskan bahwa reorder point dihitung dari pemakaian selama lead time ditambah safety stock. Mari bedah tiap komponennya.

### Pemakaian rata-rata per hari

Berapa unit barang yang keluar dari gudang per hari, dihitung dari data beberapa minggu atau bulan terakhir. Pakai satuan yang sama dengan satuan stok Anda, misalnya karton atau pcs.

### Lead time

[Lead time](L13) adalah waktu dari pesanan dibuat sampai barang diterima dan siap dipakai. Bukan hanya lama perjalanan truk, tapi juga waktu pemasok memproses pesanan dan waktu gudang menerima barang. Wikipedia mencatat bahwa makin panjang lead time, makin tinggi reorder point. Masuk akal, karena masa tunggunya lebih lama.

### Safety stock

[Safety stock](L19) adalah cadangan untuk berjaga-jaga kalau pemakaian tiba-tiba naik atau barang datang terlambat. Tanpa safety stock, reorder point hanya cukup kalau semuanya berjalan persis sesuai rencana. IBM juga menyebut rumus titik pemesanan ulang memakai jumlah stok pengaman sebagai salah satu variabelnya.

## Contoh hitung reorder point

Angka di bawah ini adalah ilustrasi, bukan data nyata.

> **CONTOH** Sebuah barang dipakai rata-rata 10 karton per hari. Lead time dari pemasok 5 hari. Safety stock yang ditetapkan 20 karton.
>
> 1. Kebutuhan selama menunggu: 10 karton x 5 hari = 50 karton.
> 2. Ditambah safety stock: 50 + 20 = **70 karton**.
>
> Artinya, begitu stok tinggal 70 karton, saatnya membuat pesanan.

Apa yang terjadi setelah pesanan dibuat? Selama 5 hari menunggu, gudang memakai sekitar 50 karton. Saat barang baru datang, stok tersisa kira-kira 20 karton, yaitu safety stock-nya. Kalau ada kejutan, misalnya pemakaian lebih tinggi dari biasanya, cadangan 20 karton itulah yang menolong.

### Bagaimana kalau angkanya berubah?

Dengan ilustrasi yang sama, lihat bagaimana reorder point bergeser:

| Kondisi | Hitungan | Reorder point |
|---|---|---|
| Normal | 10 x 5 + 20 | 70 karton |
| Lead time naik jadi 7 hari | 10 x 7 + 20 | 90 karton |
| Pemakaian naik jadi 14 karton per hari | 14 x 5 + 20 | 90 karton |
| Pemakaian turun jadi 6 karton per hari | 6 x 5 + 20 | 50 karton |

Pelajarannya: reorder point bukan angka abadi. Kalau pemakaian atau lead time berubah, angkanya ikut berubah.

## Cara menerapkan reorder point di gudang

1. **Tentukan per SKU.** Setiap barang punya pola pemakaian dan lead time sendiri. Reorder point dihitung untuk tiap SKU, bukan disamaratakan.
2. **Kumpulkan data pemakaian.** Ambil catatan barang keluar beberapa periode terakhir, lalu hitung rata-rata hariannya.
3. **Catat lead time nyata.** Pakai riwayat kedatangan barang dari pemasok, bukan janji di atas kertas.
4. **Tetapkan safety stock.** Sesuaikan dengan seberapa sering pemakaian dan lead time meleset.
5. **Pasang tanda di sistem atau di rak.** Kalau sistem stok Anda punya fitur peringatan stok minimum, isi reorder point di sana. Di gudang kecil, kartu stok atau label batas di rak juga bisa dipakai.
6. **Tinjau ulang berkala.** Jadwalkan pengecekan rutin, dan hitung ulang saat ada perubahan besar seperti ganti pemasok atau musim ramai.

## Kesalahan umum saat memakai reorder point

- **Memakai transit time, bukan lead time.** Lama perjalanan barang hanya sebagian dari lead time. Kalau yang dipakai hanya transit time, reorder point jadi terlalu rendah dan barang telat datang.
- **Tidak memasukkan safety stock.** Rumus tanpa safety stock hanya aman kalau semuanya tepat waktu. Di lapangan, hal itu jarang terjadi.
- **Angka tidak pernah diperbarui.** Reorder point dihitung sekali, lalu dibiarkan bertahun-tahun padahal pola pemakaian sudah berubah.
- **Catatan stok tidak akurat.** Reorder point membaca angka stok di sistem. Kalau stok di sistem lebih besar dari stok fisik, tanda pesan ulang tidak pernah muncul tepat waktu. Penyebab selisih seperti ini dibahas di artikel [selisih stok gudang](L14).
- **Lupa stok yang sudah dipesan.** Kalau pesanan sebelumnya masih di jalan, jangan memesan lagi hanya karena stok fisik menyentuh reorder point. Cek dulu pesanan yang belum datang.

## Reorder point menjawab "kapan", bukan "berapa banyak"

Reorder point hanya memberi tahu waktu memesan. Berapa banyak yang dipesan adalah keputusan terpisah, yang biasanya mempertimbangkan biaya pesan, kapasitas gudang, minimal order dari pemasok, dan risiko barang kedaluwarsa. Memisahkan dua pertanyaan ini membantu Anda berpikir lebih jernih: kapan pesan diatur oleh reorder point, jumlah pesanan diatur oleh kebijakan pembelian.

## Ringkasan

- Reorder point adalah batas stok yang menandakan saatnya memesan ulang.
- Rumus dasar: pemakaian rata-rata per hari x lead time + safety stock.
- Sisa stok di titik itu cukup untuk dipakai selama menunggu barang baru datang.
- Hitung per SKU dan perbarui saat pemakaian atau lead time berubah.
- Reorder point menjawab kapan memesan; jumlah pesanan diputuskan terpisah.
