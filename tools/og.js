// Membuat gambar 1200x630 per artikel dari tools/og_job.json -> public/img/og/<slug>.png
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const ROOT = path.resolve(__dirname, '..');
const job = JSON.parse(fs.readFileSync(path.join(__dirname, 'og_job.json'), 'utf8'));
const logo = 'data:image/png;base64,' + fs.readFileSync(path.join(ROOT, 'public/img/logo-256.png')).toString('base64');
const F = (n, w, f) => `@font-face{font-family:'${n}';font-weight:${w};src:url(data:font/woff2;base64,${fs.readFileSync(path.join(ROOT,'public/fonts',f+'.woff2')).toString('base64')})}`;
const FONTS = F('Plus Jakarta Sans',500,'jakarta-500')+F('Plus Jakarta Sans',800,'jakarta-800')+F('JetBrains Mono',700,'mono-700');
const esc = s => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const tpl = j => `<!doctype html><html><head><meta charset="utf-8">
<style>${FONTS}</style>
<style>*{margin:0;box-sizing:border-box}body{width:1200px;height:630px;overflow:hidden;font-family:'Plus Jakarta Sans',sans-serif;color:#EEF2F8;
background:radial-gradient(700px 500px at 88% 10%,#1E3157,transparent 60%),#0B1220;position:relative}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:48px 48px}
.k{position:absolute;left:72px;top:72px;font:700 22px 'JetBrains Mono';letter-spacing:.14em;text-transform:uppercase;color:#0B1220;background:#FFC400;padding:10px 18px;border-radius:10px}
h1{position:absolute;left:72px;right:300px;top:150px;font-weight:800;line-height:1.08;letter-spacing:-.02em}
.route{position:absolute;left:72px;right:72px;bottom:150px;height:5px;background:repeating-linear-gradient(90deg,#FFC400 0 10px,transparent 10px 34px);opacity:.5}
.box{position:absolute;right:80px;top:120px;width:190px;height:190px}
.f{position:absolute;left:72px;bottom:60px;display:flex;align-items:center;gap:16px;font-size:28px}
.f img{width:56px;height:56px;border-radius:14px}.f b{color:#FFC400}.u{position:absolute;right:72px;bottom:72px;font:700 22px 'JetBrains Mono';color:#9AA8C0}
</style></head><body><div class="grid"></div><span class="k">${esc(j.kat)}</span>
<svg class="box" viewBox="0 0 200 200"><polygon points="100,10 190,55 100,100 10,55" fill="#FFC400"/><polygon points="10,55 100,100 100,190 10,145" fill="#E5E7EB"/><polygon points="190,55 100,100 100,190 190,145" fill="#9CA3AF"/></svg>
<h1 id="t">${esc(j.judul)}</h1><div class="route"></div>
<div class="f"><img src="${logo}"><span>Ngerti <b>Logistik</b></span></div><span class="u">ngertilogistik.web.id</span></body></html>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  for (const j of job) {
    await p.setContent(tpl(j), { waitUntil: 'networkidle' });
    await p.evaluate(() => { const t = document.getElementById('t'); let s = 76; t.style.fontSize = s + 'px';
      while (t.scrollHeight > 300 && s > 40) { s -= 4; t.style.fontSize = s + 'px'; } });
    await p.screenshot({ path: path.join(ROOT, 'public/img/og', j.slug + '.png') });
  }
  await b.close();
  console.log('og', job.length);
})();
