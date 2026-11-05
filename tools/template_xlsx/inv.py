from lib import *

ITEMS = [("SKU-001","Air mineral 600 ml (karton)","ktn",48000),("SKU-002","Mi instan rasa ayam (dus)","dus",105000),("SKU-003","Minyak goreng 1 L","btl",17500),
 ("SKU-004","Gula pasir 1 kg","pak",16000),("SKU-005","Kopi sachet (renceng)","rcg",14000),("SKU-006","Sabun mandi batang","pcs",4500),
 ("SKU-007","Deterjen bubuk 800 g","pak",22000),("SKU-008","Tisu wajah 250 lembar","pak",12500),("SKU-009","Beras 5 kg","krg",72000),
 ("SKU-010","Kecap manis 520 ml","btl",21000),("SKU-011","Teh celup isi 25","kts",7500),("SKU-012","Susu UHT 1 L","ktk",19000)]

def kartu_stok():
    wb = wb_new()
    m = sheet(wb, "Master SKU", "Kartu Stok · Master SKU", tab=ACC)
    t = sheet(wb, "Transaksi", "Kartu Stok · Transaksi Masuk & Keluar")
    d = sheet(wb, "Dashboard", "Dashboard Inventory")
    wb.move_sheet("Dashboard", -2)
    rows = []
    for i, (s, n, u, h) in enumerate(ITEMS):
        rows.append([s, n, u, h, random.randint(90, 200), random.choice([30, 40, 50, 60]),
          "=SUMIFS(Transaksi!$D:$D,Transaksi!$B:$B,A{r},Transaksi!$C:$C,\"Masuk\")",
          "=SUMIFS(Transaksi!$D:$D,Transaksi!$B:$B,A{r},Transaksi!$C:$C,\"Keluar\")",
          "=IF(A{r}=\"\",\"\",E{r}+G{r}-H{r})", "=IF(A{r}=\"\",\"\",I{r}*D{r})",
          "=IF(A{r}=\"\",\"\",IF(I{r}<=F{r},\"Perlu order\",\"Aman\"))"])
    a, b = table(m, 5, 1, ["SKU","Nama barang","Satuan","Harga satuan","Stok awal","Titik pesan ulang (ROP)","Total masuk","Total keluar","Saldo","Nilai stok","Status"],
          rows, [None,None,None,RP,N0,N0,N0,N0,N0,RP,None], inputs={0,1,2,3,4,5}, blank=28)
    widths(m, [11,30,8,14,10,14,11,11,10,15,13])
    status_color(m, f"K{a}:K{b}", "Perlu", "FFD9D5"); status_color(m, f"K{a}:K{b}", "Aman", "D3F2E4")
    m.freeze_panes = "C6"
    tr = []
    for k in range(60):
        s = random.choice(ITEMS)[0]; j = "Masuk" if random.random() < .35 else "Keluar"
        tr.append([day(k // 2), s, j, random.randint(20, 80) if j == "Masuk" else random.randint(3, 15),
                   "=IFERROR(INDEX('Master SKU'!$B:$B,MATCH(B{r},'Master SKU'!$A:$A,0)),\"\")", "PO pemasok" if j == "Masuk" else "Order pelanggan"])
    a2, b2 = table(t, 5, 1, ["Tanggal","SKU","Jenis","Qty","Nama barang (otomatis)","Keterangan"], tr, [D,None,None,N0,None,None], inputs={0,1,2,3,5}, blank=200)
    dv_list(t, f"C{a2}:C{b2}", ["Masuk", "Keluar"])
    widths(t, [12,11,10,8,30,22]); t.freeze_panes = "A6"
    R = f"'Master SKU'!"
    kpi(d, 5, 1, "TOTAL SKU", f"=COUNTA({R}A6:A{b})", N0)
    kpi(d, 5, 3, "PERLU ORDER", f"=COUNTIF({R}K6:K{b},\"Perlu order\")", N0)
    kpi(d, 5, 5, "NILAI STOK", f"=SUM({R}J6:J{b})", RP, w=3)
    kpi(d, 5, 8, "TRANSAKSI", f"=COUNTA(Transaksi!B6:B{b2})", N0)
    widths(d, [12] * 10)
    bar(d, "A9", "Saldo vs titik pesan ulang per SKU", Reference(m, min_col=1, min_row=6, max_row=5 + len(ITEMS)),
        [Reference(m, min_col=9, min_row=5, max_row=5 + len(ITEMS)), Reference(m, min_col=6, min_row=5, max_row=5 + len(ITEMS))], w=24, h=9)
    return wb

def rop():
    wb = wb_new()
    i = sheet(wb, "Input", "Reorder Point & Safety Stock · Input", tab=ACC)
    h = sheet(wb, "Hasil per SKU", "Hasil Reorder Point per SKU")
    p = sheet(wb, "Panduan", "Panduan Rumus", note="Sheet ini berisi penjelasan rumus yang dipakai template.")
    rows = []
    for s, n, u, _ in ITEMS[:10]:
        avg = random.randint(5, 30); mx = round(avg * random.uniform(1.3, 1.8)); lt = random.randint(3, 10); ltm = lt + random.randint(1, 5)
        rows.append([s, n, avg, mx, lt, ltm, random.randint(40, 400)])
    a, b = table(i, 5, 1, ["SKU","Nama barang","Pemakaian rata-rata / hari","Pemakaian maksimum / hari","Lead time rata-rata (hari)","Lead time maksimum (hari)","Stok saat ini"],
          rows, [None,None,N0,N0,N0,N0,N0], inputs=set(range(7)), blank=40)
    widths(i, [11,30,14,14,14,14,12]); i.freeze_panes = "C6"
    hr = [[f"=IF(Input!A{r}=\"\",\"\",Input!A{r})", f"=IF(Input!A{r}=\"\",\"\",Input!B{r})",
           f"=IF(Input!A{r}=\"\",\"\",MAX(0,Input!D{r}*Input!F{r}-Input!C{r}*Input!E{r}))",
           f"=IF(Input!A{r}=\"\",\"\",Input!C{r}*Input!E{r}+C{{r}})".replace("{{r}}", "{r}"),
           f"=IF(Input!A{r}=\"\",\"\",Input!G{r})",
           "=IF(A{r}=\"\",\"\",IF(E{r}<=D{r},\"Pesan sekarang\",\"Aman\"))",
           "=IF(A{r}=\"\",\"\",IF(Input!C{r}=0,\"-\",(E{r}-D{r})/Input!C{r}))"] for r in range(a, b + 1)]
    hr = [[c.replace("{r}", "{r}") for c in row] for row in hr]
    header(h, 5, 1, ["SKU","Nama barang","Safety stock","Reorder point (ROP)","Stok saat ini","Status","Sisa hari sebelum ROP"])
    for k, row in enumerate(hr):
        rr = a + k
        for j, v in enumerate(row): put(h, rr, 1 + j, v.replace("{r}", str(rr)), [None,None,N0,N0,N0,None,N1][j])
    status_color(h, f"F{a}:F{b}", "Pesan", "FFD9D5"); status_color(h, f"F{a}:F{b}", "Aman", "D3F2E4")
    widths(h, [11,30,13,16,12,16,16]); h.freeze_panes = "C6"
    bar(h, "I5", "Stok saat ini vs ROP", Reference(h, min_col=1, min_row=6, max_row=15),
        [Reference(h, min_col=5, min_row=5, max_row=15), Reference(h, min_col=4, min_row=5, max_row=15)], w=18, h=9)
    widths(p, [100])
    txt = ["Safety stock (stok pengaman) = (pemakaian maksimum per hari × lead time maksimum) − (pemakaian rata-rata per hari × lead time rata-rata).",
           "Ini salah satu metode sederhana yang umum dipakai. Ada metode lain yang memakai standar deviasi; pilih yang sesuai kebijakan perusahaan Anda.",
           "Reorder point (ROP) = pemakaian rata-rata per hari × lead time rata-rata + safety stock.",
           "Status 'Pesan sekarang' muncul bila stok saat ini sudah sama atau di bawah ROP.",
           "Sisa hari sebelum ROP = (stok saat ini − ROP) ÷ pemakaian rata-rata per hari. Angka negatif berarti stok sudah melewati ROP.",
           "Penjelasan lengkap: ngertilogistik.web.id/blog/reorder-point dan ngertilogistik.web.id/blog/safety-stock"]
    for k, s in enumerate(txt): note(p, 5 + k * 2, 1, s, 11); p.row_dimensions[5 + k * 2].height = 30
    return wb

def abc():
    wb = wb_new()
    d = sheet(wb, "Data barang", "Analisis ABC · Data Barang", tab=ACC)
    h = sheet(wb, "Hasil ABC", "Hasil Analisis ABC")
    g = sheet(wb, "Grafik Pareto", "Grafik Pareto")
    names = [x[1] for x in ITEMS] + ["Saus sambal 340 ml","Margarin 200 g","Tepung terigu 1 kg","Sarden kaleng 425 g","Biskuit kaleng","Pasta gigi 190 g","Sampo sachet (renceng)","Popok bayi isi 20"]
    rows = []
    for k, n in enumerate(names):
        rows.append([f"SKU-{k+1:03d}", n, random.choice([120, 300, 600, 900, 1500, 2400, 4000, 6000]), random.choice([4500, 12000, 17500, 22000, 48000, 72000, 105000]),
                     "=IF(A{r}=\"\",\"\",C{r}*D{r})", "=IF(A{r}=\"\",\"\",E{r}+ROW()/1000000)"])
    a, b = table(d, 5, 1, ["SKU","Nama barang","Pemakaian per tahun (qty)","Harga satuan","Nilai pemakaian","Kunci urut (bantu)"], rows,
                 [None,None,N0,RP,RP,'0.000000'], inputs={0,1,2,3}, blank=30)
    widths(d, [11,30,16,14,17,14]); d.freeze_panes = "C6"
    h["A5"] = "Batas kelas A (kumulatif)"; h["A6"] = "Batas kelas B (kumulatif)"
    for r, v in ((5, .8), (6, .95)): put(h, r, 3, v, P1, inp=True)
    note(h, 7, 1, "Batas 80% dan 95% adalah nilai awal yang sering dipakai sebagai contoh. Ubah sesuai kebijakan Anda.", 9, color=MUTE)
    for r in (5, 6): h.cell(r, 1).font = Font(name=F, bold=True)
    n = b - a + 1
    header(h, 9, 1, ["Peringkat","SKU","Nama barang","Nilai pemakaian","% dari total","% kumulatif","Kelas"])
    DR = f"'Data barang'!"
    for k in range(n):
        r = 10 + k
        put(h, r, 1, k + 1, N0)
        put(h, r, 2, f"=IF(A{r}>COUNT({DR}$F${a}:$F${b}),\"\",INDEX({DR}$A${a}:$A${b},MATCH(LARGE({DR}$F${a}:$F${b},A{r}),{DR}$F${a}:$F${b},0)))")
        put(h, r, 3, f"=IF(B{r}=\"\",\"\",INDEX({DR}$B${a}:$B${b},MATCH(B{r},{DR}$A${a}:$A${b},0)))")
        put(h, r, 4, f"=IF(B{r}=\"\",\"\",INDEX({DR}$E${a}:$E${b},MATCH(B{r},{DR}$A${a}:$A${b},0)))", RP)
        put(h, r, 5, f"=IF(B{r}=\"\",\"\",D{r}/SUM({DR}$E${a}:$E${b}))", P1)
        put(h, r, 6, f"=IF(B{r}=\"\",\"\",SUM($E$10:E{r}))", P1)
        put(h, r, 7, f"=IF(B{r}=\"\",\"\",IF(F{r}-E{r}<$C$5,\"A\",IF(F{r}-E{r}<$C$6,\"B\",\"C\")))", align="center")
    last = 9 + n
    for cl, col in (("A", "FFE58A"), ("B", "DCE6F5"), ("C", "EEF1F5")):
        h.conditional_formatting.add(f"G10:G{last}", CellIsRule(operator="equal", formula=[f'"{cl}"'], fill=PatternFill("solid", fgColor=col)))
    widths(h, [10,11,30,17,12,13,8]); h.freeze_panes = "A10"
    h["I9"] = "Rekap kelas"; h["I9"].font = Font(name=F, bold=True, color=NAVY2)
    header(h, 10, 9, ["Kelas","Jumlah SKU","% SKU","Nilai","% nilai"])
    for k, cl in enumerate("ABC"):
        r = 11 + k
        put(h, r, 9, cl, align="center"); put(h, r, 10, f"=COUNTIF($G$10:$G${last},I{r})", N0)
        put(h, r, 11, f"=IFERROR(J{r}/SUM($J$11:$J$13),0)", P1); put(h, r, 12, f"=SUMIF($G$10:$G${last},I{r},$D$10:$D${last})", RP)
        put(h, r, 13, f"=IFERROR(L{r}/SUM($L$11:$L$13),0)", P1)
    widths(h, [10,11,30,17,12,13,8,3,8,11,9,16,9])
    nn = len(rows)
    b1 = BarChart(); b1.title = "Pareto nilai pemakaian"; b1.height = 10; b1.width = 26
    b1.add_data(Reference(h, min_col=4, min_row=9, max_row=9 + nn), titles_from_data=True)
    b1.set_categories(Reference(h, min_col=2, min_row=10, max_row=9 + nn))
    b1.series[0].graphicalProperties.solidFill = NAVY2; b1.y_axis.title = "Nilai"
    l1 = LineChart(); l1.add_data(Reference(h, min_col=6, min_row=9, max_row=9 + nn), titles_from_data=True)
    l1.y_axis.axId = 200; l1.y_axis.title = "% kumulatif"; l1.y_axis.crosses = "max"; l1.y_axis.number_format = '0%'
    l1.series[0].graphicalProperties.line.solidFill = ACC; l1.series[0].graphicalProperties.line.width = 28000
    b1 += l1; b1.legend.position = "b"; g.add_chart(b1, "A5")
    pie(g, "A27", "Jumlah SKU per kelas", Reference(h, min_col=9, min_row=11, max_row=13), Reference(h, min_col=10, min_row=10, max_row=13))
    pie(g, "H27", "Nilai per kelas", Reference(h, min_col=9, min_row=11, max_row=13), Reference(h, min_col=12, min_row=10, max_row=13))
    return wb

def aging():
    wb = wb_new()
    d = sheet(wb, "Data stok", "Aging Stok · Data Stok", tab=ACC)
    r_ = sheet(wb, "Rekap umur", "Rekap Umur Stok")
    db = sheet(wb, "Dashboard", "Dashboard Aging & Dead Stock")
    d["A5"] = "Tanggal laporan"; d["A5"].font = Font(name=F, bold=True); put(d, 5, 3, dt.date(2026, 11, 1), D, inp=True)
    rows = []
    for s, n, u, h in ITEMS:
        rows.append([s, n, random.randint(5, 200), h, BASE - dt.timedelta(days=random.choice([3, 10, 25, 40, 70, 95, 130, 200, 260, 400])),
                     "=IF(A{r}=\"\",\"\",$C$5-E{r})",
                     "=IF(A{r}=\"\",\"\",IF(F{r}<=90,\"0-90 hari\",IF(F{r}<=180,\"91-180 hari\",IF(F{r}<=365,\"181-365 hari\",\"Lebih dari 365 hari\"))))",
                     "=IF(A{r}=\"\",\"\",C{r}*D{r})"])
    a, b = table(d, 7, 1, ["SKU","Nama barang","Qty","Harga satuan","Tanggal terakhir bergerak","Umur (hari)","Kelompok umur","Nilai stok"], rows,
                 [None,None,N0,RP,D,N0,None,RP], inputs={0,1,2,3,4}, blank=40)
    widths(d, [11,30,9,14,14,11,14,15]); d.freeze_panes = "C8"
    status_color(d, f"G{a}:G{b}", "Lebih dari", "FFD9D5"); status_color(d, f"G{a}:G{b}", "181-365", "FFE9C7")
    header(r_, 5, 1, ["Kelompok umur","Jumlah SKU","Qty","Nilai stok","% nilai"])
    for k, g in enumerate(["0-90 hari","91-180 hari","181-365 hari","Lebih dari 365 hari"]):
        r = 6 + k; DS = "'Data stok'!"
        put(r_, r, 1, g); put(r_, r, 2, f"=COUNTIF({DS}$G${a}:$G${b},A{r})", N0)
        put(r_, r, 3, f"=SUMIF({DS}$G${a}:$G${b},A{r},{DS}$C${a}:$C${b})", N0)
        put(r_, r, 4, f"=SUMIF({DS}$G${a}:$G${b},A{r},{DS}$H${a}:$H${b})", RP)
        put(r_, r, 5, f"=IFERROR(D{r}/SUM($D$6:$D$9),0)", P1)
    put(r_, 10, 1, "Total", bold=True); put(r_, 10, 2, "=SUM(B6:B9)", N0, bold=True); put(r_, 10, 3, "=SUM(C6:C9)", N0, bold=True); put(r_, 10, 4, "=SUM(D6:D9)", RP, bold=True)
    note(r_, 12, 1, "Batas kelompok umur (90, 180, 365 hari) adalah contoh. Ubah rumus di kolom G sheet Data stok bila kebijakan Anda berbeda.", 9, color=MUTE)
    widths(r_, [16,12,10,16,10])
    kpi(db, 5, 1, "NILAI STOK TOTAL", "='Rekap umur'!D10", RP, w=3)
    kpi(db, 5, 4, "NILAI > 180 HARI", "='Rekap umur'!D8+'Rekap umur'!D9", RP, w=3)
    kpi(db, 5, 7, "% NILAI > 180 HARI", "=IFERROR(D6/A6,0)", P1)
    widths(db, [12] * 9)
    pie(db, "A9", "Nilai stok per kelompok umur", Reference(r_, min_col=1, min_row=6, max_row=9), Reference(r_, min_col=4, min_row=5, max_row=9), w=12)
    bar(db, "G9", "Jumlah SKU per kelompok umur", Reference(r_, min_col=1, min_row=6, max_row=9), [Reference(r_, min_col=2, min_row=5, max_row=9)], w=13)
    return wb

def turnover():
    wb = wb_new()
    m = sheet(wb, "Data bulanan", "Inventory Turnover · Data Bulanan", tab=ACC)
    s = sheet(wb, "Hasil per SKU", "Turnover & Days on Hand per SKU")
    t = sheet(wb, "Tren", "Tren Turnover")
    bl = ["Jan","Feb","Mar","Apr","Mei","Jun","Jul","Agu","Sep","Okt","Nov","Des"]; hari = [31,28,31,30,31,30,31,31,30,31,30,31]
    rows = []; inv = 420_000_000
    for k in range(12):
        end = int(inv * random.uniform(.9, 1.1) / 1e6) * 1e6
        rows.append([f"{bl[k]} 2026", hari[k], int(random.uniform(180, 260)) * 1e6, inv, end,
                     "=IF(A{r}=\"\",\"\",(D{r}+E{r})/2)", "=IF(A{r}=\"\",\"\",IFERROR(C{r}/F{r},0))", "=IF(A{r}=\"\",\"\",IFERROR(B{r}/G{r},0))"])
        inv = end
    a, b = table(m, 5, 1, ["Bulan","Jumlah hari","HPP / nilai barang keluar","Persediaan awal","Persediaan akhir","Rata-rata persediaan","Turnover (x)","Days on hand (hari)"], rows,
                 [None,N0,RP,RP,RP,RP,N2,N1], inputs={0,1,2,3,4})
    note(m, b + 2, 1, "Turnover = HPP ÷ rata-rata persediaan. Days on hand = jumlah hari periode ÷ turnover. Pakai satuan nilai yang sama untuk HPP dan persediaan.", 9, color=MUTE)
    widths(m, [12,10,20,18,18,18,12,14])
    s["A5"] = "Jumlah hari periode"; s["A6"] = "Batas turnover 'lambat' (x)"
    put(s, 5, 3, 90, N0, inp=True); put(s, 6, 3, 1.5, N1, inp=True)
    for r in (5, 6): s.cell(r, 1).font = Font(name=F, bold=True)
    rows = []
    for sk, n, u, h in ITEMS:
        rows.append([sk, n, random.randint(1, 30) * 1e6, random.randint(2, 15) * 1e6,
                     "=IF(A{r}=\"\",\"\",IFERROR(C{r}/D{r},0))", "=IF(A{r}=\"\",\"\",IFERROR($C$5/E{r},0))", "=IF(A{r}=\"\",\"\",IF(E{r}<$C$6,\"Lambat\",\"Normal\"))"])
    a2, b2 = table(s, 8, 1, ["SKU","Nama barang","Nilai barang keluar (periode)","Rata-rata persediaan","Turnover (x)","Days on hand (hari)","Status"], rows,
                   [None,None,RP,RP,N2,N0,None], inputs={0,1,2,3}, blank=30)
    status_color(s, f"G{a2}:G{b2}", "Lambat", "FFD9D5")
    widths(s, [11,30,20,18,12,14,10]); s.freeze_panes = "C9"
    line(t, "A5", "Turnover per bulan", Reference(m, min_col=1, min_row=6, max_row=17), [Reference(m, min_col=7, min_row=5, max_row=17)], w=20)
    bar(t, "A21", "Days on hand per bulan", Reference(m, min_col=1, min_row=6, max_row=17), [Reference(m, min_col=8, min_row=5, max_row=17)], w=20)
    return wb

def opname():
    wb = wb_new()
    l = sheet(wb, "Lembar hitung", "Stock Opname · Lembar Hitung", tab=ACC)
    r_ = sheet(wb, "Rekap selisih", "Rekap Selisih Stock Opname")
    ba = sheet(wb, "Berita acara", "Berita Acara Stock Opname", note="Isi sel kuning, lalu cetak sheet ini untuk ditandatangani.")
    rows = []
    for k, (sk, n, u, h) in enumerate(ITEMS):
        q = random.randint(10, 120); h1 = q + random.choice([0] * 12 + [-1, -2, 1])
        h2 = None if h1 == q else h1
        rows.append([f"A-{(k // 4) + 1:02d}-{(k % 4) + 1:02d}", sk, n, u, q, h1, h2,
                     "=IF(B{r}=\"\",\"\",IF(G{r}<>\"\",G{r},F{r}))", "=IF(B{r}=\"\",\"\",H{r}-E{r})", h,
                     "=IF(B{r}=\"\",\"\",I{r}*J{r})", ""])
    a, b = table(l, 5, 1, ["Lokasi","SKU","Nama barang","Satuan","Qty sistem","Hitung 1","Hitung 2 (bila beda)","Qty final","Selisih","Harga satuan","Nilai selisih","Keterangan"], rows,
                 [None,None,None,None,N0,N0,N0,N0,'#,##0;[Red]-#,##0;"-"',RP,'"Rp"#,##0;[Red]-"Rp"#,##0;"-"',None], inputs={0,1,2,3,4,5,6,9,11}, blank=60)
    widths(l, [10,10,28,8,10,9,12,9,8,13,14,20]); l.freeze_panes = "D6"
    LH = "'Lembar hitung'!"
    items = [("Jumlah baris dihitung", f"=COUNTA({LH}B{a}:B{b})", N0), ("Baris dengan selisih", f"=SUMPRODUCT(({LH}I{a}:I{b}<>\"\")*({LH}I{a}:I{b}<>0))", N0),
             ("Baris sesuai", "=C5-C6", N0), ("Akurasi (baris sesuai ÷ total)", "=IFERROR(C7/C5,0)", P1),
             ("Total selisih qty (lebih)", f"=SUMIF({LH}I{a}:I{b},\">0\")", N0), ("Total selisih qty (kurang)", f"=SUMIF({LH}I{a}:I{b},\"<0\")", N0),
             ("Nilai selisih bersih", f"=SUM({LH}K{a}:K{b})", '"Rp"#,##0;[Red]-"Rp"#,##0;"-"')]
    for k, (lab, f, fm) in enumerate(items):
        r = 5 + k; note(r_, r, 1, lab, bold=True); put(r_, r, 3, f, fm)
    header(r_, 14, 1, ["Hasil", "Jumlah baris"]); put(r_, 15, 1, "Sesuai"); put(r_, 15, 2, "=C7", N0); put(r_, 16, 1, "Selisih"); put(r_, 16, 2, "=C6", N0)
    widths(r_, [30, 12, 16])
    pie(r_, "E5", "Hasil hitung", Reference(r_, min_col=1, min_row=15, max_row=16), Reference(r_, min_col=2, min_row=14, max_row=16))
    widths(ba, [26, 40, 4, 26, 30])
    f = [("Nomor", "BA-SO/2026/001"), ("Tanggal pelaksanaan", dt.date(2026, 11, 1)), ("Lokasi / gudang", "Gudang utama"), ("Penanggung jawab", "(nama)")]
    for k, (lab, v) in enumerate(f):
        note(ba, 5 + k, 1, lab, bold=True); put(ba, 5 + k, 2, v, D if isinstance(v, dt.date) else None, inp=True)
    note(ba, 10, 1, "Pada tanggal di atas telah dilakukan perhitungan fisik persediaan dengan hasil sebagai berikut:", 10)
    ba.merge_cells("A10:E10")
    for k, (lab, ref, fm) in enumerate([("Jumlah baris dihitung", "='Rekap selisih'!C5", N0), ("Baris dengan selisih", "='Rekap selisih'!C6", N0),
                                        ("Akurasi", "='Rekap selisih'!C8", P1), ("Nilai selisih bersih", "='Rekap selisih'!C11", '"Rp"#,##0;[Red]-"Rp"#,##0;"-"')]):
        note(ba, 12 + k, 1, lab, bold=True); put(ba, 12 + k, 2, ref, fm)
    note(ba, 17, 1, "Rincian selisih terlampir pada sheet Lembar hitung.", 10)
    for c, who in ((1, "Petugas hitung"), (4, "Mengetahui")):
        note(ba, 20, c, who, bold=True); note(ba, 25, c, "(.................................)")
    return wb
