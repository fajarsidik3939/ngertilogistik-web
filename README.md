# ngertilogistik-web

Situs edukasi **Ngerti Logistik** (https://ngertilogistik.web.id): perpustakaan materi logistik singkat.

- `data/topics.json` berisi data materi (judul, pilar, intinya, naskah)
- `build.py` membuat halaman statis ke folder `public/` (`python3 build.py`)
- `public/` berisi file yang di-deploy Vercel (`vercel.json` → outputDirectory `public`)

Tambah materi baru: tambahkan entri di `data/topics.json` + sampul `public/img/c/lxxx.webp`, jalankan `python3 build.py`, commit, push. Vercel otomatis deploy.
