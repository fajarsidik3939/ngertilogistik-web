# Terbit otomatis 1 artikel per hari

Blog memakai **antrean pendek**. `build.py` hanya menayangkan artikel dengan `terbit` ≤ hari ini (WIB). Semua berjalan otomatis tanpa menunggu persetujuan Fajar. Fajar tetap bisa mengedit artikel yang masih antre di GitHub, tapi itu opsional.

Setiap pagi (±07.00 WIB) tugas terjadwal melakukan:

1. **Tayangkan artikel hari ini:** jalankan `python3 build.py`, lalu commit dan push ke `main`. Vercel otomatis deploy.
2. **Tulis 1 artikel baru** dengan `terbit` = tanggal paling awal mulai **besok** (WIB) yang belum punya artikel. Dengan begitu tidak ada hari kosong; celah di antrean otomatis terisi duluan.
3. Build lagi, commit, dan push.

## Cara memilih topik
- Topik berikutnya adalah id Lxx terkecil di `data/topics.json` yang belum punya file di `content/artikel/` (cek field `id` di frontmatter, bukan nama file).
- Bahan dasar: `topic`, `key` (intinya), dan `vo` (naskah video) dari `data/topics.json`.
- Kategori dari pilar: P0 `dasar-logistik`, P1 `kamus-logistik`, P2 `manajemen-gudang`, P3 `pengiriman-barang`, P4 `salah-kaprah-logistik`, P5 `karier-logistik`.

## Riset SEO mini (pengganti brief)
- WebSearch untuk topik itu di Google Indonesia. Tentukan kata kunci utama (istilah yang paling banyak dipakai orang), 4–8 kata kunci turunan, dan 3–5 pertanyaan nyata untuk FAQ. Jangan mengarang volume pencarian.
- **Jangan kanibalisasi:** baca `kata_kunci` di semua artikel yang ada. Kata kunci utama artikel baru harus berbeda.
- Slug: huruf kecil, tanda hubung, ±2–5 kata berbasis kata kunci utama, tanpa kode Lxx, dan unik.
- `seo_title` ≤60 karakter (kata kunci di depan), `deskripsi` 140–155 karakter, `judul` (H1) natural.
- Kata kunci utama masuk di paragraf pertama dan minimal satu H2.
- Ikuti juga `situs.aturan_artikel` di `content/brief/seo_brief_L01-L20.json`.

## Menulis
Ikuti **semua** aturan di `content/brief/PANDUAN_PENULIS.md`: 900–1.300 kata, sumber nyata yang dibuka sendiri, angka fiktif dalam blockquote **CONTOH**, tanpa menyebut perusahaan atau merek kurir/software, tanpa em dash, FAQ di frontmatter, dan diakhiri `## Ringkasan`.
Pengecualian dari panduan itu: link internal `[anchor](Lxx)` boleh ke **semua** artikel yang sudah ada filenya (sudah tayang atau masih antre), 2–4 link. Builder otomatis menjadikan link ke artikel yang belum tayang sebagai teks biasa sampai artikelnya tayang.

## Kuis & glosarium untuk artikel baru (wajib)
- Tambahkan 5 soal untuk artikel baru di `data/kuis.json` dengan format yang sama (`{"Lxx": {"slug","judul","soal":[{"q","opsi":[4 opsi],"jawab":0-3,"bahas"}]}}`). Soal hanya dari isi artikel itu, variasikan posisi jawaban benar, tanpa em dash.
- Tambahkan 1–3 istilah baru dari artikel itu ke `data/glosarium.json` (`istilah`, `alias`, `arti`, `artikel`), jaga urutan abjad dan jangan menggandakan istilah yang sudah ada.
- Validasi kedua file dengan `python3 -c "import json;json.load(open('data/kuis.json'));json.load(open('data/glosarium.json'))"`.

## Kit promosi untuk artikel baru (wajib)
- Buat `promosi/<id>-<slug>.md` dengan format yang sama seperti file lain di folder itu (7 bagian: video pendek, carousel, LinkedIn, grup FB, WhatsApp, thread X/Threads, jawaban forum), lalu tambahkan barisnya ke tabel di `promosi/README.md`.
- Fakta hanya dari artikel itu. Tanpa merek, tanpa em dash.

## Ilustrasi artikel (wajib)
- Setiap artikel baru diberi 2–3 ilustrasi bergaya sama dengan video dan gambar sampul: latar navy gelap (#0B1220) bergaris grid, aksen kuning (#FFC400), kotak isometrik abu-abu, font Plus Jakarta Sans dan JetBrains Mono.
- Sumber ilustrasi ditulis sebagai potongan HTML (isi `<body>` dengan SVG inline) di `tools/ilustrasi/<slug>/<nomor>-<nama>.html`. Contoh lengkap: `tools/ilustrasi/cara-packing-barang/`. Pakai kelas yang sudah ada (`k`, `h1 em`, `sub`, `card`, `n`, `t`, `d`, `tag ok/bad`) dan akhiri dengan `{{FOOT}}`. Jangan memakai nama kelas `.route` atau `.foot` untuk elemen sendiri (sudah dipakai footer).
- Render dengan `python3 tools/ilustrasi.py <slug>`. Hasilnya WebP di `public/img/ilustrasi/<slug>/` dan tingginya dicetak di layar.
- Pasang di isi artikel sebagai paragraf sendiri: `![alt deskriptif](/img/ilustrasi/<slug>/<nama>.webp){width="960" height="<tinggi>" loading="lazy" style="border-radius:16px"}`.
- Satu ilustrasi ringkasan setelah paragraf pembuka, lalu 1–2 ilustrasi di bagian yang paling terbantu gambar (langkah, perbandingan, alur). Teks di gambar singkat dan besar karena gambar mengecil di HP; penjelasan tetap di teks artikel.
- Isi gambar hanya dari isi artikel: tanpa angka baru, tanpa merek, tanpa em dash. Angka contoh di gambar harus sama dengan blockquote **CONTOH** dan diberi label "Contoh".
- Buka hasil WebP dengan Read sebelum commit untuk cek teks tidak terpotong atau bertumpuk.

## Cek sebelum push
- Ilustrasi sudah dirender dan terpasang di artikel.
- Frontmatter YAML valid, `python3 build.py` sukses, dan baris "Antrean" menampilkan tanggalnya.
- Buka ulang setiap URL sumber dan pastikan klaimnya didukung. Klaim yang tidak didukung harus dihapus.
- Commit ke `main` dengan pesan `Artikel Lxx: <judul>` (untuk tayangan harian: `Tayang <tanggal>`).

## Halaman alat (jangan dihapus)
- `/template` dan `/kalkulator-kubikasi` dibuat build.py dari `content/halaman/*.html`.
- File Excel template ada di `public/files/` (dipertahankan build.py). Generatornya di `tools/template_xlsx/` (`python3 tools/template_xlsx/run.py public/files`).
- `/belajar`, `/kuis`, `/glosarium`, `/karier`, `/cheat-sheet`, dan `/kalkulator-logistik` dibuat `belajar.py` dari `data/*.json` dan `content/halaman/kalkulator-logistik.html`. PDF cheat sheet dibuat otomatis ke `public/files/cheatsheet/` saat isinya berubah.
- Setiap artikel otomatis punya tombol bagikan (WhatsApp, Facebook, X, LinkedIn, Telegram, salin link).
