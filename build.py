import re
#!/usr/bin/env python3
"""Generator blog statis Ngerti Logistik.

Sumber : content/artikel/*.md  (frontmatter YAML + isi Markdown)
Keluaran: public/              (di-deploy apa adanya oleh Vercel)

Jalankan: python3 build.py
Hanya artikel yang ada file .md-nya yang terbit. Materi lain tetap tersembunyi.
"""
import os, re, sys, json, html, glob, shutil, datetime, subprocess
import yaml, markdown
import belajar

SITE = "https://ngertilogistik.web.id"
NAME = "Ngerti Logistik"
TIKTOK = "https://www.tiktok.com/@ngertilogistik"
BASE = "/blog"            # awalan URL artikel
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
WPM = 200                 # kecepatan baca (kata/menit)

AUTHOR = {
    "nama": "Fajar",
    "slug": "fajar",
    "peran": "Praktisi logistik",
    "bio": "Praktisi logistik dengan sekitar sepuluh tahun pengalaman di industri teknologi, FMCG, dan manufaktur. "
           "Menulis Ngerti Logistik supaya urusan gudang dan pengiriman bisa dipahami siapa saja.",
}

# kategori = 6 pilar. Bisa ditimpa oleh content/kategori.yml
KATEGORI = {
    "kamus-logistik": dict(pilar="P1", nama="Kamus Logistik", judul="Kamus Logistik: Istilah Gudang & Pengiriman Dijelaskan",
                           desk="Arti istilah logistik, gudang, dan supply chain dijelaskan singkat dengan contoh sehari-hari."),
    "manajemen-gudang": dict(pilar="P2", nama="Manajemen Gudang", judul="Manajemen Gudang: Proses di Dalam Gudang",
                             desk="Penerimaan, penyimpanan, picking, packing, dan stok. Cara kerja gudang dari dalam."),
    "pengiriman-barang": dict(pilar="P3", nama="Pengiriman Barang", judul="Pengiriman Barang: Ongkir, Moda, dan Tips Aman",
                              desk="Ongkir, berat volume, moda darat-laut-udara, dan cara barang sampai dengan aman."),
    "salah-kaprah-logistik": dict(pilar="P4", nama="Salah Kaprah Logistik", judul="Salah Kaprah Logistik yang Sering Terdengar",
                                  desk="Anggapan keliru soal logistik, stok, dan pengiriman, beserta penjelasan yang benar."),
    "karier-logistik": dict(pilar="P5", nama="Karier Logistik", judul="Karier Logistik: Peran, Skill, dan Jalur Karier",
                            desk="Peran di gudang dan logistik, keterampilan yang dibutuhkan, dan cara memulai karier."),
    "dasar-logistik": dict(pilar="P0", nama="Dasar Logistik", judul="Dasar Logistik untuk Pemula",
                           desk="Mulai dari sini: apa itu logistik dan bagaimana barang sampai ke tangan kita."),
}

def esc(s): return html.escape(str(s), quote=True)

# ---------------------------------------------------------------- data
def load_cfg():
    p = os.path.join(ROOT, "content/kategori.yml")
    if os.path.exists(p):
        KATEGORI.clear(); KATEGORI.update(yaml.safe_load(open(p, encoding="utf-8")))
    global BASE
    p = os.path.join(ROOT, "content/situs.yml")
    if os.path.exists(p):
        c = yaml.safe_load(open(p, encoding="utf-8")) or {}
        BASE = c.get("base", BASE)

def url(a): return f"{BASE}/{a['slug']}" if BASE else f"/{a['slug']}"

def load_articles():
    arts = []
    for f in sorted(glob.glob(os.path.join(ROOT, "content/artikel/*.md"))):
        raw = open(f, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m: raise SystemExit(f"Frontmatter tidak valid: {f}")
        a = yaml.safe_load(m.group(1)); a["body"] = m.group(2).strip()
        for k in ("id", "slug", "judul", "deskripsi", "kategori"):
            if not a.get(k): raise SystemExit(f"{f}: field '{k}' kosong")
        if a["kategori"] not in KATEGORI: raise SystemExit(f"{f}: kategori '{a['kategori']}' tidak dikenal")
        a.setdefault("seo_title", a["judul"]); a.setdefault("faq", []); a.setdefault("sumber", [])
        a.setdefault("kata_kunci", []); a.setdefault("intinya", "")
        a["terbit"] = str(a.get("terbit") or datetime.date.today())
        a["diperbarui"] = str(a.get("diperbarui") or a["terbit"])
        arts.append(a)
    # hanya artikel yang tanggal terbitnya sudah lewat (WIB) yang tayang; sisanya antrean
    today = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=7)).date().isoformat()
    antre = sorted(a["id"] + " " + a["terbit"] for a in arts if a["terbit"] > today)
    if antre: print("Antrean (belum tayang):", ", ".join(antre))
    arts = [a for a in arts if a["terbit"] <= today]
    ids = {a["id"]: a for a in arts}
    for a in arts:
        txt = re.sub(r"[#>*_`\[\]\(\)|-]", " ", a["body"])
        a["kata"] = len(txt.split()) + sum(len((q.get("a") or "").split()) for q in a["faq"])
        a["menit"] = max(1, round(a["kata"] / WPM))
    arts.sort(key=lambda a: (a["terbit"], a["id"]), reverse=True)
    return arts, ids

