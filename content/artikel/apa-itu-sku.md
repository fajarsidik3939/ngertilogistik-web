---
id: L03
slug: apa-itu-sku
judul: "SKU Itu Apa? Arti Stock Keeping Unit dan Contohnya di Gudang"
seo_title: "SKU Adalah: Arti Stock Keeping Unit dan Contohnya"
deskripsi: "SKU adalah kode untuk setiap varian barang yang dihitung terpisah. Pelajari arti stock keeping unit, contoh kode SKU, dan bedanya dengan barcode di sini."
kategori: kamus-logistik
kata_kunci: ["SKU adalah", "apa itu SKU", "stock keeping unit", "contoh kode SKU", "cara membuat kode SKU", "perbedaan SKU dan barcode", "SKU dan GTIN", "SKU di gudang"]
terbit: 2026-11-02
intinya: "Satu SKU = **satu varian** yang dihitung, disimpan, dan dijual terpisah. Stok selalu dihitung **per SKU**."
faq:
  - q: "Apa kepanjangan SKU?"
    a: "SKU adalah singkatan dari stock keeping unit. Dalam bahasa sehari-hari di gudang, SKU berarti kode untuk satu varian barang yang stoknya dihitung, disimpan, dan dijual terpisah. Barang yang berbeda isi, warna, ukuran, atau kemasan jualnya biasanya punya SKU sendiri."
  - q: "Apa bedanya SKU dan barcode?"
    a: "SKU biasanya kode internal yang dibuat sendiri oleh perusahaan atau toko untuk mengelola stok. Barcode adalah gambar garis yang bisa dipindai, dan pada produk ritel umumnya berisi GTIN, nomor global dari sistem GS1. Satu varian bisa punya SKU internal sekaligus GTIN di barcode-nya."
  - q: "Bagaimana cara membuat kode SKU?"
    a: "Buat kode yang unik untuk setiap varian, konsisten polanya, dan tanpa spasi. Susun dari bagian yang mudah dibaca, misalnya singkatan jenis barang, varian, lalu isi kemasan. Catat semua kode di satu daftar induk dan jangan memakai ulang kode lama untuk barang baru. Tidak ada format SKU baku yang berlaku untuk semua usaha."
  - q: "Apakah warna berbeda harus beda SKU?"
    a: "Umumnya ya, kalau warna itu disimpan, dihitung, dan dijual terpisah. Kalau warnanya tidak dibedakan, sistem tidak bisa tahu stok merah dan biru masing-masing, sehingga pembeli bisa menerima warna yang salah. Prinsip yang sama dipakai GS1 untuk GTIN: setiap ukuran, warna, dan kombinasinya butuh nomor sendiri."
sumber:
  - judul: "GS1 Support: How many GS1 GTINs do I need when I have a product with many sizes and colours?"
    url: "https://support.gs1.org/support/solutions/articles/43000734083-how-many-gs1-gtins-do-i-need-when-i-have-a-product-with-many-sizes-and-colours-"
    catatan: "'Each product variation needs its own GS1 GTIN': setiap ukuran, warna, dan kombinasi ukuran-warna dihitung sebagai variasi terpisah."
  - judul: "GS1 Support: What is a GS1 GTIN?"
    url: "https://support.gs1.org/support/solutions/articles/43000734120-what-is-a-gs1-gtin-"
    catatan: "GTIN adalah nomor yang terlihat di bawah barcode produk; unik, global, dan dapat diverifikasi dalam sistem GS1; kadang disebut U.P.C, EAN, atau barcode; hanya diterbitkan organisasi anggota GS1."
  - judul: "GS1 GTIN Management Standard: Declared net content"
    url: "https://gs1.org/1/gtinrules/en/rule/266/declared-net-content"
    catatan: "Perubahan (naik atau turun) isi bersih yang wajib dicantumkan di kemasan mengharuskan GTIN baru."
---
SKU adalah singkatan dari stock keeping unit, yaitu kode untuk setiap varian barang yang dihitung, disimpan, dan dijual terpisah. Jadi, kodenya bukan untuk jenis barang secara umum, melainkan untuk setiap varian. Masker isi 50 dan masker isi 20 adalah dua SKU berbeda.

