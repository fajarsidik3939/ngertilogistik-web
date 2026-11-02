#!/usr/bin/env python3
"""Generator situs statis Ngerti Logistik.
Sumber: data/topics.json  ->  public/ (siap di-deploy ke Vercel)
Jalankan: python3 build.py
"""
import json, re, html, os, shutil, datetime

SITE = "https://ngertilogistik.web.id"
TIKTOK = "https://www.tiktok.com/@ngertilogistik"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
T = json.load(open(os.path.join(ROOT, "data/topics.json"), encoding="utf-8"))

PILAR = {
    "P0": ("Perkenalan", "Kenalan dengan dunia logistik."),
    "P1": ("Kamus 60 Detik", "Istilah logistik dijelaskan singkat dan jelas."),
    "P2": ("Isi Gudang", "Apa yang sebenarnya terjadi di dalam gudang."),
    "P3": ("Kirim Tanpa Drama", "Pengiriman, ongkir, dan cara barang sampai dengan aman."),
    "P4": ("Salah Kaprah", "Anggapan keliru yang sering terdengar soal logistik."),
    "P5": ("Karier & Skill", "Peran, keterampilan, dan jalur karier di logistik."),
}
ORDER = ["P1", "P2", "P3", "P4", "P5", "P0"]

def esc(s): return html.escape(s, quote=True)
def em(s): return re.sub(r"\*(.+?)\*", r"<em>\1</em>", esc(s))
def plain(s): return s.replace("*", "")
def slug(t):
    s = t["topic"].lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60].strip("-")
    return f"{t['id'].lower()}-{s}"
for t in T: t["slug"] = slug(t)

def head(title, desc, path, img="/img/og.png", extra=""):
    return f"""<!doctype html><html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Ngerti Logistik">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{path}"><meta property="og:image" content="{SITE}{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1220">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">{extra}</head><body>"""

NAV = f"""<header class="nav"><div class="wrap nav-in">
<a class="brand" href="/"><img src="/img/logo-256.png" alt="" width="36" height="36"><span>Ngerti <b>Logistik</b></span></a>
<nav><a href="/#materi">Materi</a><a href="/#pilar">Pilar</a><a href="/tentang">Tentang</a>
<a class="btn-sm" href="{TIKTOK}" target="_blank" rel="noopener">Follow</a></nav></div></header>"""

FOOT = f"""<footer class="foot"><div class="wrap foot-in">
<div><a class="brand" href="/"><img src="/img/logo-256.png" alt="" width="32" height="32"><span>Ngerti <b>Logistik</b></span></a>
<p>Belajar logistik dari nol, satu materi singkat setiap kali. Konten edukasi, gratis untuk semua.</p></div>
<div class="foot-links"><a href="/#materi">Semua materi</a><a href="/tentang">Tentang</a><a href="{TIKTOK}" target="_blank" rel="noopener">TikTok @ngertilogistik</a></div>
</div><div class="wrap fine">Contoh angka yang ditandai CONTOH adalah ilustrasi, bukan data nyata. Fakta di dalam materi menyebut sumbernya di naskah.</div></footer>
</body></html>"""

CTA = f"""<section class="cta"><div class="wrap cta-in"><div>
<h2>Mau belajar logistik <em>lebih dalam?</em></h2><p>Follow Ngerti Logistik di TikTok, Instagram Reels, dan Facebook Reels. Video baru tayang rutin.</p></div>
<a class="btn" href="{TIKTOK}" target="_blank" rel="noopener">Follow @ngertilogistik</a></div></section>"""

def card(t):
    return f"""<a class="card" href="/materi/{t['slug']}" data-p="{t['pillar']}" data-q="{esc((plain(t['title'])+' '+t['topic']+' '+t['sub']+' '+t['kicker']).lower())}">
<div class="thumb"><img src="/img/c/{t['id'].lower()}.webp" alt="" loading="lazy" width="540" height="960"><span class="no">#{t['n']:03d}</span></div>
<div class="cbody"><span class="kick">{esc(PILAR[t['pillar']][0])}</span><h3>{em(t['title'])}</h3><p>{esc(t['sub'])}</p></div></a>"""