# ---------------------------------------------------------------- markdown
def slugify(s):
    s = re.sub(r"<[^>]+>", "", s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "bagian"

def render_body(a, ids):
    body = a["body"]
    # link internal: [anchor](L06) -> URL artikel. Jika belum terbit, jadikan teks biasa.
    def repl(m):
        t, ref = m.group(1), m.group(2)
        if ref in ids: return f"[{t}]({url(ids[ref])})"
        return t
    body = re.sub(r"\[([^\]]+)\]\((L\d{2,3})\)", repl, body)
    md = markdown.Markdown(extensions=["tables", "sane_lists", "attr_list"])
    h = md.convert(body)
    toc, used = [], set()
    def hrepl(m):
        lvl, inner = m.group(1), m.group(2)
        sid = slugify(inner); n = 2
        while sid in used: sid = f"{slugify(inner)}-{n}"; n += 1
        used.add(sid)
        toc.append((int(lvl), re.sub(r"<[^>]+>", "", inner), sid))
        return f'<h{lvl} id="{sid}">{inner}</h{lvl}>'
    h = re.sub(r"<h([23])>(.*?)</h\1>", hrepl, h)
    # blockquote berawalan CONTOH -> kotak contoh
    h = re.sub(r"<blockquote>\s*<p><strong>CONTOH(.*?)</strong>", r'<blockquote class="contoh"><p><strong>CONTOH\1</strong>', h)
    # tautan keluar
    h = re.sub(r'<a href="(https?://(?!ngertilogistik\.web\.id)[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    h = h.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    return h, toc

def md_inline(s):
    return markdown.markdown(s or "").removeprefix("<p>").removesuffix("</p>")

# ---------------------------------------------------------------- layout
def tgl(d):
    b = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
    y, m, dd = map(int, d.split("-")); return f"{dd} {b[m-1]} {y}"

def head(title, desc, path, img=None, kind="website", extra="", noindex=False):
    img = img or "/img/og.png"
    return f"""<!doctype html><html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{path}">{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<meta property="og:locale" content="id_ID"><meta property="og:type" content="{kind}"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{path}"><meta property="og:image" content="{SITE}{img}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1220">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="alternate" type="application/rss+xml" title="{NAME}" href="/feed.xml">
<link rel="preload" href="/fonts/jakarta-800.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/serif-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">{extra}</head><body>"""

def nav():
    cats = "".join(f'<a href="/kategori/{k}">{esc(v["nama"])}</a>' for k, v in KATEGORI.items())
    bl = '<a href="/belajar">Jalur belajar</a><a href="/kuis">Kuis</a><a href="/glosarium">Glosarium</a><a href="/cheat-sheet">Cheat sheet</a><a href="/karier">Karier</a>'
    al = '<a href="/produk">Produk premium</a><a href="/toolkit-gudang-pro">Toolkit Gudang Pro</a><a href="/template">Template Excel</a><a href="/kalkulator-logistik">Kalkulator logistik</a><a href="/kalkulator-kubikasi">Kalkulator kubikasi</a>'
    return f"""<a class="skip" href="#isi">Langsung ke isi</a>
<header class="nav"><div class="wrap nav-in">
<a class="brand" href="/"><img src="/img/logo-256.png" alt="" width="34" height="34"><span>Ngerti <b>Logistik</b></span></a>
<nav aria-label="Utama"><a href="{BASE or '/'}">Artikel</a><details class="dd dd-d"><summary>Kategori</summary><div>{cats}</div></details><details class="dd dd-d"><summary>Belajar</summary><div>{bl}</div></details><details class="dd dd-d"><summary>Alat</summary><div>{al}</div></details><a href="/tentang">Tentang</a>
<details class="dd dd-m"><summary>Menu</summary><div><a href="{BASE or '/'}">Semua artikel</a>{bl}{al}<a href="/tentang">Tentang</a></div></details>
<a class="btn-sm" href="{TIKTOK}" target="_blank" rel="noopener">Follow</a></nav></div></header>"""

def foot():
    cats = "".join(f'<a href="/kategori/{k}">{esc(v["nama"])}</a>' for k, v in KATEGORI.items())
    return f"""<footer class="foot"><div class="wrap foot-in">
<div><a class="brand" href="/"><img src="/img/logo-256.png" alt="" width="30" height="30"><span>Ngerti <b>Logistik</b></span></a>
<p>Blog edukasi logistik berbahasa Indonesia. Gudang, pengiriman, dan supply chain dijelaskan dengan bahasa sehari-hari. Gratis, tanpa iklan.</p></div>
<div class="foot-links"><b>Kategori</b>{cats}</div>
<div class="foot-links"><b>Belajar &amp; alat</b><a href="/belajar">Jalur belajar</a><a href="/kuis">Kuis</a><a href="/glosarium">Glosarium</a><a href="/cheat-sheet">Cheat sheet</a><a href="/karier">Karier</a><a href="/produk">Produk premium</a><a href="/toolkit-gudang-pro">Toolkit Gudang Pro</a><a href="/template">Template Excel</a><a href="/kalkulator-logistik">Kalkulator logistik</a><a href="/kalkulator-kubikasi">Kalkulator kubikasi</a></div>
<div class="foot-links"><b>Ngerti Logistik</b><a href="/tentang">Tentang</a><a href="/penulis/{AUTHOR['slug']}">Penulis</a><a href="/feed.xml">RSS</a><a href="{TIKTOK}" target="_blank" rel="noopener">TikTok @ngertilogistik</a></div>
</div><div class="wrap fine">© {datetime.date.today().year} {NAME}. Angka yang ditandai CONTOH adalah ilustrasi, bukan data nyata. Fakta lain disertai sumber di akhir artikel.</div></footer>
</body></html>"""

CTA = f"""<section class="cta"><div class="wrap cta-in"><div>
<h2>Mau belajar logistik <em>lebih dalam?</em></h2><p>Follow Ngerti Logistik di TikTok, Instagram Reels, dan Facebook Reels. Penjelasan singkat setiap minggu.</p></div>
<a class="btn" href="{TIKTOK}" target="_blank" rel="noopener">Follow @ngertilogistik</a></div></section>"""

def share(path, title, where):
    """Tombol bagikan ke media sosial (tanpa skrip pihak ketiga)."""
    from urllib.parse import quote
    u = quote(SITE + path, safe=""); tt = quote(title, safe="")
    links = [("WhatsApp", f"https://wa.me/?text={tt}%20{u}"), ("Facebook", f"https://www.facebook.com/sharer/sharer.php?u={u}"),
             ("X", f"https://twitter.com/intent/tweet?text={tt}&url={u}"), ("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={u}"),
             ("Telegram", f"https://t.me/share/url?url={u}&text={tt}")]
    btn = "".join(f'<a class="sh-{n.lower()}" href="{esc(h)}" target="_blank" rel="noopener nofollow" aria-label="Bagikan ke {n}">{n}</a>' for n, h in links)
    return (f'<div class="share share-{where}" data-url="{esc(SITE + path)}" data-title="{esc(title)}"><span class="share-l">Bagikan</span>{btn}'
            '<button type="button" class="sh-copy">Salin link</button><button type="button" class="sh-native" hidden>Bagikan…</button></div>')

SHARE_JS = """<script>document.querySelectorAll('.share').forEach(function(s){var u=s.dataset.url,t=s.dataset.title,c=s.querySelector('.sh-copy'),n=s.querySelector('.sh-native');
c.onclick=function(){(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(function(){c.textContent='Tersalin ✓';setTimeout(function(){c.textContent='Salin link'},1800)},function(){prompt('Salin link ini:',u)})};
if(navigator.share){n.hidden=false;n.onclick=function(){navigator.share({title:t,url:u}).catch(function(){})}}});</script>"""

def ld(obj): return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'

ORG = {"@type": "Organization", "@id": f"{SITE}/#org", "name": NAME, "url": SITE,
       "logo": {"@type": "ImageObject", "url": f"{SITE}/img/logo-256.png", "width": 256, "height": 256},
       "sameAs": [TIKTOK]}
PERSON = {"@type": "Person", "@id": f"{SITE}/penulis/{AUTHOR['slug']}#person", "name": AUTHOR["nama"],
          "jobTitle": AUTHOR["peran"], "url": f"{SITE}/penulis/{AUTHOR['slug']}", "description": AUTHOR["bio"]}

def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)]}

