"""Render ilustrasi artikel ke WebP, gaya sama dengan gambar sampul dan video.

Sumber: tools/ilustrasi/<slug>/<nama>.html (isi <body> saja; boleh pakai kelas di BASE_CSS).
Hasil:  public/img/ilustrasi/<slug>/<nama>.webp (lebar 960 px tampil, dirender 2x).

Pakai:  python3 tools/ilustrasi.py            # render yang belum ada
        python3 tools/ilustrasi.py --semua    # render ulang semua
        python3 tools/ilustrasi.py <slug>     # render ulang satu artikel
Di artikel: ![alt deskriptif](/img/ilustrasi/<slug>/<nama>.webp){width="960" height="<tinggi>" loading="lazy"}
Tinggi tiap gambar dicetak saat render.
"""
import base64, glob, io, os, sys
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "tools/ilustrasi")
OUT = os.path.join(ROOT, "public/img/ilustrasi")


def font(name, weight, f):
    b = base64.b64encode(open(os.path.join(ROOT, "public/fonts", f + ".woff2"), "rb").read()).decode()
    return f"@font-face{{font-family:'{name}';font-weight:{weight};src:url(data:font/woff2;base64,{b})}}"


FONTS = (font("Plus Jakarta Sans", 500, "jakarta-500") + font("Plus Jakarta Sans", 700, "jakarta-700")
         + font("Plus Jakarta Sans", 800, "jakarta-800") + font("JetBrains Mono", 700, "mono-700"))

BASE_CSS = """
*{margin:0;box-sizing:border-box}
body{width:960px;font-family:'Plus Jakarta Sans',sans-serif;color:#EEF2F8;background:transparent}
.cv{position:relative;padding:44px 44px 36px;border-radius:28px;overflow:hidden;
 background:radial-gradient(700px 500px at 90% 0%,#1E3157,transparent 60%),#0B1220}
.cv::before{content:"";position:absolute;inset:0;pointer-events:none;
 background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:48px 48px}
.cv>*{position:relative}
.k{display:inline-block;font:700 18px 'JetBrains Mono';letter-spacing:.14em;text-transform:uppercase;color:#0B1220;background:#FFC400;padding:8px 14px;border-radius:9px}
h1{font-weight:800;font-size:44px;line-height:1.1;letter-spacing:-.02em;margin:18px 0 6px}
h1 em{font-style:normal;color:#FFC400}
.sub{font:500 21px/1.4 'Plus Jakarta Sans';color:#9AA8C0}
.card{background:#14203A;border:1px solid #22304B;border-radius:18px;padding:22px}
.n{font:700 16px 'JetBrains Mono';color:#FFC400;letter-spacing:.1em}
.t{font-weight:800;font-size:24px;line-height:1.2;margin:8px 0 6px}
.d{font:500 19px/1.4 'Plus Jakarta Sans';color:#B9C4D6}
.foot{display:flex;justify-content:space-between;align-items:center;margin-top:30px;font:700 16px 'JetBrains Mono';color:#9AA8C0}
.foot b{color:#EEF2F8;font-family:'Plus Jakarta Sans';font-size:18px}.foot b i{font-style:normal;color:#FFC400}
.route{height:4px;margin-top:26px;background:repeating-linear-gradient(90deg,#FFC400 0 10px,transparent 10px 30px);opacity:.45}
.ok{color:#7EE2A8}.bad{color:#FF8A7A}
"""

FOOT = '<div class="route"></div><div class="foot"><b>Ngerti <i>Logistik</i></b><span>ngertilogistik.web.id</span></div>'


def page(body):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}</style><style>{BASE_CSS}</style>"
            f"</head><body><div class='cv'>{body.replace('{{FOOT}}', FOOT)}</div></body></html>")


def main(args):
    semua = "--semua" in args
    hanya = [a for a in args if not a.startswith("--")]
    files = sorted(glob.glob(os.path.join(SRC, "*", "*.html")))
    if hanya:
        files = [f for f in files if os.path.basename(os.path.dirname(f)) in hanya]
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 960, "height": 800}, device_scale_factor=2)
        for f in files:
            slug, nama = os.path.basename(os.path.dirname(f)), os.path.splitext(os.path.basename(f))[0]
            out = os.path.join(OUT, slug, nama + ".webp")
            if os.path.exists(out) and not (semua or hanya):
                continue
            os.makedirs(os.path.dirname(out), exist_ok=True)
            pg.set_content(page(open(f, encoding="utf-8").read()), wait_until="networkidle")
            png = pg.locator(".cv").screenshot(omit_background=True)
            im = Image.open(io.BytesIO(png))
            im.save(out, "WEBP", quality=82, method=6)
            print(f"{slug}/{nama}.webp  width=\"960\" height=\"{round(im.height / 2)}\"  {os.path.getsize(out)//1024} KB")
        b.close()


if __name__ == "__main__":
    main(sys.argv[1:])
