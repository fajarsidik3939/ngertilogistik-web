---
id: L32
slug: kode-lokasi-rak-gudang
judul: "Kode Lokasi Rak Gudang: Cara Menyusun Alamat Barang yang Mudah Dibaca"
seo_title: "Kode Lokasi Rak Gudang: Format dan Cara Membuatnya"
deskripsi: "Kode lokasi rak gudang adalah alamat unik tiap barang, misalnya A-03-02-B. Pelajari format zona-lorong-rak-tingkat dan aturan pelabelan yang konsisten."
kategori: manajemen-gudang
kata_kunci: ["kode lokasi rak gudang", "bin location adalah", "format kode lokasi gudang", "cara membuat kode rak gudang", "penomoran lokasi gudang", "label rak gudang", "alamat barang di gudang", "contoh kode lokasi gudang"]
terbit: 2026-11-17
intinya: "Kode lokasi rak adalah **alamat unik tempat sebuah barang disimpan**, biasanya tersusun dari zona, lorong, rak, dan tingkat. Formatnya bebas, asal **konsisten, singkat, dan terbaca jelas** di rak."
faq:
  - q: "Apa itu kode lokasi rak gudang?"
    a: "Kode lokasi rak adalah alamat unik yang menunjukkan di mana sebuah barang disimpan di gudang. Kode ini biasanya gabungan beberapa bagian, seperti zona, lorong, rak, tingkat, dan nomor bin, sehingga petugas bisa menemukan barang tanpa menghafal tata letak."
  - q: "Apa bedanya kode lokasi rak dengan bin location?"
    a: "Bin location adalah istilah bahasa Inggris untuk posisi simpan tertentu yang diberi identitas unik di gudang. Dalam praktik, kode lokasi rak adalah penulisan atau label dari posisi tersebut."
  - q: "Bagaimana format kode lokasi gudang yang baik?"
    a: "Tidak ada satu format wajib. Sumber-sumber panduan gudang memberi contoh seperti Z1-A03-R2-L4-B07 atau A03-S02-B05. Yang ditekankan adalah format yang konsisten, pemisah yang jelas, dan kode yang tetap pendek."
  - q: "Rak bertingkat sebaiknya dinomori dari atas atau bawah?"
    a: "Salah satu panduan menyarankan penomoran dari bawah ke atas. Dengan begitu, bila rak kelak ditambah tingkatnya, label yang sudah ada tidak perlu diganti."
  - q: "Apa yang terjadi bila label rak hilang atau salah?"
    a: "Kode di sistem tidak lagi cocok dengan kondisi fisik, sehingga barang sulit ditemukan dan risiko salah ambil naik. Karena itu label perlu tahan lama, terlihat dari jalur picking, dan diperbarui setiap ada perubahan."
sumber:
  - judul: "ShipBob, How to Design and Create the Ultimate Warehouse Location Numbering System (diperbarui 12 Maret 2026)"
    url: "https://www.shipbob.com/blog/warehouse-location/"
    catatan: "Hierarki zona, lorong, rak, level, bin; contoh kode Z1-A03-R2-L4-B07 dan A-03-2-4-07; pemisah antar elemen; pola urutan yang bisa diprediksi (ganjil di kiri, genap di kanan); angka kecil di depan gudang; nomor lorong berkelipatan 10 untuk ruang tumbuh; hindari konflik kode; change log dan audit minimal sekali per kuartal; manfaat: picking lebih cepat, kesalahan berkurang, pelatihan staf lebih sederhana."
  - judul: "Linnworks, Mastering bin location and labeling for efficient warehouses (direvisi 23 Maret 2025)"
    url: "https://www.linnworks.com/blog/warehouse-locations-and-bin-labeling-best-practices-and-tips/"
    catatan: "Definisi location, primary bin location, dan bin; format aisle-unit-shelf-bin; nomori shelf dari bawah ke atas; angka nol di depan (01, 02) agar urutan terbaca benar; pelabelan tidak konsisten disebut merusak sistem; perbandingan pelabelan standar dan serpentine."
  - judul: "Racklify, Bin Location: A Beginner's Guide (terbit 15 Oktober 2025)"
    url: "https://racklify.com/encyclopedia/bin-location-a-beginners-guide/"
    catatan: "Bin location sebagai posisi simpan unik seperti alamat; contoh A03-S02-B05; kode singkat dan hindari karakter membingungkan seperti huruf O dan angka 0; label terlihat dari jalur picking; sistem di perangkat lunak mencerminkan tata letak fisik dan diperbarui saat stok pindah; pertimbangan ergonomi; langkah awal: sketsa peta, pilih konvensi, beri label, masukkan ke sistem atau spreadsheet, latih staf."
