"""Generator landing page produk digital (AIDA) -> content/halaman/<slug>.html.
Jalankan: python3 tools/produk/gen_landing.py  lalu  python3 build.py
Link checkout & harga diatur di PRODUK pada build.py ({{LYNK}} dan {{HARGA}})."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "content/halaman/toolkit-gudang-pro.html")
CSS = re.search(r"<style>.*?</style>", open(SRC, encoding="utf-8").read(), re.S).group(0)
CSS = CSS.replace("</style>", """.pk-cover{position:relative}.pk-cover img{width:100%;max-width:520px;display:block;margin:0 auto;border-radius:22px;box-shadow:0 30px 80px rgba(0,0,0,.5);border:1px solid var(--line)}
.pk-item .vis img{width:100%;border-radius:10px;border:1px solid var(--line)}
.pk-item .vis.duo{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.pk-bundle li span{margin-left:auto;color:var(--mute);font-family:var(--fm);font-size:14px;white-space:nowrap}
.pk-old{font-size:18px;color:var(--mute);text-decoration:line-through;margin-bottom:4px}
.pk-note{font-size:13px;color:var(--mute);margin-top:10px}
</style>""")

def li(xs): return "".join(f"<li>{x}</li>" for x in xs)

def mock(title, tag, head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f'<td class="n">{c}</td>' if (i > 0 and c[:1].isdigit()) else f"<td>{c}</td>" for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="pk-mini"><div class="sheet"><div class="sheet-h">{title} <i>{tag}</i></div><table><tr>{th}</tr>{tr}</table></div></div>'

def page(p):
    items = ""
    for it in p["items"]:
        v = it["vis"]
        if isinstance(v, list):
            vis = f'<div class="vis{" duo" if len(v) > 1 else ""}">' + "".join(f'<img src="/img/produk/{x}.webp" alt="{it["h3"]}" loading="lazy">' for x in v) + "</div>"
        else:
            vis = v
        items += f'<div class="pk-item">{vis}<div><span class="kick">{it["kick"]}</span><h3>{it["h3"]}</h3><p>{it["p"]}</p><ul>{li(it["ul"])}</ul></div></div>'
    pains = "".join(f'<div class="pk-card"><span class="pk-num">0{i+1}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(p["pains"]))
    story = "".join(f"<p>{x}</p>" for x in p["story"])
    faq = "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in p["faq"])
    old = f'<div class="pk-old">{p["old"]}</div>' if p.get("old") else ""
    offer_cls = ' class="pk-bundle"' if p.get("bundle") else ""
    return f"""{CSS}
<main id="isi">

<!-- ATTENTION -->
<section class="pk-hero"><div class="wrap pk-hero-in">
<div>
<span class="pk-tag">{p["tag"]}</span>
<h1>{p["h1"]}</h1>
<p class="lead">{p["lead"]}</p>
<ul class="pk-checks">{li(p["checks"])}</ul>
<div class="pk-buy"><a class="btn" href="{{{{LYNK}}}}" target="_blank" rel="noopener" data-cta="hero">{p["cta"]}</a><div class="pk-price">{{{{HARGA}}}}<small>Sekali bayar · unduh lewat Lynk.id</small></div></div>
</div>
<div class="pk-cover"><img src="/img/produk/{p["slug"]}-cover.webp" alt="{p["name"]}" width="720" height="720" loading="eager"></div>
</div></section>

<!-- INTEREST -->
<section class="sec"><div class="wrap">
<div class="pk-story">
<span class="eyebrow">Kenal situasi ini?</span>
<p class="big">{p["story_big"]}</p>
{story}
</div>
<div class="pk-pain">{pains}</div>
<p class="pk-story" style="font-size:18px;color:var(--txt);margin:0">{p["turn"]}</p>
</div></section>

<!-- DESIRE -->
<section class="sec alt"><div class="wrap">
<div class="sec-h"><span class="eyebrow">Bayangkan kalau</span><h2>{p["vs_h2"]}</h2></div>
<div class="pk-vs">
<div class="before"><h3>Sebelum</h3><ul>{li(p["before"])}</ul></div>
<div class="after"><h3>Dengan {p["name"]}</h3><ul>{li(p["after"])}</ul></div>
</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="sec-h"><span class="eyebrow">Isi paket</span><h2>{p["items_h2"]}</h2></div>
<div class="pk-items">{items}</div>
</div></section>

<section class="sec alt"><div class="wrap">
<div class="sec-h"><span class="eyebrow">Cara pakai</span><h2>Bisa dipakai <em>hari ini juga</em></h2></div>
<ol class="pk-steps">{li(p["steps"])}</ol>
<div class="pk-fit" style="margin-top:22px">
<div class="pk-card"><h3>Cocok untuk kamu yang</h3><ul>{li(p["fit"])}</ul></div>
<div class="pk-card"><h3>Biar jelas dari awal</h3><ul>{li(p["honest"])}</ul></div>
</div>
</div></section>

<!-- ACTION -->
<section class="sec" id="beli"><div class="wrap">
<div class="pk-offer">
<span class="eyebrow">Semua yang kamu dapat</span>
<h2>{p["name_html"]}</h2>
<p class="sub">{p["offer_sub"]}</p>
<ul{offer_cls}>{li(p["offer"])}</ul>
{old}<div class="pk-price">{{{{HARGA}}}}</div>
<a class="btn" href="{{{{LYNK}}}}" target="_blank" rel="noopener" data-cta="offer">{p["cta_offer"]}</a>
<div class="pk-trust"><span>Sekali bayar</span><span>{p["format"]}</span><span>Pembayaran lewat Lynk.id</span></div>
</div>
</div></section>

<section class="sec alt"><div class="wrap narrow">
<div class="faq" style="margin-top:0"><h2>Masih ragu? Ini jawabannya</h2>{faq}
<details><summary>Boleh dibagikan ke teman atau dijual lagi?</summary><div><p>Tidak. File untuk dipakai pribadi atau di tempat kerja/usaha pembeli, tidak untuk dijual ulang atau dibagikan ulang.</p></div></details>
<details><summary>Bagaimana cara menerima filenya?</summary><div><p>Pembayaran dan pengiriman file dilakukan lewat Lynk.id. Kalau file tidak bisa dibuka, kirim DM ke @ngertilogistik.</p></div></details>
</div>
</div></section>

<section class="pk-final"><div class="wrap">
<h2>{p["final_h2"]}</h2>
<p>{p["final_p"]}</p>
<div class="pk-buy"><a class="btn" href="{{{{LYNK}}}}" target="_blank" rel="noopener" data-cta="final">{p["cta"]}</a><div class="pk-price">{{{{HARGA}}}}<small>Sekali bayar · unduh lewat Lynk.id</small></div></div>
</div></section>
</main>
<div class="pk-bar" id="pkBar"><div><b>{p["name"]}</b><span>{{{{HARGA}}}} · sekali bayar</span></div><a class="btn" href="{{{{LYNK}}}}" target="_blank" rel="noopener" data-cta="bar">Ambil sekarang</a></div>
<script>(function(){{var bar=document.getElementById('pkBar'),hero=document.querySelector('.pk-hero'),offer=document.getElementById('beli');if(!bar||!('IntersectionObserver' in window))return;var hv=true,ov=false;function u(){{bar.classList.toggle('on',!hv&&!ov)}}new IntersectionObserver(function(e){{hv=e[0].isIntersecting;u()}}).observe(hero);new IntersectionObserver(function(e){{ov=e[0].isIntersecting;u()}}).observe(offer)}})();</script>
"""

STEPS = lambda last: ["Bayar lewat Lynk.id, lalu unduh file ZIP.", "Buka file dan ikuti panduan singkat di dalamnya.", last]
COMMON_FAQ_XLS = ("Saya tidak jago Excel, bisa pakai?", "Bisa. Kamu hanya mengisi kolom kuning; kolom lain berisi rumus yang bekerja sendiri. Ada sheet <b>Mulai Di Sini</b> berisi langkah pemakaian, dan file sudah berisi data contoh supaya kamu lihat hasilnya dulu.")

P = []
# ------------------------------------------------------------------ STOK & CUAN
P.append(dict(slug="stok-cuan-seller", name="Stok & Cuan", name_html='Stok &amp; <em>Cuan</em>', tag="Untuk online seller &amp; UMKM",
  h1="Omzet naik, tapi <em>untungnya ke mana?</em>",
  lead="Catat restock dan penjualan sekali saja. Potongan marketplace, modal, dan laba bersih tiap channel langsung terhitung, lengkap dengan stok per gudang.",
  checks=["Template Excel 10 sheet yang saling terhubung", "Laba bersih per channel: Shopee, TikTok Shop, Tokopedia, dan lainnya", "Kalkulator harga jual sesuai target laba"],
  cta="Ambil template-nya", cta_offer="Ambil Stok &amp; Cuan",
  story_big="Akhir bulan, saldo di aplikasi terlihat besar. Tapi setelah dipotong biaya admin, voucher, subsidi ongkir, dan modal barang, sisanya ternyata tipis.",
  story=["Belum lagi stok: di gudang tinggal sedikit, padahal di etalase toko masih banyak. Barang yang paling laku malah habis duluan.", "Tanpa catatan yang rapi, sulit tahu channel mana yang benar-benar menguntungkan."],
  pains=[("Untung tidak jelas", "Omzet tercatat, tapi potongan marketplace dan modal tidak dihitung per pesanan."), ("Stok tersebar", "Barang ada di gudang, toko, dan rumah. Total stok dihitung manual."), ("Harga asal pasang", "Harga jual ditentukan tanpa menghitung potongan channel, jadi margin tergerus.")],
  turn='Masalahnya bukan jualanmu kurang laku. Masalahnya, <b style="color:var(--ink)">hitungannya belum ada.</b>',
  vs_h2="Jualan online <em>sebelum dan sesudah</em>",
  before=["Untung dikira dari saldo yang masuk", "Potongan marketplace dihitung kira-kira", "Stok per lokasi dicek satu per satu", "Tahu barang habis setelah pembeli komplain", "Harga jual sama untuk semua channel"],
  after=["Laba bersih per pesanan dan per channel terhitung otomatis", "Biaya admin, layanan, dan biaya tetap channel bisa kamu atur sendiri", "Stok gudang, toko, dan lokasi lain terlihat dalam satu tabel", "Status RESTOCK/HABIS muncul sendiri", "Harga minimal per channel sesuai target laba"],
  items_h2="10 sheet, <em>saling terhubung</em>",
  items=[dict(vis=["seller-dashboard"], kick="Dashboard", h3="Laporan per channel otomatis", p="Ganti bulan di pengaturan, semua angka menyesuaikan.",
              ul=["Omzet, laba bersih, margin, jumlah pesanan, nilai stok", "Tabel per channel: biaya marketplace, HPP, subsidi ongkir, laba", "Tren omzet dan laba per bulan + grafik"]),
         dict(vis=mock("Stok", "MULTI-GUDANG", ["SKU", "Gudang", "Toko", "Status"], [["KAOS-M", "22", "25", '<span class="st y">RESTOCK</span>'], ["CASE-CLR", "92", "26", '<span class="st g">AMAN</span>'], ["MADU-500", "11", "3", '<span class="st g">AMAN</span>']]),
              kick="Stok", h3="Stok per gudang &amp; produk laris/lambat", p="Stok bergerak otomatis dari restock, penjualan, dan pindah gudang.",
              ul=["Sampai 3 lokasi stok (gudang, toko, cadangan)", "Status RESTOCK/HABIS dan nilai stok", "10 produk terlaris dan 10 paling lambat per periode"]),
         dict(vis=mock("Kalkulator Harga", "TARGET LABA", ["Channel", "Harga min."], [["Shopee", "49.000"], ["TikTok Shop", "48.500"], ["Offline", "39.500"]]),
              kick="Kalkulator", h3="Harga jual &amp; ongkir", p="Hitung sebelum pasang harga, bukan sesudah rugi.",
              ul=["Harga jual minimal per channel dari modal, kemasan, subsidi ongkir, dan target laba", "Cek laba di harga yang sudah kamu pasang", "Berat volumetrik dan estimasi ongkir per ukuran paket"])],
  steps=STEPS("Isi biaya tiap channel dan produkmu, lalu catat restock &amp; penjualan."),
  fit=["Jualan di Shopee, TikTok Shop, Tokopedia, atau Lazada", "Punya toko offline sekaligus online", "Reseller yang menyimpan stok sendiri"],
  honest=["Ini template Excel, bukan aplikasi yang terhubung otomatis ke marketplace. Data penjualan diisi atau ditempel sendiri.", "Persentase biaya marketplace di file adalah contoh. Isi sesuai tarif tokomu.", "Laba di sini belum termasuk biaya iklan, gaji, dan sewa.", "Kapasitas 300 SKU dan 2.000 baris penjualan, bisa diperpanjang."],
  offer_sub="Template Excel untuk tahu stok dan untung yang sebenarnya.",
  offer=["<span><b>Dashboard</b> · omzet, laba, margin, pesanan, nilai stok, tren bulanan</span>", "<span><b>Penjualan → laba otomatis</b> · biaya marketplace, HPP, subsidi ongkir</span>", "<span><b>Stok multi-gudang</b> · status RESTOCK/HABIS, laris &amp; lambat</span>", "<span><b>Kalkulator</b> · harga jual sesuai target laba, ongkir &amp; volumetrik</span>"],
  format="Excel (.xlsx)",
  faq=[COMMON_FAQ_XLS, ("Apakah terhubung otomatis ke Shopee atau TikTok Shop?", "Tidak. Ini file Excel; pesanan dicatat atau ditempel dari laporan marketplace. Keuntungannya: semua channel bisa digabung di satu file."), ("Bisa untuk lebih dari satu gudang?", "Bisa, sampai 3 lokasi stok. Nama lokasinya bisa kamu ganti di sheet Pengaturan.")],
  final_h2="Jualan tetap jalan, <em>untungnya sekarang kelihatan.</em>", final_p="Template Excel 10 sheet: laba per channel, stok multi-gudang, dan kalkulator harga."))

# ------------------------------------------------------------------ EKSPEDISI
P.append(dict(slug="toolkit-ekspedisi", name="Toolkit Ekspedisi", name_html='Toolkit <em>Ekspedisi</em>', tag="Untuk ekspedisi &amp; forwarder",
  h1="Quotation cepat, kiriman terpantau, <em>invoice tinggal cetak.</em>",
  lead="Satu file Excel untuk ekspedisi dan forwarder: hitung berat ditagih dari dimensi koli, buat penawaran rapi, pantau ketepatan waktu kiriman, lalu tagih dengan invoice otomatis.",
  checks=["Kalkulator quotation: CBM, volumetrik, asuransi, PPN, total", "Shipment tracker dengan status tepat/terlambat otomatis", "Quotation &amp; invoice siap PDF + dashboard on-time"],
  cta="Ambil Toolkit-nya", cta_offer="Ambil Toolkit Ekspedisi",
  story_big="Customer minta harga sekarang. Kamu hitung CBM satu per satu di kalkulator HP, cari tarif di chat lama, lalu ketik ulang penawarannya.",
  story=["Sorenya ada yang tanya kiriman minggu lalu sudah sampai atau belum. Datanya tersebar di grup WhatsApp dan buku catatan.", "Akhir bulan, invoice dibuat manual dari resi yang dikumpulkan satu per satu."],
  pains=[("Quotation lambat", "Dimensi, berat volumetrik, dan tarif dihitung ulang setiap ada permintaan."), ("Status kiriman tersebar", "Tidak ada satu tempat untuk melihat mana yang tepat waktu dan mana yang terlambat."), ("Penagihan manual", "Invoice disusun ulang dari resi, rawan salah angka.")],
  turn='Masalahnya bukan timmu kurang cepat. Masalahnya, <b style="color:var(--ink)">alurnya belum di satu tempat.</b>',
  vs_h2="Kerja ekspedisi <em>sebelum dan sesudah</em>",
  before=["CBM dan volumetrik dihitung manual", "Tarif dicari di chat atau ingatan", "Penawaran diketik ulang di Word", "Status kiriman ditanyakan satu per satu", "Invoice disusun manual dari resi"],
  after=["Isi dimensi koli, berat ditagih langsung keluar", "Tarif diambil otomatis dari rate card", "Quotation rapi terisi sendiri, tinggal simpan PDF", "Ketepatan waktu (tepat/terlambat/lewat ETA) muncul otomatis", "Ketik nomor resi, invoice terisi sendiri"],
  items_h2="Dari penawaran <em>sampai tagihan</em>",
  items=[dict(vis=["ekspedisi-quotation"], kick="Quotation", h3="Rate card + kalkulator + cetak quotation", p="Tarif per kg, per W/M (LCL), atau per trip.",
              ul=["CBM, berat aktual, berat volumetrik, berat ditagih", "Packing kayu, asuransi (rate &amp; premi minimum), handling, diskon, PPN", "Cetak quotation siap PDF dengan syarat &amp; ketentuan"]),
         dict(vis=mock("Shipment Tracker", "OTOMATIS", ["Resi", "Tujuan", "Ketepatan"], [["NL261001001", "Makassar", '<span class="st g">TEPAT</span>'], ["NL261005010", "Medan", '<span class="st r">TERLAMBAT</span>'], ["NL261111064", "Surabaya", '<span class="st y">LEWAT ETA</span>']]),
              kick="Tracking", h3="Shipment tracker, invoice &amp; dashboard", p="Satu baris per resi, sisanya otomatis.",
              ul=["Status, ETA, tanggal terima, POD kembali atau belum", "Invoice otomatis dari nomor resi + jatuh tempo sesuai termin customer", "Dashboard: jumlah kiriman, omzet, on-time %, retur, top 5 customer, tren bulanan"]),
         dict(vis=mock("LCL vs FCL", "TERMURAH", ["Opsi", "Biaya"], [["LCL", "3.789.500"], ["FCL 20'", "12.000.000"], ["FCL 40' HC", "19.500.000"]]),
              kick="Bonus", h3="LCL vs FCL + 3 cheat sheet", p="Untuk kiriman laut dan bahan menjawab customer.",
              ul=["Bandingkan LCL dengan FCL 20', 40', 40' HC berdasarkan volume dan berat", "Bonus cheat sheet Incoterms 2020, Ukuran Kontainer, dan Rumus Logistik"])],
  steps=STEPS("Ganti nama perusahaan, isi rate card dan customer, lalu buat quotation pertama."),
  fit=["Punya usaha ekspedisi atau jasa kirim kecil-menengah", "Bekerja sebagai admin, sales, atau CS di forwarder", "Rutin mengirim barang dan ingin hitungan ongkos yang rapi"],
  honest=["Ini template Excel, bukan aplikasi tracking real-time. Status kiriman diupdate manual.", "Tarif di file adalah contoh. Isi dengan tarif usahamu.", "Tarif PPN jasa pengiriman bisa berbeda dari tarif umum. Isi sesuai ketentuan pajak usahamu.", "Kapasitas 100 rate, 200 customer, dan 1.000 kiriman, bisa diperpanjang."],
  offer_sub="Template Excel dari penawaran sampai penagihan.",
  offer=["<span><b>Rate card + kalkulator quotation</b> · CBM, volumetrik, asuransi, PPN</span>", "<span><b>Cetak quotation &amp; invoice</b> · terisi otomatis, siap PDF</span>", "<span><b>Shipment tracker + dashboard</b> · on-time %, POD, top customer</span>", "<span><b>LCL vs FCL + 3 cheat sheet bonus</b></span>"],
  format="Excel (.xlsx) + bonus PNG",
  faq=[COMMON_FAQ_XLS, ("Bisa pakai tarif dan nama perusahaan sendiri?", "Bisa. Tarif diisi di Rate Card; nama, alamat, dan rekening diganti di sheet Cetak Quotation dan Invoice."), ("Apakah bisa untuk kiriman laut LCL dan truk sewa?", "Bisa. Basis tarif bisa per kg, per W/M (LCL, 1 ton = 1 m³), atau per trip armada.")],
  final_h2="Penawaran berikutnya, <em>kirim lebih cepat dan lebih rapi.</em>", final_p="Quotation, tracker, invoice, dashboard, dan LCL vs FCL dalam satu file Excel."))

# ------------------------------------------------------------------ LOLOS KERJA
P.append(dict(slug="lolos-kerja-logistik", name="Paket Lolos Kerja", name_html='Lolos Kerja <em>Logistik</em>', tag="Untuk pelamar kerja logistik",
  h1="CV dilirik HRD, interview lancar, <em>tes Excel tidak panik.</em>",
  lead="Template CV ATS untuk 5 posisi logistik, 50 pertanyaan interview dengan contoh jawaban, dan latihan tes Excel yang langsung menilai jawabanmu.",
  checks=["CV ATS 5 posisi + 2 contoh surat lamaran (Word)", "E-book 50 pertanyaan interview + contoh jawaban", "Latihan tes Excel 8 soal + kunci jawaban"],
  cta="Siapkan lamaranku", cta_offer="Ambil Paket Lolos Kerja",
  story_big="Sudah kirim banyak lamaran, tapi jarang dipanggil. Sekali dipanggil, bingung menjawab \"ceritakan tentang diri Anda\" dan grogi saat diminta mengerjakan tes Excel.",
  story=["Sering kali masalahnya bukan kemampuan, tapi persiapan: CV yang sulit dibaca sistem rekrutmen, jawaban yang tidak terstruktur, dan rumus Excel yang belum dilatih."],
  pains=[("CV tidak terbaca", "Desain ramai, tabel, dan foto bisa menyulitkan sistem penyaring CV (ATS)."), ("Jawaban mengambang", "Pertanyaan teknis gudang dan ekspedisi dijawab tanpa contoh nyata."), ("Tes Excel bikin panik", "SUMIFS, VLOOKUP, dan pivot belum pernah dilatih dengan kasus logistik.")],
  turn='Kemampuanmu mungkin sudah cukup. Yang perlu ditambah: <b style="color:var(--ink)">persiapan yang terarah.</b>',
  vs_h2="Melamar kerja <em>sebelum dan sesudah</em>",
  before=["CV memakai template desain yang ramai", "Pengalaman ditulis sebagai daftar tugas", "Menghafal jawaban dari internet", "Belajar Excel dari video acak", "Datang interview tanpa checklist"],
  after=["CV satu kolom yang ramah ATS untuk posisi logistik", "Poin pengalaman dengan kata kerja dan angka", "Pola jawaban dengan metode STAR + contoh", "8 soal Excel kasus logistik dengan cek jawaban otomatis", "Checklist persiapan H-3 sampai hari-H"],
  items_h2="3 bagian, <em>siap dipakai</em>",
  items=[dict(vis=["cv-ats"], kick="Word", h3="Template CV ATS 5 posisi + surat lamaran", p="Tinggal ganti dengan data dan pengalamanmu.",
              ul=["Admin gudang (fresh graduate), staf logistik &amp; ekspedisi, inventory control, PPIC, purchasing", "Panduan aturan ATS dan cara menulis poin pengalaman", "Contoh surat lamaran via email dan versi formal"]),
         dict(vis=["interview-isi"], kick="PDF", h3="E-book 50 Pertanyaan Interview Logistik", p="Untuk setiap pertanyaan: maksud HRD, contoh jawaban, dan yang harus dihindari.",
              ul=["Pertanyaan umum, gudang &amp; inventory, pengiriman, PPIC &amp; purchasing, Excel &amp; sistem, situasional", "Metode STAR, 5 pertanyaan untuk HRD, checklist hari-H"]),
         dict(vis=mock("Tes Excel", "CEK OTOMATIS", ["Soal", "Cek"], [["SUMIFS", '<span class="st g">BENAR ✓</span>'], ["VLOOKUP", '<span class="st g">BENAR ✓</span>'], ["ROUNDUP", '<span class="st r">CEK LAGI</span>']]),
              kick="Excel", h3="Latihan tes Excel + kunci jawaban", p="Kerjakan, dan kolom Cek langsung memberi tahu benar atau belum.",
              ul=["8 soal: SUMIFS, VLOOKUP, IF, COUNTIFS, ROUNDUP, OTIF %, tanggal, pivot table", "Skor otomatis + file kunci berisi rumus", "Bonus cheat sheet Rumus Logistik &amp; KPI Gudang"])],
  steps=STEPS("Pilih CV yang paling mirip posisi incaranmu, lalu latihan interview dan tes Excel."),
  fit=["Fresh graduate atau mahasiswa tingkat akhir", "Ingin pindah karier ke gudang, ekspedisi, PPIC, atau purchasing", "Sudah bekerja dan ingin melamar posisi berikutnya"],
  honest=["Paket ini membantu persiapan, tapi tidak menjamin diterima kerja.", "Contoh jawaban adalah pola, bukan untuk dihafal. Sesuaikan dengan pengalamanmu.", "Nama perusahaan dan angka di contoh CV adalah ilustrasi."],
  offer_sub="Persiapan melamar kerja logistik dari CV sampai tes.",
  offer=["<span><b>Template CV ATS 5 posisi</b> · Word, bisa diedit</span>", "<span><b>2 contoh surat lamaran</b> · email &amp; formal</span>", "<span><b>E-book 50 pertanyaan interview</b> · contoh jawaban + checklist</span>", "<span><b>Latihan tes Excel 8 soal + kunci</b> · cek jawaban otomatis</span>", "<span><b>Bonus 2 cheat sheet</b> · Rumus Logistik &amp; KPI Gudang</span>"],
  format="Word · PDF · Excel",
  faq=[("Posisi apa saja yang ada contoh CV-nya?", "Admin gudang (fresh graduate), staf logistik &amp; ekspedisi, inventory control, PPIC, dan purchasing. Formatnya bisa dipakai juga untuk posisi logistik lain."), ("Apakah cocok untuk fresh graduate?", "Cocok. Salah satu contoh CV dibuat khusus untuk fresh graduate dengan pengalaman magang dan organisasi."), ("Format filenya apa?", "CV dan surat lamaran dalam Word (.docx), e-book PDF, dan latihan tes dalam Excel (.xlsx).")],
  final_h2="Lamaran berikutnya, <em>kirim dengan persiapan matang.</em>", final_p="CV ATS 5 posisi, 50 pertanyaan interview, dan latihan tes Excel dalam satu paket."))

# ------------------------------------------------------------------ KAMUS
P.append(dict(slug="kamus-logistik", name="Kamus Logistik", name_html='Kamus <em>Logistik</em>', tag="Kamus Inggris – Indonesia",
  h1="Istilah logistik bahasa Inggris, <em>sekarang langsung paham.</em>",
  lead="250 istilah gudang, pengiriman, ekspor-impor, pengadaan, produksi, KPI, dan sistem, dijelaskan singkat dalam Bahasa Indonesia.",
  checks=["250 istilah dalam 8 bidang", "Padanan/kepanjangan + arti singkat", "Indeks A–Z untuk cari cepat"],
  cta="Ambil kamusnya", cta_offer="Ambil Kamus Logistik",
  story_big="Di briefing pagi, atasan bilang \"cek dulu IRA-nya, lalu follow up POD yang belum balik.\" Kamu mengangguk, lalu diam-diam mencari artinya di Google.",
  story=["Di gudang, di dokumen ekspor-impor, dan di sistem, istilah bahasa Inggris dipakai setiap hari. Penjelasan yang singkat dan berbahasa Indonesia jarang ada di satu tempat."],
  pains=[("Istilah campur aduk", "FIFO, FEFO, cycle count, W/M, demurrage dipakai tanpa dijelaskan."), ("Dokumen bahasa Inggris", "B/L, packing list, dan invoice penuh singkatan."), ("Penjelasan tersebar", "Mencari arti satu per satu memakan waktu.")],
  turn='Kamu tidak perlu menghafal semuanya. Cukup punya <b style="color:var(--ink)">rujukan yang cepat dibuka.</b>',
  vs_h2="Belajar istilah <em>sebelum dan sesudah</em>",
  before=["Mencari arti istilah satu per satu", "Penjelasan dalam bahasa Inggris lagi", "Istilah gudang dan ekspor-impor bercampur", "Bingung singkatan di dokumen"],
  after=["250 istilah dalam satu PDF", "Arti singkat dalam Bahasa Indonesia", "Dikelompokkan per bidang dan diurutkan A–Z", "Indeks A–Z dan bisa dicari dengan Ctrl+F"],
  items_h2="250 istilah, <em>8 bidang</em>",
  items=[dict(vis=["kamus-isi"], kick="PDF A5", h3="Isi kamus", p="Setiap istilah: istilah asli, padanan atau kepanjangan, dan arti singkat.",
              ul=["Gudang &amp; Inventory (68 istilah)", "Transportasi &amp; Pengiriman (45)", "Ekspor-Impor &amp; Kepabeanan (49)", "Pengadaan &amp; Supply Chain (26)", "Produksi &amp; PPIC (17)", "KPI, Biaya &amp; Analisis (18) · Teknologi &amp; Sistem (13) · Kemasan, K3 &amp; Handling (14)", "Indeks A–Z"])],
  steps=STEPS("Simpan PDF di HP, buka saat ketemu istilah baru."),
  fit=["Staf baru di gudang, ekspedisi, PPIC, atau purchasing", "Mahasiswa logistik dan supply chain", "Sedang persiapan interview atau membaca dokumen berbahasa Inggris"],
  honest=["Ini kamus ringkas, bukan buku teks. Setiap istilah dijelaskan singkat.", "Untuk aturan resmi (misalnya kepabeanan), tetap cek ketentuan terbaru dari instansi terkait."],
  offer_sub="Rujukan istilah logistik yang cepat dibuka.",
  offer=["<span><b>250 istilah</b> · Inggris → Indonesia</span>", "<span><b>8 bidang</b> · gudang sampai sistem</span>", "<span><b>Indeks A–Z</b> · bisa Ctrl+F</span>"],
  format="PDF A5",
  faq=[("Formatnya apa?", "PDF ukuran A5, nyaman dibaca di HP dan bisa dicari dengan Ctrl+F."), ("Bedanya dengan glosarium gratis di situs ini?", "Kamus ini berisi 250 istilah dalam satu PDF yang bisa disimpan dan dibuka tanpa internet, dikelompokkan per bidang dengan indeks A–Z.")],
  final_h2="Istilah berikutnya, <em>tidak perlu googling lagi.</em>", final_p="250 istilah logistik dalam Bahasa Indonesia, satu PDF."))

# ------------------------------------------------------------------ CHEAT SHEET
P.append(dict(slug="cheat-sheet-logistik", name="Cheat Sheet Logistik", name_html='Cheat Sheet <em>Logistik</em>', tag="10 lembar siap print",
  h1="Materi logistik penting, <em>sekali lihat langsung paham.</em>",
  lead="10 lembar ringkasan siap print plus versi gambar untuk HP: Incoterms, kontainer, simbol kemasan, dokumen ekspor-impor, jalur Bea Cukai, rumus, barang berbahaya, armada, satuan, dan KPI.",
  checks=["10 lembar A4 siap print", "10 gambar PNG untuk disimpan di HP", "Bahasa Indonesia, dengan contoh angka"],
  cta="Ambil cheat sheet-nya", cta_offer="Ambil Cheat Sheet",
  story_big="Customer bertanya \"kalau FOB, risikonya pindah kapan?\" atau \"kontainer 20 feet muat berapa CBM?\" Jawabannya ada, tapi tersebar di puluhan artikel.",
  story=["Saat butuh cepat, yang diperlukan adalah satu lembar ringkas yang bisa langsung dilihat, bukan artikel panjang."],
  pains=[("Materi tersebar", "Incoterms, ukuran kontainer, dan rumus ada di sumber yang berbeda-beda."), ("Lupa rumus", "CBM, ROP, safety stock, OTIF harus dicari ulang setiap kali dipakai."), ("Sulit dijelaskan", "Menjelaskan ke rekan atau customer tanpa bahan visual.")],
  turn='Yang kamu butuhkan: <b style="color:var(--ink)">ringkasan yang selalu ada di dekatmu.</b>',
  vs_h2="Mencari materi <em>sebelum dan sesudah</em>",
  before=["Membuka banyak tab untuk satu jawaban", "Mencari ulang rumus yang sama", "Menjelaskan tanpa tabel atau gambar"],
  after=["10 topik inti dalam 10 lembar", "13 rumus lengkap dengan contoh angka", "Tempel di dinding gudang atau simpan di HP"],
  items_h2="10 topik, <em>10 lembar</em>",
  items=[dict(vis=["cs-incoterms", "cs-simbol"], kick="PDF A4 + PNG", h3="Isi cheat sheet", p="Setiap lembar satu topik, ringkas dan siap print.",
              ul=["Incoterms® 2020 (11 aturan) dan ukuran kontainer 20', 40', 40' HC, reefer", "10 simbol kemasan ISO 780 dan dokumen ekspor-impor", "Jalur pengeluaran barang impor (merah, hijau, MITA)", "13 rumus logistik dan 9 kelas barang berbahaya", "Armada darat, satuan &amp; palet, serta 13 KPI gudang &amp; pengiriman"])],
  steps=STEPS("Cetak lembar yang paling sering kamu butuhkan, simpan versi gambar di HP."),
  fit=["Bekerja di gudang, ekspedisi, atau ekspor-impor", "Mahasiswa atau sedang persiapan interview", "Suka belajar dari ringkasan visual"],
  honest=["Ini ringkasan, bukan pengganti aturan resmi. Ketentuan kepabeanan bisa berubah, jadi tetap cek sumber resmi.", "Ukuran kontainer dan armada adalah angka umum; cek spesifikasi carrier atau vendor sebelum booking."],
  offer_sub="Ringkasan materi logistik untuk print dan HP.",
  offer=["<span><b>10 lembar A4</b> · siap print</span>", "<span><b>10 gambar PNG</b> · untuk disimpan di HP</span>", "<span><b>13 rumus</b> dengan contoh angka</span>"],
  format="PDF + PNG",
  faq=[("Bedanya dengan halaman cheat sheet gratis di situs ini?", "Versi ini berisi 10 lembar desain siap print dalam satu PDF, plus 10 gambar untuk HP, dengan topik tambahan seperti dokumen ekspor-impor, jalur impor, simbol kemasan, dan barang berbahaya."), ("Formatnya apa?", "PDF A4 (10 lembar) dan 10 gambar PNG.")],
  final_h2="Jawaban cepat, <em>selalu ada di dekatmu.</em>", final_p="10 lembar ringkasan logistik, siap print dan siap disimpan di HP."))

# ------------------------------------------------------------------ MEGA BUNDLE
P.append(dict(slug="mega-bundle-logistik", name="Mega Bundle", name_html='Mega <em>Bundle</em>', tag="Paket hemat semua produk", bundle=True,
  old="Total harga satuan Rp252.000",
  h1="Semua alat kerja logistik, <em>satu paket hemat.</em>",
  lead="6 produk Ngerti Logistik untuk gudang, ekspedisi, online seller, dan persiapan karier. Total harga satuan Rp252.000.",
  checks=["6 produk: template Excel, e-book, SOP, kamus, cheat sheet", "Untuk gudang, ekspedisi, seller, dan karier", "Hemat Rp103.000 dibanding beli satuan"],
  cta="Ambil Mega Bundle", cta_offer="Ambil Mega Bundle",
  story_big="Kerja di logistik jarang cuma satu urusan. Hari ini menghitung stok, besok membuat penawaran ongkir, lusa menjelaskan Incoterms ke rekan baru.",
  story=["Membeli alat satu per satu saat dibutuhkan memang bisa, tapi totalnya lebih mahal dan prosesnya terpotong-potong."],
  pains=[("Gudang", "Stok, kartu stok, opname, SOP, dan form."), ("Pengiriman &amp; jualan", "Quotation, tracker, invoice, serta laba per channel."), ("Belajar &amp; karier", "Kamus, cheat sheet, CV, dan latihan interview.")],
  turn='Semua alatnya sudah ada. Di bundle ini <b style="color:var(--ink)">kamu mendapat semuanya sekaligus.</b>',
  vs_h2="Beli satuan <em>vs bundle</em>",
  before=["Total harga satuan Rp252.000", "Beli satu per satu saat butuh", "File tersebar di beberapa unduhan"],
  after=["Cukup bayar {{HARGA}}", "Semua alat siap sejak awal", "Satu file ZIP, rapi per produk"],
  items_h2="6 produk <em>dalam satu ZIP</em>",
  items=[dict(vis=["toolkit-gudang-pro-cover"], kick="Rp47.000", h3="Toolkit Gudang Pro", p="Excel 9-in-1, e-book panduan admin gudang 21 halaman, 8 SOP + 8 form.", ul=["Stok, kartu stok, opname, ABC, ROP, kubikasi, dashboard KPI"]),
         dict(vis=["toolkit-ekspedisi-cover"], kick="Rp79.000", h3="Toolkit Ekspedisi &amp; Forwarder", p="Quotation, tracker, invoice, dashboard, LCL vs FCL.", ul=["Bonus 3 cheat sheet"]),
         dict(vis=["stok-cuan-seller-cover"], kick="Rp39.000", h3="Stok &amp; Cuan Online Seller", p="Laba per channel, stok multi-gudang, kalkulator harga.", ul=["Template Excel 10 sheet"]),
         dict(vis=["lolos-kerja-logistik-cover"], kick="Rp39.000", h3="Paket Lolos Kerja Logistik", p="CV ATS 5 posisi, 50 pertanyaan interview, tes Excel + kunci.", ul=["Bonus 2 cheat sheet"]),
         dict(vis=["kamus-logistik-cover"], kick="Rp29.000", h3="Kamus Logistik EN–ID", p="250 istilah dalam 8 bidang + indeks A–Z.", ul=["PDF A5"]),
         dict(vis=["cheat-sheet-logistik-cover"], kick="Rp19.000", h3="Cheat Sheet Logistik", p="10 lembar A4 + versi gambar untuk HP.", ul=["Incoterms, kontainer, rumus, KPI, dan lainnya"])],
  steps=STEPS("Mulai dari produk yang paling kamu butuhkan minggu ini."),
  fit=["Bekerja di gudang atau ekspedisi dan ingin semua alatnya", "Mengelola usaha yang menyimpan stok dan mengirim barang", "Ingin belajar logistik sekaligus menyiapkan karier"],
  honest=["Isi bundle sama persis dengan produk satuan; tidak ada produk tambahan khusus bundle.", "Template berbentuk Excel, bukan aplikasi. Angka di dalam file adalah contoh."],
  offer_sub="Semua produk Ngerti Logistik, satu kali bayar.",
  offer=["Toolkit Gudang Pro<span>Rp47.000</span>", "Toolkit Ekspedisi &amp; Forwarder<span>Rp79.000</span>", "Stok &amp; Cuan Online Seller<span>Rp39.000</span>", "Paket Lolos Kerja Logistik<span>Rp39.000</span>", "Kamus Logistik EN–ID<span>Rp29.000</span>", "Cheat Sheet Logistik<span>Rp19.000</span>"],
  format="Excel · PDF · Word",
  faq=[("Apakah isinya sama dengan produk satuan?", "Sama persis. Bundle berisi keenam produk lengkap dengan bonusnya."), ("Saya sudah membeli salah satu produk, bagaimana?", "Bundle tetap berisi semua produk. Kalau ingin menyesuaikan, kirim DM ke @ngertilogistik sebelum membeli.")],
  final_h2="Semua alat kerja logistik, <em>sekali bayar.</em>", final_p="6 produk untuk gudang, ekspedisi, online seller, dan karier dalam satu paket."))

# ------------------------------------------------------------------ SIMULASI ADMIN GUDANG
P.append(dict(slug="simulasi-admin-gudang", name="Simulasi Admin Gudang", name_html='Simulasi <em>Admin Gudang</em>', tag="Simulasi interaktif",
  h1="Rasakan seminggu jadi admin gudang <em>sebelum hari pertama kerja.</em>",
  lead="20 kasus nyata dalam 5 hari kerja: surat jalan tidak sesuai, stok selisih, kiriman terlambat, dan hitungan yang harus cepat. Pilih tindakanmu, lalu lihat pembahasannya.",
  checks=["5 hari kerja · 20 kasus · ada pembahasan", "Main di HP atau laptop, tanpa internet", "Skor, predikat, dan daftar materi yang perlu diulang"],
  cta="Coba jadi admin gudang", cta_offer="Ambil Simulasinya",
  story_big="Kamu sudah baca soal FIFO, stock opname, dan surat jalan. Tapi saat sopir minta tanda tangan cepat dan jumlah barang kurang 2 dus, apa yang sebenarnya harus kamu lakukan?",
  story=["Teori gudang mudah ditemukan. Yang jarang ada adalah latihan mengambil keputusan di situasi nyata, lengkap dengan alasan kenapa satu tindakan lebih tepat dari yang lain."],
  pains=[("Paham teori, bingung praktik", "Tahu istilahnya, tapi ragu saat harus memutuskan di lapangan."), ("Kesalahan mahal", "Salah tanda tangan surat jalan atau salah hitung stok bisa jadi kerugian perusahaan."), ("Belajar dari video saja", "Menonton tidak sama dengan mencoba menjawab sendiri.")],
  turn='Cara tercepat paham pekerjaan gudang adalah <b style="color:var(--ink)">mencoba memutuskan, lalu melihat pembahasannya.</b>',
  vs_h2="Belajar gudang <em>sebelum dan sesudah</em>",
  before=["Membaca teori tanpa latihan", "Tidak tahu bagian mana yang masih lemah", "Kaget saat menghadapi masalah pertama di tempat kerja", "Hitungan CBM dan akurasi stok terasa asing"],
  after=["20 keputusan kerja yang kamu jawab sendiri", "Skor per hari kerja dan daftar materi yang perlu diulang", "Sudah pernah \"mengalami\" kasus yang umum terjadi", "Latihan hitung karton, kubikasi, berat volumetrik, dan akurasi stok"],
  items_h2="Satu minggu kerja, <em>dalam satu file</em>",
  items=[dict(vis=["sim-case", "sim-map"], kick="Kasus", h3="5 hari kerja, 20 kasus", p="Setiap hari punya tema sendiri. Hari berikutnya terbuka setelah hari sebelumnya selesai.",
              ul=["Hari 1 · Penerimaan barang: surat jalan, kelebihan kirim, ED, hitung per lapis", "Hari 2 · Penyimpanan: slotting, FEFO, kode lokasi, kubikasi", "Hari 3 · Picking &amp; packing: short pick, barang mirip, berat volumetrik", "Hari 4 · Pengiriman: muat truk, keterlambatan, POD", "Hari 5 · Stock opname &amp; selisih: akurasi stok dan penelusuran selisih"]),
         dict(vis=["sim-result", "sim-start"], kick="Hasil", h3="Pembahasan, skor, dan kartu hasil", p="Setelah menjawab, kamu langsung tahu benar atau belum, dan kenapa.",
              ul=["Pembahasan singkat di setiap kasus", "Skor per hari dan predikat akhir", "Daftar materi yang perlu diulang", "Kartu hasil yang bisa dicetak (kartu latihan, bukan sertifikat resmi)", "Progres tersimpan otomatis di browser"])],
  steps=STEPS("Isi nama, mulai hari pertama, dan selesaikan 5 hari kerja."),
  fit=["Pelamar atau calon admin gudang", "Staf gudang baru yang ingin cepat paham alur kerja", "Leader atau HR yang butuh bahan latihan staf baru", "Mahasiswa logistik"],
  honest=["Kasus dan angka adalah ilustrasi untuk latihan; prosedur tiap perusahaan bisa berbeda.", "Kartu hasil adalah kartu latihan, bukan sertifikat resmi.", "Ini file HTML yang dibuka di browser, bukan aplikasi dari Play Store/App Store."],
  offer_sub="Latihan mengambil keputusan kerja gudang.",
  offer=["<span><b>Simulasi 5 hari kerja</b> · 20 kasus pilihan &amp; hitungan</span>", "<span><b>Pembahasan setiap kasus</b> · langsung setelah menjawab</span>", "<span><b>Skor, predikat &amp; materi ulang</b> · tahu bagian yang masih lemah</span>", "<span><b>Kartu hasil siap print</b> · kartu latihan</span>"],
  format="File HTML (offline)",
  faq=[("Bagaimana cara membukanya?", "Unduh dan ekstrak ZIP, lalu buka file .html di Chrome, Edge, Safari, atau browser lain. Bisa di HP maupun laptop, dan tidak perlu internet."), ("Apakah perlu install aplikasi?", "Tidak. Simulasi berjalan di browser yang sudah ada di HP atau laptopmu."), ("Kalau berhenti di tengah, progresnya hilang?", "Tidak, progres tersimpan otomatis di browser yang sama. Kalau pindah HP atau browser, mulai lagi dari awal."), ("Bisa dipakai untuk melatih staf?", "Bisa, untuk staf di tempat kerja pembeli. File tidak boleh dijual ulang atau dibagikan ke luar.")],
  final_h2="Hari pertama kerja, <em>rasanya sudah pernah.</em>", final_p="20 kasus nyata admin gudang dengan pembahasan, bisa dimainkan di HP."))

# ------------------------------------------------------------------ BRIEFING PAGI
P.append(dict(slug="briefing-pagi-gudang", name="Briefing Pagi Gudang", name_html='Briefing Pagi <em>Gudang</em>', tag="Untuk supervisor &amp; leader",
  h1="Briefing pagi 5 menit, <em>tanpa bingung mau bahas apa.</em>",
  lead="30 naskah toolbox meeting siap baca: K3, operasional, dan kerja tim. Setiap topik sudah ada pembuka, poin bicara, contoh kasus, pertanyaan untuk tim, dan aksi hari ini.",
  checks=["30 topik, satu halaman per topik", "± 5 menit, tinggal dibacakan", "Plus daftar hadir, jadwal bulanan, dan form near miss"],
  cta="Ambil 30 naskahnya", cta_offer="Ambil Materi Briefing",
  story_big="Jam 07.55. Tim sudah berbaris, kamu yang harus bicara. Kemarin sudah bahas APD, kemarin lusa juga. Hari ini mau bahas apa lagi?",
  story=["Briefing pagi seharusnya jadi waktu terbaik untuk mengingatkan tim soal keselamatan dan kualitas kerja. Tapi menyiapkan materi baru setiap hari itu melelahkan, sehingga isinya sering berulang dan tim berhenti mendengarkan."],
  pains=[("Materi itu-itu saja", "Tim hafal isinya, lalu tidak lagi memperhatikan."), ("Tidak sempat menyiapkan", "Pekerjaan sudah menunggu sebelum briefing dimulai."), ("Satu arah", "Leader bicara, tim diam, tidak ada tindak lanjut.")],
  turn='Briefing yang baik itu <b style="color:var(--ink)">singkat, ada contohnya, dan berakhir dengan aksi.</b>',
  vs_h2="Briefing pagi <em>sebelum dan sesudah</em>",
  before=["Topik dipikirkan dadakan", "Isi berulang setiap minggu", "Tim hanya mendengar", "Tidak ada catatan kehadiran dan tindak lanjut"],
  after=["30 topik terjadwal untuk satu bulan kerja lebih", "K3, operasional, tim, dan musiman bergantian", "2 pertanyaan untuk mengajak tim bicara", "Daftar hadir, kolom catatan, dan form near miss"],
  items_h2="30 topik, <em>siap dibacakan</em>",
  items=[dict(vis=["br-topik"], kick="Naskah", h3="Satu topik, satu halaman", p="Alurnya sama di setiap topik sehingga mudah dibawakan siapa saja.",
              ul=["Tujuan dan kalimat pembuka untuk dibacakan", "4 poin bicara", "Contoh kasus di gudang", "2 pertanyaan untuk tim dan 3 aksi hari ini", "Kolom catatan leader dan tindak lanjut"]),
         dict(vis=["br-daftar"], kick="Topik", h3="K3, operasional, tim, dan musiman", p="Bisa dipakai berurutan atau dipilih sesuai kejadian di gudang.",
              ul=["10 topik K3: APD, angkat manual, forklift, APAR &amp; evakuasi, rak, tumpahan, barang berbahaya, kelelahan, near miss, listrik", "12 topik operasional: receiving, FIFO/FEFO, dokumen, picking, packing, label, lokasi, retur, barang rusak, muat truk, opname, serah terima shift", "6 topik tim + 2 topik musiman (musim sibuk dan musim hujan)"]),
         dict(vis=["br-nearmiss"], kick="Form", h3="3 form siap print", p="Supaya briefing tercatat dan ada tindak lanjutnya.",
              ul=["Daftar hadir briefing pagi", "Jadwal topik briefing bulanan", "Form laporan near miss"])],
  steps=STEPS("Print atau buka di HP, pilih topik hari ini, dan bacakan."),
  fit=["Supervisor, leader, dan kepala gudang", "Petugas K3 atau HSE di gudang dan pusat distribusi", "Leader baru yang belum terbiasa memimpin briefing"],
  honest=["Materi K3 bersifat umum. Sesuaikan dengan prosedur dan aturan K3 di perusahaanmu.", "Contoh kasus adalah ilustrasi; lebih baik lagi bila diganti dengan kejadian di gudangmu sendiri."],
  offer_sub="Bahan briefing pagi untuk lebih dari satu bulan kerja.",
  offer=["<span><b>30 naskah briefing</b> · ± 5 menit per topik</span>", "<span><b>Panduan alur briefing 5 menit</b> · dan tips untuk leader</span>", "<span><b>3 form siap print</b> · daftar hadir, jadwal, near miss</span>"],
  format="PDF A4 (35 halaman)",
  faq=[("Formatnya apa?", "PDF A4 35 halaman. Bisa dibaca dari HP atau dicetak."), ("Boleh diperbanyak untuk tim?", "Form boleh diperbanyak untuk internal perusahaan pembeli. File tidak boleh dijual ulang atau dibagikan ke luar."), ("Apakah sesuai aturan K3 resmi?", "Isinya praktik K3 umum di gudang, bukan pengganti prosedur atau aturan resmi. Tetap ikuti ketentuan di perusahaanmu.")],
  final_h2="Besok pagi, <em>tinggal buka topik berikutnya.</em>", final_p="30 naskah briefing pagi gudang plus 3 form siap print."))

for p in P:
    open(os.path.join(ROOT, "content/halaman", p["slug"] + ".html"), "w", encoding="utf-8").write(page(p))
    print("ok", p["slug"])
