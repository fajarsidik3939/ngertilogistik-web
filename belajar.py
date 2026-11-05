"""Halaman belajar & alat Ngerti Logistik (dipanggil dari build.py).

/belajar              jalur belajar + progres (localStorage)
/kuis                 kuis per artikel (data/kuis.json)
/glosarium            kamus istilah A-Z (data/glosarium.json)
/kalkulator-logistik  6 kalkulator (ROP & safety stock, EOQ, palet, berat volume, biaya simpan, turnover)
/karier               pojok karier (data/karier.json)
/cheat-sheet          cheat sheet 1 halaman + PDF (data/cheatsheet.json -> public/files/cheatsheet/*.pdf)
Hanya artikel yang sudah tayang yang ditautkan.
"""
import os, json, html, hashlib

def esc(s): return html.escape(str(s), quote=True)
def jdump(o): return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")

def load(B, name, default):
    p = os.path.join(B.ROOT, "data", name)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else default

def page(B, path, title, desc, eyebrow, h1, lead, body, script="", crumb=None, extra_ld=None):
    ldg = {"@context": "https://schema.org", "@graph": [B.crumbs_ld([("Beranda", "/"), (crumb or h1.split("<")[0], path)])] + (extra_ld or [])}
    s = B.head(title, desc, path, extra=B.ld(ldg)) + B.nav() + f"""
<main id="isi" class="bl"><section class="bl-hero"><div class="wrap">
<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>
{B.share(path, title.split(' | ')[0], 'top')}</div></section>
{body}</main>""" + B.CTA + B.foot().replace("</body>", B.SHARE_JS + script + "</body>")
    B.write(path, s)

# ------------------------------------------------------------ jalur belajar
LEVELS = [("Pemula", "Kenalan dengan logistik, gudang, dan istilah dasar.", 1, 40),
          ("Menengah", "Mengelola stok, proses gudang, dan pengiriman sehari-hari.", 41, 80),
          ("Lanjutan", "Perencanaan, biaya, KPI, dan cara berpikir supply chain.", 81, 120)]

def page_belajar(B, arts, kuis):
    topics = json.load(open(os.path.join(B.ROOT, "data/topics.json"), encoding="utf-8"))
    by = {a["id"]: a for a in arts}
    secs = ""
    for i, (nm, ds, lo, hi) in enumerate(LEVELS):
        rows = ""
        lst = [t for t in topics if lo <= t["n"] <= hi]
        live = [t for t in lst if t["id"] in by]
        for t in lst:
            a = by.get(t["id"])
            if a:
                k = B.KATEGORI[a["kategori"]]["nama"]
                q = f'<a class="bl-q" href="/kuis?a={a["id"]}">Kuis</a>' if a["id"] in kuis else ""
                rows += f"""<li class="bl-step" data-id="{a['id']}"><label class="bl-chk"><input type="checkbox" aria-label="Tandai sudah dibaca: {esc(a['judul'])}"><span></span></label>
<a class="bl-t" href="{B.url(a)}"><small>{t['n']:02d} · {esc(k)} · {a['menit']} menit</small><b>{esc(a['judul'])}</b></a>{q}</li>"""
            else:
                rows += f"""<li class="bl-step off"><span class="bl-chk dis"><span></span></span><span class="bl-t"><small>{t['n']:02d} · segera tayang</small><b>{esc(t['topic'])}</b></span></li>"""
        secs += f"""<section class="bl-lv" data-lv="{i}"><div class="bl-lvh"><div><span class="bl-badge">Level {i + 1}</span><h2>{nm}</h2><p>{ds}</p></div>
<div class="bl-prog"><b><span class="done">0</span> / {len(live)}</b><small>artikel tayang sudah dibaca · {len(lst)} topik total</small><i><u></u></i></div></div>
<ol class="bl-list">{rows}</ol></section>"""
    body = f"""<div class="wrap"><div class="bl-total pan-b"><div><b id="tot">0%</b><small>progres belajar Anda</small></div>
<p>Centang artikel yang sudah dibaca, atau baca sampai akhir dan centangnya terisi otomatis. Progres tersimpan di browser Anda, tanpa akun.</p>
<button class="bl-reset" type="button">Reset progres</button></div>
{secs}</div>"""
    js = """<script>(function(){var K='nl_read',r=[];try{r=JSON.parse(localStorage.getItem(K)||'[]')}catch(e){}
function save(){try{localStorage.setItem(K,JSON.stringify(r))}catch(e){}}
function upd(){var all=0,dn=0;document.querySelectorAll('.bl-lv').forEach(function(s){var st=s.querySelectorAll('.bl-step[data-id]'),d=0;st.forEach(function(x){var on=r.indexOf(x.dataset.id)>-1;x.classList.toggle('ok',on);x.querySelector('input').checked=on;if(on)d++});
s.querySelector('.done').textContent=d;s.querySelector('.bl-prog u').style.width=(st.length?d/st.length*100:0)+'%';all+=st.length;dn+=d});document.getElementById('tot').textContent=(all?Math.round(dn/all*100):0)+'%'}
document.querySelectorAll('.bl-step[data-id] input').forEach(function(c){c.onchange=function(){var id=c.closest('.bl-step').dataset.id,i=r.indexOf(id);if(c.checked&&i<0)r.push(id);if(!c.checked&&i>-1)r.splice(i,1);save();upd()}});
document.querySelector('.bl-reset').onclick=function(){if(confirm('Hapus semua progres belajar?')){r=[];save();upd()}};upd()})();</script>"""
    page(B, "/belajar", "Jalur Belajar Logistik dari Nol | Ngerti Logistik",
         "Belajar logistik dari nol secara berurutan: level pemula, menengah, dan lanjutan. Centang artikel yang sudah dibaca dan pantau progres Anda.",
         "Jalur belajar", "Belajar logistik <em>dari nol, berurutan.</em>",
         f"{len(topics)} topik disusun dari dasar sampai lanjutan. Artikel baru tayang setiap hari, dan progres belajar Anda tersimpan otomatis.", body, js, "Jalur belajar")