def card(a, big=False):
    k = KATEGORI[a["kategori"]]
    return f"""<article class="post{' big' if big else ''}"><a href="{url(a)}">
<div class="pimg"><img src="/img/og/{a['slug']}.png" alt="" loading="lazy" width="1200" height="630"></div>
<div class="pbody"><span class="kick">{esc(k['nama'])}</span><h3>{esc(a['judul'])}</h3>
<p>{esc(a['deskripsi'])}</p><span class="meta">{tgl(a['terbit'])} · {a['menit']} menit baca</span></div></a></article>"""

def write(path, s):
    d = os.path.join(OUT, path.strip("/")) if path.strip("/") else OUT
    f = d + ".html" if path.endswith(".html") else os.path.join(d, "index.html")
    if path.endswith(".html"): f = os.path.join(OUT, path.strip("/"))
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(s)

# ---------------------------------------------------------------- halaman
KUIS = {}
EXTRA = []

def page_article(a, arts, ids):
    k = KATEGORI[a["kategori"]]
    body, toc = render_body(a, ids)
    path = url(a)
    toc_h = "".join(f'<li class="l{l}"><a href="#{i}">{esc(t)}</a></li>' for l, t, i in toc)
    faq_h = ""
    if a["faq"]:
        faq_h = '<section class="faq" id="faq"><h2>Pertanyaan yang sering ditanyakan</h2>' + "".join(
            f'<details><summary>{esc(q["q"])}</summary><div>{markdown.markdown(q["a"])}</div></details>' for q in a["faq"]) + "</section>"
    src_h = ""
    if a["sumber"]:
        src_h = '<section class="src" id="sumber"><h2>Sumber</h2><ol>' + "".join(
            f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener nofollow">{esc(s["judul"])}</a>'
            + (f' <span>{esc(s["catatan"])}</span>' if s.get("catatan") else "") + "</li>" for s in a["sumber"]) + "</ol></section>"
    same = [x for x in arts if x["kategori"] == a["kategori"] and x is not a]
    other = [x for x in arts if x["kategori"] != a["kategori"] and x is not a]
    rel = (same + other)[:3]
    i = sorted(arts, key=lambda x: x["id"]); n = [x["id"] for x in i].index(a["id"])
    prv = i[n - 1] if n else None; nxt = i[n + 1] if n + 1 < len(i) else None
    pn = (f'<a class="pn-l" href="{url(prv)}"><small>← Sebelumnya</small><span>{esc(prv["judul"])}</span></a>' if prv else "<span></span>") + \
         (f'<a class="pn-r" href="{url(nxt)}"><small>Berikutnya →</small><span>{esc(nxt["judul"])}</span></a>' if nxt else "")
    img = f"/img/og/{a['slug']}.png"
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "@id": f"{SITE}{path}#artikel", "headline": a["judul"][:110], "description": a["deskripsi"],
         "image": f"{SITE}{img}", "datePublished": a["terbit"], "dateModified": a["diperbarui"], "inLanguage": "id-ID",
         "mainEntityOfPage": f"{SITE}{path}", "author": {"@id": PERSON["@id"]}, "publisher": {"@id": ORG["@id"]},
         "articleSection": k["nama"], "keywords": ", ".join(a["kata_kunci"]), "wordCount": a["kata"],
         "isAccessibleForFree": True},
        crumbs_ld([("Beranda", "/"), (k["nama"], f"/kategori/{a['kategori']}"), (a["judul"], path)]),
        PERSON, ORG]}
    if a["faq"]:
        graph["@graph"].append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", markdown.markdown(q["a"]))}}
            for q in a["faq"]]})
    extra = f'<meta property="article:published_time" content="{a["terbit"]}"><meta property="article:modified_time" content="{a["diperbarui"]}"><meta property="article:section" content="{esc(k["nama"])}">' + ld(graph)
    s = head(a["seo_title"], a["deskripsi"], path, img, "article", extra) + nav() + f"""
<main id="isi" class="post-page"><div class="wrap">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Beranda</a><span>/</span><a href="/kategori/{a['kategori']}">{esc(k['nama'])}</a></nav>
<header class="ph"><span class="eyebrow">{esc(k['nama'])}</span><h1>{esc(a['judul'])}</h1>
<p class="dek">{esc(a['deskripsi'])}</p>
{share(path, a['judul'], 'top')}
<div class="byline"><img src="/img/logo-256.png" alt="" width="40" height="40"><div><a href="/penulis/{AUTHOR['slug']}">{AUTHOR['nama']}</a><span>{AUTHOR['peran']}</span></div>
<div class="bm"><time datetime="{a['terbit']}">{tgl(a['terbit'])}</time>{f' · diperbarui <time datetime="{a["diperbarui"]}">{tgl(a["diperbarui"])}</time>' if a['diperbarui'] != a['terbit'] else ''} · {a['menit']} menit baca</div></div>
</header>
<div class="post-grid">
<aside class="toc-side">{f'<nav class="toc" aria-label="Daftar isi"><b>Daftar isi</b><ol>{toc_h}</ol></nav>' if toc else ''}</aside>
<article class="prose">
{f'<div class="key"><span>Intinya</span><p>{md_inline(a["intinya"])}</p></div>' if a['intinya'] else ''}
{f'<details class="toc-mob"><summary>Daftar isi</summary><ol>{toc_h}</ol></details>' if toc else ''}
{body}
{faq_h}
{src_h}
<a class="watch" href="{TIKTOK}" target="_blank" rel="noopener"><span class="play">▶</span><span><b>Lebih suka versi video 60 detik?</b><small>Tonton di TikTok @ngertilogistik</small></span></a>
{belajar.kuis_cta(a, KUIS)}
{share(path, a['judul'], 'end')}
<div class="author-box"><img src="/img/logo-256.png" alt="" width="64" height="64"><div><small>Ditulis oleh</small><a href="/penulis/{AUTHOR['slug']}"><b>{AUTHOR['nama']}</b></a><p>{esc(AUTHOR['bio'])}</p></div></div>
<div class="pn">{pn}</div>
</article></div></div>
{f'<section class="rel"><div class="wrap"><h2>Baca juga</h2><div class="posts g3">{"".join(card(x) for x in rel)}</div></div></section>' if rel else ''}
</main>""" + CTA + foot().replace("</body>", SHARE_JS + belajar.ARTICLE_JS + "</body>")
    s = s.replace("<body>", f'<body data-aid="{a["id"]}">', 1)
    write(path, s)