# ---------- index ----------
def build_index():
    counts = {p: sum(1 for t in T if t["pillar"] == p) for p in PILAR}
    chips = '<button class="chip on" data-f="all">Semua <i>%d</i></button>' % len(T) + "".join(
        f'<button class="chip" data-f="{p}">{esc(PILAR[p][0])} <i>{counts[p]}</i></button>' for p in ORDER)
    pil = "".join(f"""<button class="pil" data-f="{p}"><span class="pn">{p}</span><h3>{esc(PILAR[p][0])}</h3><p>{esc(PILAR[p][1])}</p><span class="pc">{counts[p]} materi →</span></button>""" for p in ORDER)
    feat = [t for t in T if t["id"] in ("L01", "L06", "L61")]
    grid = "".join(card(t) for t in T)
    h = head("Ngerti Logistik · Belajar logistik dari nol",
             "120 materi logistik singkat: istilah, isi gudang, pengiriman, salah kaprah, dan karier. Dijelaskan sederhana oleh praktisi logistik.", "/")
    h += NAV + f"""
<section class="hero"><div class="wrap hero-in">
<div class="hero-tx">
<span class="eyebrow">Edukasi logistik · gratis</span>
<h1>Logistik itu <em>bisa dimengerti.</em></h1>
<p class="lead">Dari istilah gudang sampai kenapa ongkir barang ringan bisa mahal. {len(T)} materi singkat, masing-masing selesai dibaca dalam satu menit.</p>
<div class="hero-act"><a class="btn" href="#materi">Mulai belajar</a><a class="btn ghost" href="/materi/{T[0]['slug']}">Apa itu logistik?</a></div>
<dl class="stats"><div><dt>{len(T)}</dt><dd>materi</dd></div><div><dt>6</dt><dd>pilar</dd></div><div><dt>±60 dtk</dt><dd>per materi</dd></div></dl>
</div>
<div class="hero-art" aria-hidden="true">{''.join(f'<img src="/img/c/{t["id"].lower()}.webp" alt="" width="540" height="960">' for t in feat)}</div>
</div><div class="route" aria-hidden="true"></div></section>

<section id="pilar" class="sec"><div class="wrap">
<div class="sec-h"><span class="eyebrow">6 pilar</span><h2>Pilih dari mana mau mulai</h2></div>
<div class="pils">{pil}</div></div></section>

<section id="materi" class="sec alt"><div class="wrap">
<div class="sec-h"><span class="eyebrow">Perpustakaan</span><h2>Semua materi</h2></div>
<div class="tools"><label class="search"><svg viewBox="0 0 24 24" width="20" height="20"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="m20 20-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
<input id="q" type="search" placeholder="Cari: SKU, FIFO, ongkir, Incoterms…" autocomplete="off"></label>
<div class="chips">{chips}</div></div>
<p id="count" class="count" aria-live="polite"></p>
<div id="grid" class="grid">{grid}</div>
<p id="empty" class="empty" hidden>Belum ada materi yang cocok. Coba kata lain.</p>
</div></section>
""" + CTA + FOOT.replace("</body>", "<script src=\"/app.js\" defer></script></body>")
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(h)