ARTICLE_JS = """<script>(function(){var id=document.body.dataset.aid;if(!id)return;var K='nl_read',done=false;
function mark(){if(done)return;var h=document.documentElement;if((h.scrollTop+innerHeight)/h.scrollHeight>.75){done=true;try{var r=JSON.parse(localStorage.getItem(K)||'[]');if(r.indexOf(id)<0){r.push(id);localStorage.setItem(K,JSON.stringify(r))}}catch(e){}}}
addEventListener('scroll',mark,{passive:true})})();</script>"""

def kuis_cta(a, kuis):
    if a["id"] not in kuis: return ""
    return f"""<a class="kz-cta" href="/kuis?a={a['id']}"><span class="kz-ic">?</span><span><b>Uji pemahaman Anda</b><small>{len(kuis[a['id']]['soal'])} soal singkat tentang artikel ini, langsung dengan pembahasan.</small></span><span class="kz-go">Mulai kuis →</span></a>"""

# ------------------------------------------------------------ kuis
def page_kuis(B, arts, kuis):
    live = [a for a in sorted(arts, key=lambda x: x["id"]) if a["id"] in kuis]
    data = {a["id"]: {"j": a["judul"], "u": B.url(a), "s": kuis[a["id"]]["soal"]} for a in live}
    cards = "".join(f"""<button class="kz-card" data-id="{a['id']}"><small>{esc(B.KATEGORI[a['kategori']]['nama'])}</small><b>{esc(a['judul'])}</b>
<span><em class="kz-sc" data-id="{a['id']}">Belum dicoba</em> · {len(kuis[a['id']]['soal'])} soal</span></button>""" for a in live)
    body = f"""<div class="wrap"><div class="kz-wrap"><section id="kzList"><div class="kz-sum pan-b"><div><b id="kzDone">0</b><small>kuis selesai dari {len(live)}</small></div><div><b id="kzAvg">-</b><small>rata-rata skor</small></div>
<button class="btn" id="kzRand" type="button">Kuis acak 10 soal</button></div><div class="kz-grid">{cards}</div></section>
<section id="kzPlay" class="pan-b" hidden></section></div></div>"""
    js = "<script>var KZ=" + jdump(data) + """;(function(){var K='nl_kuis',sc={};try{sc=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}
var L=document.getElementById('kzList'),P=document.getElementById('kzPlay');
function sum(){var ks=Object.keys(sc).filter(function(k){return KZ[k]}),t=0;ks.forEach(function(k){t+=sc[k]});document.getElementById('kzDone').textContent=ks.length;document.getElementById('kzAvg').textContent=ks.length?Math.round(t/ks.length)+'%':'-';
document.querySelectorAll('.kz-sc').forEach(function(e){var v=sc[e.dataset.id];e.textContent=v==null?'Belum dicoba':'Skor terbaik '+v+'%';e.classList.toggle('ok',v>=80)})}
function shuffle(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
function play(id,qs,title,link){var i=0,ok=0;L.hidden=true;P.hidden=false;scrollTo({top:P.offsetTop-90});
function q(){var s=qs[i];var h='<div class="kz-top"><button class="kz-back" type="button">← Semua kuis</button><span>Soal '+(i+1)+' / '+qs.length+'</span></div><i class="kz-bar"><u style="width:'+(i/qs.length*100)+'%"></u></i><small class="kz-from">'+title+'</small><h2>'+s.q+'</h2><div class="kz-opts">';
s.opsi.forEach(function(o,k){h+='<button class="kz-o" data-k="'+k+'">'+String.fromCharCode(65+k)+'. '+o+'</button>'});P.innerHTML=h+'</div><div class="kz-ex" hidden></div>';
P.querySelector('.kz-back').onclick=back;P.querySelectorAll('.kz-o').forEach(function(b){b.onclick=function(){var k=+b.dataset.k,r=k===s.jawab;if(r)ok++;
P.querySelectorAll('.kz-o').forEach(function(x){x.disabled=true;if(+x.dataset.k===s.jawab)x.classList.add('right')});if(!r)b.classList.add('wrong');
var ex=P.querySelector('.kz-ex');ex.hidden=false;ex.innerHTML='<b>'+(r?'Benar!':'Kurang tepat.')+'</b> '+s.bahas+(s.u?' <a href="'+s.u+'">Baca artikelnya</a>':'')+'<button class="btn" type="button">'+(i+1<qs.length?'Soal berikutnya →':'Lihat hasil')+'</button>';
ex.querySelector('button').onclick=function(){i++;i<qs.length?q():end()}}})}
function end(){var p=Math.round(ok/qs.length*100);if(id){sc[id]=Math.max(sc[id]||0,p);try{localStorage.setItem(K,JSON.stringify(sc))}catch(e){}}sum();
P.innerHTML='<div class="kz-res"><b>'+p+'%</b><h2>'+ok+' dari '+qs.length+' jawaban benar</h2><p>'+(p>=80?'Mantap, Anda sudah paham topik ini.':p>=50?'Lumayan. Baca ulang bagian yang masih ragu, lalu coba lagi.':'Tidak apa-apa. Baca artikelnya dulu, lalu ulangi kuisnya.')+'</p><div class="kz-act">'+(link?'<a class="btn" href="'+link+'">Baca artikel</a>':'')+'<button class="btn ghost" type="button" id="kzAgain">Ulangi</button><button class="btn ghost" type="button" id="kzAll">Kuis lain</button></div></div>';
document.getElementById('kzAgain').onclick=function(){play(id,shuffle(qs.slice()),title,link)};document.getElementById('kzAll').onclick=back}
q()}
function back(){P.hidden=true;L.hidden=false;history.replaceState(null,'','/kuis')}
function start(id){var d=KZ[id];if(!d)return;history.replaceState(null,'','/kuis?a='+id);play(id,d.s.slice(),d.j,d.u)}
document.querySelectorAll('.kz-card').forEach(function(c){c.onclick=function(){start(c.dataset.id)}});
document.getElementById('kzRand').onclick=function(){var all=[];Object.keys(KZ).forEach(function(k){KZ[k].s.forEach(function(s){var x=Object.assign({},s);x.u=KZ[k].u;all.push(x)})});play(null,shuffle(all).slice(0,10),'Kuis acak dari semua artikel',null)};
sum();var a=new URLSearchParams(location.search).get('a');if(a)start(a)})();</script>"""
    page(B, "/kuis", "Kuis Logistik: Uji Pemahaman Gudang & Pengiriman | Ngerti Logistik",
         "Kuis pilihan ganda tentang logistik, gudang, stok, dan pengiriman. Setiap soal langsung dengan pembahasan. Gratis, tanpa daftar.",
         "Kuis", "Uji pemahaman Anda, <em>langsung dengan pembahasan.</em>",
         f"{sum(len(kuis[a['id']]['soal']) for a in live)} soal dari {len(live)} artikel. Skor terbaik tersimpan di browser Anda.", body, js, "Kuis")

