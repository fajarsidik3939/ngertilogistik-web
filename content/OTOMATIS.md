# Terbit otomatis 1 artikel per hari

Blog memakai **antrean 3 hari**. `build.py` hanya menayangkan artikel dengan `terbit` ≤ hari ini (WIB). Artikel dengan tanggal di depan menunggu di antrean, jadi Fajar sempat mengecek atau mengeditnya di GitHub sebelum tayang.

Setiap pagi (±07.00 WIB) tugas terjadwal melakukan:

1. **Tayangkan artikel hari ini:** jalankan `python3 build.py`, lalu commit dan push ke `main`. Vercel otomatis deploy.
2. **Tulis 1 artikel baru** di ujung antrean, dengan `terbit` = tanggal terbit terakhir di antrean + 1 hari (minimal hari ini + 3).
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

## Cek sebelum push
- Frontmatter YAML valid, `python3 build.py` sukses, dan baris "Antrean" menampilkan tanggalnya.
- Buka ulang setiap URL sumber dan pastikan klaimnya didukung. Klaim yang tidak didukung harus dihapus.
- Commit ke `main` dengan pesan `Artikel Lxx: <judul>` (untuk tayangan harian: `Tayang <tanggal>`).