Artikel ini versi lengkap dari video 60 detik "SKU itu apa?" di Ngerti Logistik. Kita bahas kenapa satu barang bisa punya banyak SKU, bedanya dengan barcode, dan cara membuat kode SKU sederhana.

![Ilustrasi SKU: satu jenis barang masker punya dua kode SKU berbeda untuk varian biru isi 50 dan biru isi 20 (contoh)](/img/ilustrasi/apa-itu-sku/1-satu-varian-satu-sku.webp){width="960" height="560" loading="lazy" style="border-radius:16px"}

## SKU adalah kode untuk setiap varian barang

Bayangkan rak gudang berisi masker merek yang sama. Ada yang isi 50, ada yang isi 20. Bagi pembeli, keduanya "masker". Bagi gudang, keduanya barang berbeda, karena jumlah stoknya dihitung terpisah dan pesanan pelanggan juga menyebut varian tertentu.

Di sinilah SKU bekerja. Setiap varian diberi kode sendiri, sehingga sistem, label rak, dan petugas gudang membicarakan barang yang sama persis.

Untuk penjual online, logikanya sama. Pilihan varian di halaman produk, misalnya warna atau ukuran, pada dasarnya adalah SKU. Kalau varian tertukar, pembeli menerima barang yang tidak ia pesan, dan komplain pun datang.

## Kenapa satu barang bisa punya banyak SKU?

Satu produk bisa pecah menjadi banyak SKU karena hal-hal berikut.

### Beda isi kemasan

Masker isi 50 dan isi 20 harganya beda, ukurannya beda, dan stoknya habis dengan kecepatan berbeda. Karena itu keduanya perlu dihitung terpisah.

### Beda warna atau ukuran

Kaus ukuran M dan L, atau tas hitam dan cokelat, biasanya dipisah SKU-nya. Pembeli memilih varian yang spesifik, jadi gudang harus tahu stok setiap varian.

### Beda kemasan jual (satuan vs karton)

Sebagian usaha menjual barang yang sama dalam satuan dan dalam karton. Kalau keduanya dijual dan disimpan sebagai unit berbeda, masing-masing perlu SKU sendiri. Kalau tidak, stok satuan dan stok karton akan tercampur di catatan.

## Contoh SKU: masker isi 50 vs isi 20

Tabel berikut ilustrasi. Kode di bawah dibuat untuk contoh, bukan standar resmi.

> **CONTOH**
>
> | Nama barang | Varian | Kode SKU | Satuan |
> |---|---|---|---|
> | Masker medis 3 ply | Biru, isi 50 | MSK-BIR-050 | Kotak |
> | Masker medis 3 ply | Biru, isi 20 | MSK-BIR-020 | Kotak |
> | Masker medis 3 ply | Putih, isi 50 | MSK-PUT-050 | Kotak |
> | Masker medis 3 ply | Biru, isi 50, karton 40 kotak | MSK-BIR-050-K40 | Karton |

Empat baris, empat SKU, walaupun semuanya "masker". Dengan cara ini, laporan stok bisa menjawab pertanyaan spesifik, misalnya berapa kotak masker biru isi 20 yang tersisa.

## SKU vs barcode (GTIN): apa bedanya?

Banyak orang menyamakan SKU dengan barcode. Keduanya berhubungan, tetapi tidak sama.

- **SKU** umumnya kode internal. Perusahaan atau toko membuat sendiri formatnya untuk keperluan stok. Toko lain bisa memakai kode berbeda untuk barang yang sama.
- **Barcode** adalah gambar garis yang bisa dipindai mesin. Pada produk ritel, angka di bawah barcode umumnya adalah **GTIN** (Global Trade Item Number). Menurut GS1, organisasi standar global untuk kode barang, GTIN bersifat unik, global, dan bisa diverifikasi. GTIN kadang juga disebut U.P.C atau EAN.