# ------------------------------------------------------------ glosarium
def page_glosarium(B, arts, glos):
    by = {a["id"]: a for a in arts}
    letters = sorted({(g["istilah"][0].upper() if g["istilah"][0].isalpha() else "#") for g in glos})
    groups = {}
    for g in glos:
        L = g["istilah"][0].upper() if g["istilah"][0].isalpha() else "#"; groups.setdefault(L, []).append(g)
    body = '<div class="wrap"><div class="gl-tools"><input id="glq" class="tp-search" type="search" placeholder="Cari istilah, misal: FEFO, resi, putaway" aria-label="Cari istilah"><nav class="gl-az">' + \
           "".join(f'<a href="#h-{"num" if L == "#" else L}">{L}</a>' for L in letters) + '</nav></div><p id="glc" class="tp-count"></p>'
    defs = []
    for L in letters:
        body += f'<section class="gl-sec"><h2 id="h-{"num" if L == "#" else L}">{L}</h2><dl class="gl-grid">'
        for g in groups[L]:
            a = by.get(g.get("artikel"))
            al = f'<span class="gl-al">{esc(", ".join(g["alias"]))}</span>' if g.get("alias") else ""
            lk = f'<a class="gl-lk" href="{B.url(a)}">Baca: {esc(a["judul"])} →</a>' if a else ""
            body += f'<div class="gl-it" data-q="{esc((g["istilah"] + " " + " ".join(g.get("alias", [])) + " " + g["arti"]).lower())}"><dt>{esc(g["istilah"])}{al}</dt><dd>{esc(g["arti"])}{lk}</dd></div>'
            defs.append({"@type": "DefinedTerm", "name": g["istilah"], "description": g["arti"]})
        body += "</dl></section>"
    body += '<p id="gle" class="empty" hidden>Istilah tidak ditemukan. Coba kata lain.</p></div>'
    js = """<script>(function(){var q=document.getElementById('glq'),it=[].slice.call(document.querySelectorAll('.gl-it')),c=document.getElementById('glc'),e=document.getElementById('gle');
function run(){var t=q.value.trim().toLowerCase(),n=0;it.forEach(function(x){var ok=!t||x.dataset.q.indexOf(t)>-1;x.hidden=!ok;n+=ok});document.querySelectorAll('.gl-sec').forEach(function(s){s.hidden=!s.querySelector('.gl-it:not([hidden])')});c.textContent=n+' istilah';e.hidden=n>0}
q.oninput=run;run()})();</script>"""
    page(B, "/glosarium", "Glosarium Logistik: Kamus Istilah Gudang & Pengiriman | Ngerti Logistik",
         f"Kamus {len(glos)} istilah logistik dari A sampai Z: gudang, stok, dokumen, dan pengiriman. Dijelaskan singkat dengan bahasa sederhana.",
         "Glosarium", "Kamus istilah logistik <em>A sampai Z.</em>",
         f"{len(glos)} istilah gudang, stok, dokumen, dan pengiriman dijelaskan singkat. Setiap istilah terhubung ke artikel lengkapnya.", body, js, "Glosarium",
         [{"@type": "DefinedTermSet", "name": "Glosarium Logistik Ngerti Logistik", "hasDefinedTerm": defs}])