def page_home(arts):
    feat, rest = arts[0], arts[1:]
    cats = "".join(f"""<a class="cat" href="/kategori/{k}"><h3>{esc(v['nama'])}</h3><p>{esc(v['desk'])}</p>
<span>{sum(1 for a in arts if a['kategori']==k)} artikel →</span></a>""" for k, v in KATEGORI.items() if any(a['kategori'] == k for a in arts))
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": f"{SITE}/#web", "url": SITE, "name": NAME, "inLanguage": "id-ID", "publisher": {"@id": ORG["@id"]},
         "description": "Blog edukasi logistik: gudang, pengiriman, dan supply chain dengan bahasa sederhana."}, ORG]}
    s = head("Ngerti Logistik: Blog Belajar Logistik, Gudang & Pengiriman",
             "Belajar logistik dari nol: arti istilah gudang, cara kerja pengiriman, stok, dan karier logistik. Dijelaskan sederhana oleh praktisi logistik.",
             "/", extra=ld(graph)) + nav() + f"""
<main id="isi">
<section class="bhero"><div class="wrap">
<span class="eyebrow">Blog edukasi logistik</span>
<h1>Belajar logistik, <em>pelan-pelan sampai ngerti.</em></h1>
<p class="lead">Artikel lengkap tentang gudang, pengiriman, dan supply chain. Ditulis praktisi, pakai bahasa sehari-hari, dan setiap fakta ada sumbernya.</p>
<form class="search" role="search" action="{BASE or '/'}" method="get"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="m20 20-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
<input name="q" type="search" placeholder="Cari artikel: FIFO, SKU, ongkir…" aria-label="Cari artikel"></form>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-h row"><h2>Artikel terbaru</h2><a href="{BASE or '/'}">Lihat semua →</a></div>
<div class="posts lead-grid">{card(feat, True)}{''.join(card(a) for a in rest[:4])}</div></div></section>
<section class="sec alt"><div class="wrap"><div class="sec-h"><h2>Jelajahi per kategori</h2></div><div class="cats">{cats}</div></div></section>
<section class="sec"><div class="wrap"><div class="sec-h"><h2>Mulai dari sini</h2></div>
<div class="posts g3">{''.join(card(a) for a in sorted(arts, key=lambda x: x['id'])[:3])}</div></div></section>
</main>""" + CTA + foot()
    write("/", s)