# ---------- halaman materi ----------
def build_pages():
    for i, t in enumerate(T):
        prev = T[i - 1] if i else None
        nxt = T[i + 1] if i + 1 < len(T) else None
        rel = [x for x in T if x["pillar"] == t["pillar"] and x["id"] != t["id"]]
        k = [x["id"] for x in rel].index(nxt["id"]) if nxt and nxt in rel else 0
        rel = (rel[k:] + rel[:k])[:3]
        body = "".join(f'<p class="{"contoh" if v.startswith("Contoh") else ""}">{esc(v)}</p>' for v in t["vo"])
        title = f"{plain(t['title'])} · Ngerti Logistik"
        desc = t["key"] if len(t["key"]) > 40 else f"{t['topic']}. {t['key']}"
        ld = json.dumps({"@context": "https://schema.org", "@type": "LearningResource", "name": plain(t["title"]),
                         "description": t["key"], "inLanguage": "id", "isAccessibleForFree": True,
                         "learningResourceType": "Materi singkat", "about": PILAR[t["pillar"]][0],
                         "publisher": {"@type": "Organization", "name": "Ngerti Logistik", "url": SITE}}, ensure_ascii=False)
        h = head(title, desc, f"/materi/{t['slug']}", f"/img/c/{t['id'].lower()}.webp",
                 f'<script type="application/ld+json">{ld}</script>')
        nav = ""
        if prev: nav += f'<a class="pn-l" href="/materi/{prev["slug"]}"><small>← Sebelumnya</small><span>{em(prev["title"])}</span></a>'
        else: nav += "<span></span>"
        if nxt: nav += f'<a class="pn-r" href="/materi/{nxt["slug"]}"><small>Berikutnya →</small><span>{em(nxt["title"])}</span></a>'
        h += NAV + f"""
<main class="art"><div class="wrap art-in">
<aside class="art-cover"><img src="/img/c/{t['id'].lower()}.webp" alt="Sampul materi {esc(plain(t['title']))}" width="540" height="960"></aside>
<article>
<nav class="crumb"><a href="/">Beranda</a> / <a href="/?p={t['pillar']}#materi">{esc(PILAR[t['pillar']][0])}</a> / <span>#{t['n']:03d}</span></nav>
<span class="eyebrow">{esc(t['kicker'])}</span>
<h1>{em(t['title'])}</h1>
<p class="sub">{esc(t['sub'])}</p>
<div class="key"><span>Intinya</span><p>{esc(t['key'])}</p></div>
<h2 class="nh">Penjelasan lengkap</h2>
<div class="prose">{body}</div>
<a class="watch" href="{TIKTOK}" target="_blank" rel="noopener"><span class="play">▶</span><span><b>Tonton versi videonya</b><small>di TikTok @ngertilogistik</small></span></a>
<div class="pn">{nav}</div>
</article></div>
<section class="rel"><div class="wrap"><h2>Materi lain di pilar {esc(PILAR[t['pillar']][0])}</h2><div class="grid g3">{''.join(card(x) for x in rel)}</div></div></section>
</main>""" + CTA + FOOT
        d = os.path.join(OUT, "materi", t["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(h)

def build_about():
    h = head("Tentang · Ngerti Logistik", "Ngerti Logistik adalah akun edukasi logistik yang menjelaskan dunia gudang, pengiriman, dan supply chain dengan bahasa sederhana.", "/tentang")
    h += NAV + f"""<main class="about"><div class="wrap narrow">
<span class="eyebrow">Tentang</span><h1>Belajar logistik <em>tanpa ribet.</em></h1>
<p class="lead">Ngerti Logistik adalah akun edukasi yang menjelaskan logistik dengan bahasa sehari-hari. Setiap materi membahas satu hal saja, cukup singkat untuk dipahami dalam satu menit.</p>
<h2>Siapa di baliknya?</h2>
<p>Ngerti Logistik dibuat oleh Fajar, praktisi logistik yang sudah sekitar sepuluh tahun bekerja di bidang ini, di industri teknologi, FMCG, dan manufaktur. Materinya disusun dari pengalaman lapangan dan rujukan yang bisa dicek.</p>
<h2>Prinsip konten</h2>
<ul class="ticks">
<li><b>Satu materi, satu ide.</b> Tidak bertele-tele.</li>
<li><b>Fakta bersumber.</b> Angka dan kejadian nyata disebut sumber dan waktunya.</li>
<li><b>Contoh ditandai.</b> Ilustrasi angka diberi label CONTOH supaya tidak tertukar dengan data nyata.</li>
<li><b>Netral.</b> Tidak membahas atau mempromosikan perusahaan tertentu.</li>
<li><b>Gratis.</b> Murni edukasi, tanpa iklan dan tanpa jualan.</li>
</ul>
<h2>Untuk siapa?</h2>
<p>Pelajar dan mahasiswa yang penasaran, pekerja baru di gudang atau pengiriman, pelaku UMKM yang mengirim barang setiap hari, dan siapa saja yang ingin tahu bagaimana barang bisa sampai ke tangan kita.</p>
<p><a class="btn" href="/#materi">Lihat semua materi</a></p>
</div></main>""" + CTA + FOOT
    d = os.path.join(OUT, "tentang"); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(h)

def build_misc():
    h = head("Halaman tidak ditemukan · Ngerti Logistik", "Halaman tidak ditemukan.", "/404")
    h += NAV + """<main class="about"><div class="wrap narrow" style="text-align:center">
<span class="eyebrow">404</span><h1>Paket ini <em>salah alamat.</em></h1><p class="lead">Halaman yang dicari tidak ada. Mungkin sudah pindah rak.</p>
<p><a class="btn" href="/">Kembali ke beranda</a></p></div></main>""" + FOOT
    open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(h)
    today = datetime.date.today().isoformat()
    urls = ["/", "/tentang"] + [f"/materi/{t['slug']}" for t in T]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(
        f"<url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>" for u in urls) + "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")

if __name__ == "__main__":
    shutil.rmtree(os.path.join(OUT, "materi"), ignore_errors=True)
    build_index(); build_pages(); build_about(); build_misc()
    print("OK", len(T), "materi")