# ------------------------------------------------------------ karier
def page_karier(B, arts, kr):
    by = {a["id"]: a for a in arts}
    jal = "".join(f'<div class="kr-tahap"><span class="bl-badge">Tahap {i + 1}</span><h3>{esc(j["tahap"])}</h3><ul>' + "".join(f"<li><a href=\"#r-{esc(p.lower().replace(' ', '-'))}\">{esc(p)}</a></li>" for p in j["peran"]) + "</ul></div>"
                  for i, j in enumerate(kr["jalur"]))
    areas = sorted({p["area"] for p in kr["peran"]})
    chips = '<button class="on" data-f="semua">Semua</button>' + "".join(f'<button data-f="{esc(a)}">{esc(a)}</button>' for a in areas)
    roles = ""
    for p in kr["peran"]:
        rel = [by[x] for x in p.get("artikel", []) if x in by]
        rl = ("<div class='kr-rel'><small>Pelajari:</small>" + "".join(f'<a href="{B.url(a)}">{esc(a["judul"])}</a>' for a in rel) + "</div>") if rel else ""
        roles += f"""<article class="kr-role" id="r-{esc(p['nama'].lower().replace(' ', '-'))}" data-k="{esc(p['area'])}"><span class="tp-tag">{esc(p['area'])}</span><h3>{esc(p['nama'])}</h3><p>{esc(p['ringkas'])}</p>
<div class="kr-cols"><div><b>Tugas utama</b><ul>{''.join(f'<li>{esc(t)}</li>' for t in p['tugas'])}</ul></div><div><b>Skill</b><ul class="kr-sk">{''.join(f'<li>{esc(t)}</li>' for t in p['skill'])}</ul></div></div>{rl}</article>"""
    ww = "".join(f'<details class="kr-q"><summary><span>{esc(w["untuk"])}</span>{esc(w["q"])}</summary><p>{esc(w["tips"])}</p></details>' for w in kr["wawancara"])
    sk = "".join(f'<div class="step"><b>{i + 1}</b><h3>{esc(s["nama"])}</h3><p>{esc(s["kenapa"])}</p></div>' for i, s in enumerate(kr["skill_umum"]))
    body = f"""<div class="wrap"><h2 class="bl-h2">Jalur <em>karier</em></h2><div class="kr-jalur">{jal}</div>
<h2 class="bl-h2">Kenali <em>perannya</em></h2><div class="tp-filter kr-f">{chips}</div><div class="kr-grid">{roles}</div>
<h2 class="bl-h2">Persiapan <em>wawancara</em></h2><p class="bl-p">Pertanyaan yang sering muncul saat melamar posisi logistik, beserta tips menjawabnya.</p><div class="kr-qs">{ww}</div>
<h2 class="bl-h2">Skill yang <em>selalu terpakai</em></h2><div class="steps kr-steps">{sk}</div>
<p class="bl-p" style="margin-top:28px">Mau latihan dulu? Coba <a href="/kuis">kuis logistik</a>, pelajari <a href="/glosarium">istilahnya</a>, atau pakai <a href="/template">template spreadsheet</a> untuk latihan Excel.</p></div>"""
    js = """<script>(function(){var b=[].slice.call(document.querySelectorAll('.kr-f button'));b.forEach(function(x){x.onclick=function(){b.forEach(function(y){y.classList.toggle('on',y===x)});var f=x.dataset.f;document.querySelectorAll('.kr-role').forEach(function(r){r.hidden=!(f==='semua'||r.dataset.k===f)})}})})();</script>"""
    page(B, "/karier", "Karier Logistik: Peran, Skill, dan Tips Wawancara | Ngerti Logistik",
         "Kenali peran kerja di gudang, pengiriman, dan supply chain: tugas, skill yang dibutuhkan, jalur karier, dan tips menjawab pertanyaan wawancara.",
         "Pojok karier", "Mau kerja di logistik? <em>Mulai dari sini.</em>",
         f"Kenali {len(kr['peran'])} peran di gudang, inventory, pengiriman, dan supply chain, jalur kariernya, dan cara menyiapkan wawancara.", body, js, "Karier")