def page_list(arts):
    data = [dict(u=url(a), t=a["judul"], d=a["deskripsi"], k=a["kategori"], w=" ".join(a["kata_kunci"])) for a in arts]
    chips = '<button class="chip on" data-f="all">Semua</button>' + "".join(
        f'<button class="chip" data-f="{k}">{esc(v["nama"])}</button>' for k, v in KATEGORI.items() if any(a["kategori"] == k for a in arts))
    s = head("Semua Artikel Logistik | Ngerti Logistik", "Daftar lengkap artikel Ngerti Logistik tentang gudang, pengiriman, stok, istilah logistik, dan karier.", BASE or "/",
             extra=ld({"@context": "https://schema.org", "@graph": [crumbs_ld([("Beranda", "/"), ("Artikel", BASE)])]})) + nav() + f"""
<main id="isi" class="sec"><div class="wrap">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Beranda</a><span>/</span><span>Artikel</span></nav>
<div class="sec-h"><h1>Semua artikel</h1><p class="lead">{len(arts)} artikel. Cari topik atau pilih kategori.</p></div>
<div class="tools"><label class="search"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="m20 20-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
<input id="q" type="search" placeholder="Cari: FIFO, SKU, ongkir…" aria-label="Cari artikel"></label><div class="chips">{chips}</div></div>
<p id="count" class="count" aria-live="polite"></p>
<div id="grid" class="posts">{''.join(card(a).replace('<article class="post"', f'<article class="post" data-k="{a["kategori"]}" data-q="{esc((a["judul"]+" "+a["deskripsi"]+" "+" ".join(a["kata_kunci"])).lower())}"') for a in arts)}</div>
<p id="empty" class="empty" hidden>Belum ada artikel yang cocok. Coba kata lain.</p>
</div></main>""" + CTA + foot().replace("</body>", '<script src="/app.js" defer></script></body>')
    write(BASE or "/semua", s)

def page_categories(arts):
    for k, v in KATEGORI.items():
        lst = [a for a in arts if a["kategori"] == k]
        path = f"/kategori/{k}"
        graph = {"@context": "https://schema.org", "@graph": [
            {"@type": "CollectionPage", "name": v["judul"], "description": v["desk"], "url": SITE + path, "inLanguage": "id-ID"},
            crumbs_ld([("Beranda", "/"), (v["nama"], path)])]}
        inner = "".join(card(a) for a in lst) if lst else '<p class="empty">Artikel untuk kategori ini sedang ditulis. Segera terbit.</p>'
        s = head(f"{v['judul']} | {NAME}"[:70], v["desk"], path, extra=ld(graph), noindex=not lst) + nav() + f"""
<main id="isi" class="sec"><div class="wrap">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Beranda</a><span>/</span><span>{esc(v['nama'])}</span></nav>
<div class="sec-h"><span class="eyebrow">Kategori</span><h1>{esc(v['judul'])}</h1><p class="lead">{esc(v['desk'])}</p></div>
<div class="posts">{inner}</div></div></main>""" + CTA + foot()
        write(path, s)