---
Kode lokasi rak gudang adalah alamat unik yang menunjukkan di mana sebuah barang disimpan. Contohnya A-03-02-B: zona A, lorong 3, rak 2, tingkat B. Dengan kode ini, petugas baru pun bisa menemukan barang tanpa harus hafal isi gudang.

Artikel ini versi lengkap dari video 60 detik Ngerti Logistik tentang kode lokasi rak.

![Ilustrasi kode lokasi A-03-02-B diuraikan menjadi zona, lorong, rak, dan tingkat](/img/ilustrasi/kode-lokasi-rak-gudang/1-anatomi-kode.webp){width="960" height="601" loading="lazy" style="border-radius:16px"}

## Kode lokasi rak gudang itu apa?

Sebuah panduan gudang menyebut bin location sebagai posisi simpan tertentu yang punya identitas unik di dalam gudang, mirip alamat di dalam sebuah fasilitas. Panduan lain membedakan tiga hal: location, yaitu area berlabel tempat petugas mengambil produk, primary bin location, yaitu lokasi utama tempat sebuah item disimpan dan biasanya dicari lebih dulu, dan bin, yaitu ruang simpan paling spesifik di dalam sebuah lokasi.

Jadi, kode lokasi rak adalah cara menuliskan alamat itu di rak dan di sistem. Ia dipakai sejak barang disimpan lewat [putaway](L16) sampai barang diambil saat [picking](L22).

## Bagian-bagian kode lokasi

Sumber-sumber panduan memberi contoh yang berbeda, tetapi pola dasarnya mirip: dari bagian terbesar menuju yang paling kecil.

| Bagian | Artinya | Contoh |
|---|---|---|
| Zona | Area besar di gudang | A |
| Lorong | Jalur di antara deretan rak | 03 |
| Rak | Unit rak di lorong itu | 02 |
| Tingkat | Susunan ke atas pada rak | B |
| Bin | Posisi paling spesifik di satu tingkat | 07 |

Tiga contoh dari sumber yang kami baca: Z1-A03-R2-L4-B07 (zona, lorong, rak, level, bin), A-03-2-4-07, dan A03-S02-B05 (lorong, tingkat, bin tanpa zona). Artinya, tidak ada format yang wajib. Gudang kecil bisa memakai tiga bagian saja, gudang besar bisa memakai lima.

> **CONTOH** Sebuah gudang fiktif memakai format zona-lorong-rak-tingkat. Kode **A-03-02-B** dibaca: zona A, lorong 3, rak 2, tingkat B. Petugas yang menerima daftar ambil berisi kode itu cukup berjalan ke zona A, masuk lorong 3, lalu mencari rak 2 pada tingkat B.

## Aturan menyusun kode yang mudah dipakai

Dari tiga sumber tadi, ada beberapa aturan yang berulang.

1. **Konsisten di seluruh gudang.** Salah satu panduan menyebut pelabelan yang tidak konsisten sebagai hal yang paling merusak sistem, karena staf cepat kewalahan.
2. **Pakai pemisah yang jelas.** Tanda hubung atau titik membuat tiap bagian mudah dipisahkan, baik oleh mata maupun oleh sistem.
3. **Pakai nol di depan.** Tulis 01, 02, 03, bukan 1, 2, 3, agar urutan alfanumerik di sistem terbaca benar.
4. **Buat urutan yang bisa ditebak.** Satu panduan memberi contoh ganjil di sisi kiri dan genap di sisi kanan, dengan angka kecil di bagian depan gudang.
5. **Sisakan ruang tumbuh.** Penomoran lorong berkelipatan 10 (A10, A20, A30) memberi celah bila kelak ada lorong baru di antaranya.
6. **Nomori tingkat dari bawah ke atas.** Bila rak ditinggikan, label lama tidak perlu diganti.
7. **Jaga kode tetap pendek.** Hindari karakter yang mudah tertukar, misalnya huruf O dengan angka 0.
8. **Hindari kode kembar.** Contoh dari panduan: rak "3A" dan lorong "3A" akan membingungkan.