# ------------------------------------------------------------ cheat sheet
def sheet_html(cs, by, B, print_mode=False):
    out = ""
    for b in cs["blok"]:
        j, isi = b["jenis"], b["isi"]
        if j == "rumus": x = f'<div class="cs-f">{esc(isi)}</div>'
        elif j == "contoh": x = f'<div class="cs-ex">{esc(isi)}</div>'
        elif j == "daftar": x = "<ul>" + "".join(f"<li>{esc(i)}</li>" for i in isi) + "</ul>"
        elif j == "langkah": x = "<ol>" + "".join(f"<li>{esc(i)}</li>" for i in isi) + "</ol>"
        elif j == "tabel": x = "<table><thead><tr>" + "".join(f"<th>{esc(c)}</th>" for c in isi["kolom"]) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in isi["baris"]) + "</tbody></table>"
        else: x = f"<p>{esc(isi)}</p>"
        cat = f'<p class="cs-n">{esc(b["catatan"])}</p>' if b.get("catatan") else ""
        out += f'<section class="cs-b cs-{j}"><h3>{esc(b["judul"])}</h3>{x}{cat}</section>'
    return out

PRINT_CSS = """@page{size:A4;margin:11mm 11mm 10mm}
@font-face{font-family:J;src:url(FONTS/jakarta-400.woff2)}@font-face{font-family:J;font-weight:700;src:url(FONTS/jakarta-700.woff2)}@font-face{font-family:J;font-weight:800;src:url(FONTS/jakarta-800.woff2)}@font-face{font-family:M;src:url(FONTS/mono-500.woff2)}
*{box-sizing:border-box}body{margin:0;font:400 9.6pt/1.42 J,Arial,sans-serif;color:#0B1220}
.h{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px solid #FFC400;padding-bottom:6px;margin-bottom:8px}
.h h1{margin:0;font:800 19pt/1.1 J}.h p{margin:3px 0 0;color:#4A5873}.h small{font:9pt M;color:#4A5873;text-align:right}
.g{columns:2;column-gap:7mm}.cs-b{break-inside:avoid;margin:0 0 6px;padding:7px 9px;border:1px solid #D5DCE6;border-radius:7px}
.cs-b h3{margin:0 0 4px;font:800 10.5pt J;color:#1F3A6B}.cs-f{font:700 9.6pt/1.4 J;background:#FFF6CC;border-left:3px solid #FFC400;padding:5px 7px;border-radius:4px}
.cs-ex{background:#F3F6FB;padding:5px 7px;border-radius:4px;font-size:9pt}.cs-n{margin:4px 0 0;color:#4A5873;font-size:8.6pt}
ul,ol{margin:0;padding-left:15px}li{margin:1px 0}table{width:100%;border-collapse:collapse;font-size:8.4pt}th{background:#14203A;color:#fff;text-align:left;padding:3px 4px}td{border-bottom:1px solid #E3E8F0;padding:3px 4px;vertical-align:top}
.f{margin-top:6px;border-top:1px solid #D5DCE6;padding-top:5px;font:8pt M;color:#4A5873;display:flex;justify-content:space-between}"""