def page_author(arts):
    path = f"/penulis/{AUTHOR['slug']}"
    graph = {"@context": "https://schema.org", "@graph": [{"@type": "ProfilePage", "mainEntity": PERSON, "url": SITE + path}, ORG]}
    s = head(f"{AUTHOR['nama']}, Penulis Ngerti Logistik", AUTHOR["bio"], path, extra=ld(graph)) + nav() + f"""
<main id="isi" class="about"><div class="wrap narrow">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Beranda</a><span>/</span><span>Penulis</span></nav>
<div class="author-hero"><img src="/img/logo-256.png" alt="" width="96" height="96"><div><span class="eyebrow">Penulis</span><h1>{AUTHOR['nama']}</h1><p>{AUTHOR['peran']}</p></div></div>
<p class="lead">{esc(AUTHOR['bio'])}</p>
<h2>Cara menulis di Ngerti Logistik</h2>
<ul class="ticks"><li><b>Satu artikel, satu topik.</b> Dibahas tuntas sampai bisa dipraktikkan.</li>
<li><b>Fakta bersumber.</b> Angka, standar, dan kejadian nyata disertai sumbernya.</li>
<li><b>Contoh ditandai.</b> Ilustrasi angka diberi label CONTOH.</li>
<li><b>Netral.</b> Tidak membahas atau mempromosikan perusahaan tertentu.</li></ul>
<h2>Artikel oleh {AUTHOR['nama']}</h2></div>
<div class="wrap"><div class="posts">{''.join(card(a) for a in arts)}</div></div></main>""" + CTA + foot()
    write(path, s)

def page_about():
    s = head("Tentang Ngerti Logistik", "Ngerti Logistik adalah blog dan akun edukasi yang menjelaskan logistik, gudang, dan pengiriman dengan bahasa sederhana.", "/tentang") + nav() + f"""
<main id="isi" class="about"><div class="wrap narrow">
<span class="eyebrow">Tentang</span><h1>Belajar logistik <em>tanpa ribet.</em></h1>
<p class="lead">Ngerti Logistik adalah blog dan akun edukasi yang menjelaskan logistik dengan bahasa sehari-hari. Di media sosial kami membuat video 60 detik. Di blog ini, setiap topik dibahas lebih lengkap.</p>
<h2>Siapa di baliknya?</h2>
<p>Ngerti Logistik ditulis oleh <a href="/penulis/{AUTHOR['slug']}">{AUTHOR['nama']}</a>, praktisi logistik dengan sekitar sepuluh tahun pengalaman di industri teknologi, FMCG, dan manufaktur.</p>
<h2>Prinsip konten</h2>
<ul class="ticks">
<li><b>Fakta bersumber.</b> Angka dan kejadian nyata disebut sumber dan waktunya.</li>
<li><b>Contoh ditandai.</b> Ilustrasi angka diberi label CONTOH supaya tidak tertukar dengan data nyata.</li>
<li><b>Netral.</b> Tidak membahas atau mempromosikan perusahaan tertentu.</li>
<li><b>Gratis.</b> Murni edukasi, tanpa iklan dan tanpa jualan.</li></ul>
<h2>Untuk siapa?</h2>
<p>Pelajar dan mahasiswa, pekerja baru di gudang atau pengiriman, pelaku UMKM yang mengirim barang setiap hari, dan siapa saja yang ingin tahu bagaimana barang bisa sampai ke tangan kita.</p>
<p><a class="btn" href="{BASE or '/'}">Baca artikel</a></p></div></main>""" + CTA + foot()
    write("/tentang", s)

# Produk digital: isi link Lynk.id dan harga di sini, lalu jalankan build.py
# Satu entri per landing page. Ganti "lynk" dengan link checkout Lynk.id produk masing-masing.
TOKO = "https://lynk.id/ngertilogistik"
PRODUK = {
    "/toolkit-gudang-pro": {"lynk": "https://lynk.id/ngertilogistik/jjm4m9w15zgj/checkout", "harga": "Rp47.000"},
    "/toolkit-ekspedisi": {"lynk": TOKO, "harga": "Rp79.000"},
    "/stok-cuan-seller": {"lynk": TOKO, "harga": "Rp39.000"},
    "/lolos-kerja-logistik": {"lynk": TOKO, "harga": "Rp39.000"},
    "/kamus-logistik": {"lynk": TOKO, "harga": "Rp29.000"},
    "/cheat-sheet-logistik": {"lynk": TOKO, "harga": "Rp19.000"},
    "/mega-bundle-logistik": {"lynk": TOKO, "harga": "Rp149.000"},
}