Menariknya, prinsipnya sama. GS1 menyatakan "each product variation needs its own GS1 GTIN": setiap ukuran, warna, dan kombinasinya butuh nomor sendiri. Aturan pengelolaan GTIN dari GS1 juga menyebut bahwa perubahan isi bersih yang tercantum di kemasan mengharuskan GTIN baru. Jadi, baik SKU maupun GTIN memegang prinsip yang sama: satu varian, satu kode.

| Aspek | SKU | GTIN di barcode |
|---|---|---|
| Siapa yang membuat | Perusahaan atau toko sendiri | Diterbitkan lewat organisasi anggota GS1 |
| Berlaku di mana | Internal | Global |
| Format | Bebas, sesuai kebutuhan | Mengikuti standar GS1 |
| Fungsi utama | Mengelola stok dan pesanan | Identifikasi produk dalam perdagangan |

## Cara membuat kode SKU sederhana

Perlu diingat: tidak ada format SKU baku yang berlaku untuk semua usaha. Yang penting adalah aturan internal Anda jelas dan dipatuhi.

### Aturan dasar: unik, konsisten, tanpa spasi

1. **Unik.** Satu varian, satu kode. Satu kode, satu varian.
2. **Konsisten.** Urutan bagian kode selalu sama untuk semua barang.
3. **Tanpa spasi dan karakter aneh.** Pakai huruf, angka, dan tanda hubung. Spasi sering membuat pencarian di sistem atau lembar kerja gagal.

### Pola kode yang mudah dibaca

Susun kode dari kiri ke kanan, dari yang umum ke yang spesifik: jenis barang, lalu varian, lalu isi atau ukuran. Hindari huruf O dan angka 0 di posisi yang bisa tertukar. Buat daftar induk SKU di satu tempat, berisi kode, nama lengkap, varian, dan satuan.

![Ilustrasi pola kode SKU contoh MSK-BIR-050: jenis, varian, lalu isi, dengan aturan unik, konsisten, dan tanpa spasi](/img/ilustrasi/apa-itu-sku/2-pola-kode-sku.webp){width="960" height="681" loading="lazy" style="border-radius:16px"}

### Jangan memakai ulang kode lama

Saat produk berhenti dijual, biarkan kodenya pensiun. Kalau kode lama dipakai untuk barang baru, data penjualan dan stok lama akan tercampur dengan barang yang berbeda.

## Kenapa stok harus dihitung per SKU

Stok yang benar adalah stok per SKU. Kalau dua varian dicampur dalam satu kode, sistem bisa bilang barang tersedia, padahal varian yang dipesan sudah habis.

> **CONTOH** Toko mencatat masker isi 50 dan isi 20 dalam satu kode. Sistem menunjukkan stok 30 kotak. Pembeli memesan 10 kotak isi 50, padahal di rak tinggal kotak isi 20. Pesanan terlanjur diterima, lalu dibatalkan atau dikirim salah.

Masalah seperti ini sering berujung pada [selisih stok di sistem dan rak](L14). SKU yang rapi juga memudahkan setiap tahap dalam [alur proses gudang](L04), dari penerimaan sampai pengiriman.

## Kesalahan umum soal SKU

- **Mencampur dua varian dalam satu kode.** Stok terlihat ada, tetapi variannya salah.
- **Kode di label beda dengan kode di sistem.** Petugas mengambil barang dari rak yang benar menurut label, tetapi sistem mencatat barang lain.
- **Satu varian punya dua kode.** Stok terbelah di dua catatan, sehingga salah satunya tampak habis padahal barangnya ada.
- **Kode terlalu panjang dan sulit dibaca.** Petugas cenderung salah ketik atau salah baca.

## Ringkasan

- SKU (stock keeping unit) adalah kode untuk satu varian barang yang dihitung, disimpan, dan dijual terpisah.
- Beda isi, warna, ukuran, atau kemasan jual biasanya berarti beda SKU.
- SKU umumnya kode internal; GTIN di barcode adalah nomor global dari sistem GS1. Keduanya memegang prinsip satu varian satu kode.
- Buat SKU yang unik, konsisten, tanpa spasi, dan jangan memakai ulang kode lama.
- Lanjutkan ke [istilah gudang lainnya](L20) untuk mengenal kosakata gudang dasar.