def page_cheatsheet(B, arts, cs):
    by = {a["id"]: a for a in arts}
    outdir = os.path.join(B.OUT, "files", "cheatsheet"); os.makedirs(outdir, exist_ok=True)
    import base64
    def fdata(n): return "data:font/woff2;base64," + base64.b64encode(open(os.path.join(B.OUT, "fonts", n), "rb").read()).decode()
    css = PRINT_CSS
    for n in ("jakarta-400.woff2", "jakarta-700.woff2", "jakarta-800.woff2", "mono-500.woff2"): css = css.replace(f"FONTS/{n}", fdata(n))
    jobs = []
    cards = ""
    for c in cs:
        inner = sheet_html(c, by, B)
        rel = [by[x] for x in c["artikel"] if x in by]
        doc = f"""<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="h"><div><h1>{esc(c['judul'])}</h1><p>{esc(c['sub'])}</p></div><small>Ngerti Logistik<br>ngertilogistik.web.id</small></div>
<div class="g">{inner}</div><div class="f"><span>Gratis untuk dibagikan dan dicetak. Angka berlabel CONTOH adalah ilustrasi.</span><span>Selengkapnya: ngertilogistik.web.id/cheat-sheet</span></div></body></html>"""
        h = hashlib.md5(doc.encode()).hexdigest()[:10]
        pdf = os.path.join(outdir, f"{c['slug']}.pdf"); stamp = pdf + ".hash"
        if not (os.path.exists(pdf) and os.path.exists(stamp) and open(stamp).read() == h): jobs.append((doc, pdf, stamp, h))
        rl = "".join(f'<a href="{B.url(a)}">{esc(a["judul"])}</a>' for a in rel)
        cards += f"""<article class="cs-card" id="{c['slug']}"><div class="cs-prev"><div class="cs-page"><b>{esc(c['judul'])}</b><span></span><span></span><span class="s"></span><span></span><span class="s"></span></div></div>
<div class="tp-body"><span class="tp-tag">PDF · 1 halaman A4</span><h3>{esc(c['judul'])}</h3><p>{esc(c['sub'])}</p>
<div class="kr-rel"><small>Dari artikel:</small>{rl}</div>
<div class="tp-foot"><button class="btn ghost cs-view" type="button" data-s="{c['slug']}">Lihat</button><a class="btn" href="/files/cheatsheet/{c['slug']}.pdf" download>Download PDF</a></div></div>
<template id="t-{c['slug']}"><div class="cs-modal-in"><div class="cs-mh"><b>{esc(c['judul'])}</b><button type="button" class="cs-x" aria-label="Tutup">×</button></div><div class="cs-sheet">{inner}</div></div></template></article>"""
    if jobs:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                br = p.chromium.launch(); pg = br.new_page()
                for doc, pdf, stamp, h in jobs:
                    pg.set_content(doc, wait_until="load"); pg.wait_for_timeout(300)
                    pg.pdf(path=pdf, format="A4", print_background=True, prefer_css_page_size=True)
                    open(stamp, "w").write(h)
                br.close()
        except Exception as e:
            print("PERINGATAN: PDF cheat sheet gagal dibuat:", e)
    body = f"""<div class="wrap"><div class="cs-grid">{cards}</div></div><div class="cs-modal" id="csm" hidden></div>"""
    js = """<script>(function(){var m=document.getElementById('csm');function close(){m.hidden=true;m.innerHTML='';document.body.style.overflow=''}
document.querySelectorAll('.cs-view').forEach(function(b){b.onclick=function(){m.innerHTML='';m.appendChild(document.getElementById('t-'+b.dataset.s).content.cloneNode(true));m.hidden=false;document.body.style.overflow='hidden';m.querySelector('.cs-x').onclick=close}});
m.onclick=function(e){if(e.target===m)close()};addEventListener('keydown',function(e){if(e.key==='Escape'&&!m.hidden)close()})})();</script>"""
    page(B, "/cheat-sheet", "Cheat Sheet Logistik PDF Gratis (Rumus & Istilah) | Ngerti Logistik",
         "Download gratis cheat sheet logistik 1 halaman: rumus stok, istilah gudang, alur gudang, berat volume, FIFO FEFO, dan dasar supply chain.",
         "Cheat sheet", "Rangkuman 1 halaman, <em>siap dicetak.</em>",
         f"{len(cs)} cheat sheet PDF berisi rumus, istilah, dan langkah penting dari artikel Ngerti Logistik. Tempel di meja kerja atau bagikan ke tim.", body, js, "Cheat sheet")