HALAMAN = [  # halaman statis dari content/halaman/<file>.html
    ("/produk", "produk.html", "Produk Digital Logistik: Template Excel, E-book & Toolkit | Ngerti Logistik",
     "Template Excel, e-book, SOP, kamus, dan cheat sheet logistik berbahasa Indonesia untuk gudang, ekspedisi, online seller, dan persiapan kerja."),
    ("/toolkit-ekspedisi", "toolkit-ekspedisi.html", "Toolkit Ekspedisi & Forwarder: Quotation, Tracker & Invoice Excel | Ngerti Logistik",
     "Template Excel untuk ekspedisi dan forwarder: kalkulator quotation (CBM, volumetrik, asuransi, PPN), shipment tracker, invoice otomatis, dashboard, LCL vs FCL."),
    ("/stok-cuan-seller", "stok-cuan-seller.html", "Stok & Cuan: Template Excel Stok & Laba Online Seller | Ngerti Logistik",
     "Template Excel untuk online seller: laba bersih per channel setelah potongan marketplace, stok multi-gudang, produk laris & lambat, kalkulator harga jual dan ongkir."),
    ("/lolos-kerja-logistik", "lolos-kerja-logistik.html", "Paket Lolos Kerja Logistik: CV ATS, 50 Pertanyaan Interview & Tes Excel | Ngerti Logistik",
     "Template CV ATS 5 posisi logistik, e-book 50 pertanyaan interview dengan contoh jawaban, dan latihan tes Excel 8 soal + kunci jawaban."),
    ("/kamus-logistik", "kamus-logistik.html", "Kamus Logistik Inggris–Indonesia: 250 Istilah | Ngerti Logistik",
     "250 istilah logistik dan supply chain dalam 8 bidang, dijelaskan singkat dalam Bahasa Indonesia, lengkap dengan indeks A–Z."),
    ("/cheat-sheet-logistik", "cheat-sheet-logistik.html", "Cheat Sheet Logistik: 10 Lembar Siap Print | Ngerti Logistik",
     "10 lembar ringkasan logistik: Incoterms 2020, kontainer, simbol kemasan, dokumen ekspor-impor, jalur impor, rumus, barang berbahaya, armada, satuan, KPI."),
    ("/mega-bundle-logistik", "mega-bundle-logistik.html", "Mega Bundle Ngerti Logistik: 6 Produk Digital | Ngerti Logistik",
     "Semua produk digital Ngerti Logistik dalam satu paket: Toolkit Gudang Pro, Toolkit Ekspedisi, Stok & Cuan, Paket Lolos Kerja, Kamus, dan Cheat Sheet."),
    ("/toolkit-gudang-pro", "toolkit-gudang-pro.html", "Toolkit Gudang Pro: Template Excel, E-book & SOP Gudang | Ngerti Logistik",
     "Template Excel 9-in-1 untuk stok, kartu stok, opname, ABC, ROP, dan kubikasi, plus e-book panduan admin gudang serta 8 SOP dan 8 form siap print."),
    ("/template", "template.html", "Template Spreadsheet Logistik Gratis (Excel) | Ngerti Logistik",
     "Download gratis 18 template Excel logistik: kartu stok, reorder point, analisis ABC, cycle count, picking list, tracker pengiriman, dan lainnya."),
    ("/kalkulator-kubikasi", "kalkulator-kubikasi.html", "Kalkulator Kubikasi & Cargo Planner Kontainer | Ngerti Logistik",
     "Hitung CBM, berat volume, dan perkiraan jumlah karton yang muat di kontainer 20 ft, 40 ft, 40 ft high cube, atau truk Anda. Gratis, langsung di browser."),
]

# Landing page jualan: tanpa menu, link keluar, tombol bagikan, dan CTA TikTok supaya pembaca fokus ke penawaran
LANDING = {p for p in PRODUK}

def nav_landing():
    return """<header class="nav"><div class="wrap nav-in">
<span class="brand"><img src="/img/logo-256.png" alt="" width="34" height="34"><span>Ngerti <b>Logistik</b></span></span>
<a class="btn-sm" href="#beli">Lihat penawaran</a></div></header>"""

def foot_landing():
    return f"""<footer class="foot"><div class="wrap fine" style="text-align:center">© {datetime.date.today().year} {NAME}. Data di dalam file produk adalah CONTOH, bukan data nyata. File untuk dipakai pribadi atau di tempat kerja pembeli, tidak untuk dijual ulang.</div></footer>
</body></html>"""

def page_halaman():
    for path, f, title, desc in HALAMAN:
        body = open(os.path.join(ROOT, "content/halaman", f), encoding="utf-8").read()
        pr = PRODUK.get(path, {"lynk": TOKO, "harga": ""})
        body = body.replace("{{LYNK}}", esc(pr["lynk"])).replace("{{HARGA}}", esc(pr["harga"]))
        body = re.sub(r"\{\{HARGA:(/[a-z0-9-]+)\}\}", lambda m: esc(PRODUK.get(m.group(1), {}).get("harga", "")), body)
        if path in LANDING:
            s = head(title, desc, path) + nav_landing() + body.replace("<!--SHARE-->", "") + foot_landing()
        else:
            body = body.replace("<!--SHARE-->", share(path, title.split(" | ")[0], "top"))
            s = head(title, desc, path) + nav() + body + CTA + foot().replace("</body>", SHARE_JS + "</body>")
        write(path, s)