![Perbandingan kode lokasi yang konsisten dan kode yang membingungkan](/img/ilustrasi/kode-lokasi-rak-gudang/2-aturan-kode.webp){width="960" height="591" loading="lazy" style="border-radius:16px"}

## Urutan penomoran: standar atau serpentine

Salah satu panduan membandingkan dua pola pelabelan. Pola standar menomori rak berurutan dengan cara yang sederhana. Pada pola serpentine, urutan mengikuti jalur zigzag. Contoh dari panduan itu: lorong 01 berisi unit AA, AB, AC, lalu AF, AE, AD, sehingga petugas menyusuri satu sisi lalu kembali lewat sisi lainnya.

Menurut panduan itu, serpentine dianggap lebih efisien untuk wave picking karena petugas mengikuti jalur zigzag, tetapi lebih rumit dipelajari staf dan butuh sistem yang kuat. Untuk gudang kecil atau tim baru, pola standar yang sederhana biasanya cukup. Pilih satu, lalu pakai terus.

## Kesalahan yang sering terjadi

Masalah paling sering bukan pada rumus kodenya, melainkan pada disiplin memakainya. Kode ditulis dengan gaya berbeda-beda oleh orang berbeda, label dibuat dari kertas yang cepat pudar, atau barang dipindah ke rak lain tanpa mengubah catatan. Akibatnya sistem menunjuk ke rak yang kosong, sementara barangnya ada di tempat lain.

> **CONTOH** Sistem fiktif mencatat sebuah barang di **A-03-02-B**. Karena rak penuh, petugas menaruhnya di **A-03-04-B** tanpa mengubah catatan. Petugas picking yang datang ke rak 2 tidak menemukan apa-apa, lalu menandai barang itu habis, padahal barangnya masih ada.

Karena itu, setiap perpindahan barang perlu dicatat, sekecil apa pun.

## Label di rak harus terbaca

Kode yang rapi di sistem tidak berguna bila label di rak hilang atau salah. Sumber-sumber tadi menekankan beberapa hal:

- Label tahan lama dan terlihat dari jalur picking.
- Sistem di perangkat lunak mencerminkan tata letak fisik, dan diperbarui setiap stok berpindah.
- Barang berat sebaiknya ditempatkan di ketinggian yang nyaman, sehingga ergonomi ikut dipertimbangkan saat menentukan tingkat.
- Dokumentasikan perubahan di satu catatan terpusat, dan audit sistem lokasi minimal sekali per kuartal.

Bila kode di sistem tidak cocok dengan kondisi fisik, barang jadi sulit ditemukan dan masalahnya sering berujung pada [selisih stok](L14). Karena itu, setiap kali barang dipindah, kode di sistem harus ikut diubah.

## Langkah membuat sistem kode dari nol

Panduan untuk pemula menyarankan urutan sederhana:

1. Gambar sketsa denah gudang.
2. Pilih konvensi penamaan dan tuliskan aturannya.
3. Beri label pada rak.
4. Masukkan kode ke sistem atau spreadsheet.
5. Latih staf membaca kode.

![Lima langkah membuat kode lokasi: sketsa, konvensi, label, input sistem, latih staf](/img/ilustrasi/kode-lokasi-rak-gudang/3-lima-langkah.webp){width="960" height="456" loading="lazy" style="border-radius:16px"}

## Manfaat kode lokasi yang baik

Panduan-panduan itu menyebut manfaat yang serupa. Petugas lebih cepat menemukan barang dan kesalahan ambil berkurang. Pelatihan staf baru lebih sederhana karena mereka belajar sistem alamat, bukan menghafal tempat acak. Rute juga lebih mudah diatur, sehingga jarak tempuh bisa ditekan.

Manfaat ini bergantung pada satu syarat: kode dan label harus selalu sesuai dengan keadaan nyata di rak.

## Ringkasan

- Kode lokasi rak adalah alamat unik barang di gudang, biasanya tersusun dari zona, lorong, rak, dan tingkat.
- Tidak ada format wajib; yang penting konsisten, singkat, dan memakai pemisah yang jelas.
- Pakai nol di depan, nomori tingkat dari bawah ke atas, dan sisakan ruang untuk lorong baru.
- Label harus tahan lama dan terlihat, dan kode di sistem harus selalu cocok dengan kondisi fisik.
- Dokumentasikan perubahan dan audit sistem lokasi secara berkala.