# ------------------------------------------------------------ kalkulator logistik
def page_kalkulator(B):
    body = open(os.path.join(B.ROOT, "content/halaman/kalkulator-logistik.html"), encoding="utf-8").read()
    page(B, "/kalkulator-logistik", "Kalkulator Logistik: ROP, Safety Stock, EOQ, Palet | Ngerti Logistik",
         "Kalkulator logistik gratis: reorder point dan safety stock, EOQ, kebutuhan palet, berat volume, biaya simpan, dan inventory turnover. Langsung di browser.",
         "Alat gratis", "Kalkulator logistik, <em>sekali klik.</em>",
         "Enam kalkulator untuk urusan stok, gudang, dan pengiriman. Semua rumus dijelaskan, dan hasilnya langsung muncul saat Anda mengetik.", body, "", "Kalkulator logistik")

def build(B, arts):
    kuis = load(B, "kuis.json", {}); glos = load(B, "glosarium.json", []); kr = load(B, "karier.json", None); cs = load(B, "cheatsheet.json", [])
    page_belajar(B, arts, kuis); page_kuis(B, arts, kuis)
    if glos: page_glosarium(B, arts, glos)
    if kr: page_karier(B, arts, kr)
    if cs: page_cheatsheet(B, arts, cs)
    page_kalkulator(B)
    return ["/belajar", "/kuis", "/glosarium", "/karier", "/cheat-sheet", "/kalkulator-logistik"]