def page_404():
    s = head("Halaman tidak ditemukan | Ngerti Logistik", "Halaman tidak ditemukan.", "/404", noindex=True) + nav() + f"""
<main id="isi" class="about"><div class="wrap narrow" style="text-align:center">
<span class="eyebrow">404</span><h1>Paket ini <em>salah alamat.</em></h1><p class="lead">Halaman yang dicari tidak ada. Mungkin sudah pindah rak.</p>
<p><a class="btn" href="{BASE or '/'}">Lihat semua artikel</a></p></div></main>""" + foot()
    write("/404.html", s)

def feeds(arts):
    today = datetime.date.today().isoformat()
    urls = [("/", today), (BASE, today), ("/tentang", today), (f"/penulis/{AUTHOR['slug']}", today)]
    urls += [(p, today) for p, *_ in HALAMAN]
    urls += [(p, today) for p in EXTRA]
    urls += [(f"/kategori/{k}", today) for k in KATEGORI if any(a["kategori"] == k for a in arts)]
    urls += [(url(a), a["diperbarui"]) for a in arts]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"<url><loc>{SITE}{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in urls if u) + "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    def rfc(d): return datetime.datetime.strptime(d, "%Y-%m-%d").strftime("%a, %d %b %Y 07:00:00 +0700")
    items = "".join(f"""<item><title>{esc(a['judul'])}</title><link>{SITE}{url(a)}</link><guid>{SITE}{url(a)}</guid>
<pubDate>{rfc(a['terbit'])}</pubDate><category>{esc(KATEGORI[a['kategori']]['nama'])}</category><description>{esc(a['deskripsi'])}</description></item>""" for a in arts[:30])
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>{NAME}</title><link>{SITE}</link>
<atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml"/>
<description>Blog edukasi logistik berbahasa Indonesia.</description><language>id</language>{items}</channel></rss>"""
    open(os.path.join(OUT, "feed.xml"), "w").write(rss)

def og_images(arts):
    """Gambar 1200x630 per artikel (sampul + og:image). Dibuat sekali, lewati yang sudah ada."""
    need = [a for a in arts if not os.path.exists(os.path.join(OUT, "img/og", a["slug"] + ".png"))]
    if not need: return
    os.makedirs(os.path.join(OUT, "img/og"), exist_ok=True)
    job = [dict(slug=a["slug"], judul=a["judul"], kat=KATEGORI[a["kategori"]]["nama"], id=a["id"]) for a in need]
    json.dump(job, open(os.path.join(ROOT, "tools/og_job.json"), "w"), ensure_ascii=False)
    subprocess.run(["node", os.path.join(ROOT, "tools/og.js")], check=True, cwd=ROOT,
                   env={**os.environ, "NODE_PATH": subprocess.check_output(["npm", "root", "-g"]).decode().strip()})

def redirects(arts):
    """Alihkan URL lama /materi/lxx-* ke artikel baru (308), sisanya ke daftar artikel."""
    v = json.load(open(os.path.join(ROOT, "vercel.json")))
    old = json.load(open(os.path.join(ROOT, "data/topics.json"), encoding="utf-8"))
    by = {a["id"]: a for a in arts}
    r = []
    for t in old:
        s = re.sub(r"[^a-z0-9]+", "-", t["topic"].lower()).strip("-")[:60].strip("-")
        src = f"/materi/{t['id'].lower()}-{s}"
        r.append({"source": src, "destination": url(by[t["id"]]) if t["id"] in by else (BASE or "/"), "permanent": t["id"] in by})
    r.append({"source": "/materi", "destination": BASE or "/", "permanent": False})
    v["redirects"] = r
    json.dump(v, open(os.path.join(ROOT, "vercel.json"), "w"), indent=1)

if __name__ == "__main__":
    load_cfg()
    arts, ids = load_articles()
    if not arts: raise SystemExit("Belum ada artikel di content/artikel/")
    keep = {f for f in os.listdir(OUT) if re.fullmatch(r"[0-9a-f]{32}\.txt", f)} | {"files", "img", "fonts", "style.css", "app.js", "favicon.svg", "apple-touch-icon.png"}
    for f in os.listdir(OUT):
        if f not in keep:
            p = os.path.join(OUT, f); shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    og_images(arts)
    KUIS = belajar.load(sys.modules[__name__], "kuis.json", {})
    for a in arts: page_article(a, arts, ids)
    page_home(arts); page_list(arts); page_categories(arts); page_author(arts); page_about(); page_halaman(); page_404()
    EXTRA = belajar.build(sys.modules[__name__], arts)
    feeds(arts); redirects(arts)
    print(f"OK {len(arts)} artikel terbit · base={BASE or '/'}")
