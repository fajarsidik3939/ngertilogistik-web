from lib import *
from inv import ITEMS

def cycle_count():
    wb = wb_new()
    j = sheet(wb, "Jadwal", "Cycle Count · Jadwal Hitung", tab=ACC)
    h = sheet(wb, "Hasil hitung", "Cycle Count · Hasil Hitung")
    d = sheet(wb, "Dashboard", "Dashboard Cycle Count")
    zones = ["A", "B", "C", "D"]; rows = []
    for k in range(32):
        z = zones[k // 8]; kl = random.choice("AABBC")
        rows.append([f"{z}-{(k % 8) // 4 + 1:02d}-{k % 4 + 1:02d}", z, kl, day(k // 4 * 3 + (0 if kl == "A" else 1)), random.choice(["Rina", "Budi", "Sari", "Dodi"])])
    a, b = table(j, 5, 1, ["Lokasi","Zona","Kelas ABC","Tanggal jadwal","Petugas"], rows, [None,None,None,D,None], inputs=set(range(5)), blank=80)
    widths(j, [12, 8, 10, 14, 14]); j.freeze_panes = "A6"
    note(j, 5, 7, "Saran: barang kelas A dihitung lebih sering daripada B dan C.", 9, color=MUTE)
    hr = []
    for k, rw in enumerate(rows[:26]):
        q = random.randint(10, 90); f = q + random.choice([0] * 9 + [-1, -2, 1])
        hr.append([rw[3], rw[0], random.choice(ITEMS)[0], q, f, "=IF(B{r}=\"\",\"\",E{r}-D{r})", "=IF(B{r}=\"\",\"\",IF(F{r}=0,1,0))",
                   "=IFERROR(INDEX(Jadwal!$B:$B,MATCH(B{r},Jadwal!$A:$A,0)),\"\")"])
    a2, b2 = table(h, 5, 1, ["Tanggal hitung","Lokasi","SKU","Qty sistem","Qty fisik","Selisih","Akurat (1/0)","Zona (otomatis)"], hr,
                   [D,None,None,N0,N0,'#,##0;[Red]-#,##0;"-"',N0,None], inputs={0,1,2,3,4}, blank=300)
    widths(h, [14, 12, 11, 11, 10, 9, 12, 14]); h.freeze_panes = "A6"
    H = "'Hasil hitung'!"
    kpi(d, 5, 1, "LOKASI DIJADWALKAN", f"=COUNTA(Jadwal!A{a}:A{b})", N0)
    kpi(d, 5, 3, "LOKASI DIHITUNG", f"=COUNTA({H}B{a2}:B{b2})", N0)
    kpi(d, 5, 5, "AKURASI", f"=IFERROR(AVERAGE({H}G{a2}:G{b2}),0)", P1)
    kpi(d, 5, 7, "LOKASI SELISIH", f"=COUNTIF({H}G{a2}:G{b2},0)", N0)
    kpi(d, 5, 9, "PROGRES", "=IFERROR(C6/A6,0)", P1)
    header(d, 9, 1, ["Zona", "Dihitung", "Akurat", "Akurasi"])
    for k, z in enumerate(zones):
        r = 10 + k
        put(d, r, 1, z, align="center"); put(d, r, 2, f"=COUNTIF({H}H{a2}:H{b2},A{r})", N0)
        put(d, r, 3, f"=COUNTIFS({H}H{a2}:H{b2},A{r},{H}G{a2}:G{b2},1)", N0); put(d, r, 4, f"=IFERROR(C{r}/B{r},0)", P1)
    widths(d, [11] * 10)
    bar(d, "F9", "Akurasi per zona", Reference(d, min_col=1, min_row=10, max_row=13), [Reference(d, min_col=4, min_row=9, max_row=13)], w=14)
    return wb

def receiving():
    wb = wb_new()
    lg = sheet(wb, "Log harian", "Log Penerimaan Barang", tab=ACC)
    ck = sheet(wb, "Checklist", "Checklist Penerimaan Barang", note="Pilih Ya atau Tidak di kolom C. Cetak untuk dipakai di area penerimaan.")
    rk = sheet(wb, "Rekap pemasok", "Rekap Penerimaan per Pemasok")
    sup = ["Pemasok A", "Pemasok B", "Pemasok C", "Pemasok D", "Pemasok E"]; rows = []
    for k in range(32):
        q = random.choice([50, 100, 120, 200, 240]); sj = q; rcv = q - random.choice([0] * 7 + [2, 5, 10]); rs = random.choice([0] * 8 + [1, 3])
        rows.append([day(k // 2), f"PO-26{k // 3 + 101:04d}", random.choice(sup), f"SJ-{k + 501}", random.choice(ITEMS)[0], q, sj, rcv, rs,
                     "=IF(B{r}=\"\",\"\",IF(AND(H{r}=F{r},I{r}=0),\"Sesuai\",\"Bermasalah\"))", "" if rcv == q and rs == 0 else ("Kurang kirim" if rcv < q else "Ada barang rusak")])
    a, b = table(lg, 5, 1, ["Tanggal","No. PO","Pemasok","No. surat jalan","SKU","Qty PO","Qty surat jalan","Qty diterima baik","Qty rusak","Status","Catatan"], rows,
                 [D,None,None,None,None,N0,N0,N0,N0,None,None], inputs={0,1,2,3,4,5,6,7,8,10}, blank=200)
    status_color(lg, f"J{a}:J{b}", "Bermasalah", "FFD9D5"); status_color(lg, f"J{a}:J{b}", "Sesuai", "D3F2E4")
    widths(lg, [12, 12, 13, 13, 10, 9, 11, 13, 9, 13, 20]); lg.freeze_panes = "C6"
    items = ["Nomor PO di surat jalan sesuai dengan PO", "Nama pemasok dan alamat kirim sesuai", "Jumlah koli sesuai surat jalan",
             "Qty per SKU sesuai PO dan surat jalan", "Kemasan tidak rusak, basah, atau terbuka", "Label barang dan SKU terbaca jelas",
             "Tanggal kedaluwarsa / batch tercatat (bila ada)", "Barang rusak atau kurang dicatat di surat jalan", "Surat jalan ditandatangani kedua pihak"]
    header(ck, 5, 1, ["No", "Item cek", "Hasil", "Catatan"])
    for k, it in enumerate(items):
        r = 6 + k; put(ck, r, 1, k + 1, align="center"); put(ck, r, 2, it); put(ck, r, 3, "Ya" if k != 7 else "Tidak", inp=True, align="center"); put(ck, r, 4, "", inp=True)
    dv_list(ck, f"C6:C{5 + len(items)}", ["Ya", "Tidak", "N/A"])
    r = 7 + len(items); note(ck, r, 2, "Skor checklist", bold=True); put(ck, r, 3, f'=IFERROR(COUNTIF(C6:C{r-2},"Ya")/(COUNTA(C6:C{r-2})-COUNTIF(C6:C{r-2},"N/A")),0)', P1, bold=True)
    widths(ck, [6, 48, 10, 30])
    header(rk, 5, 1, ["Pemasok", "Kedatangan", "Sesuai", "Bermasalah", "% sesuai", "Qty rusak"])
    LG = "'Log harian'!"
    for k, s in enumerate(sup):
        r = 6 + k
        put(rk, r, 1, s, inp=True); put(rk, r, 2, f"=COUNTIF({LG}C{a}:C{b},A{r})", N0)
        put(rk, r, 3, f"=COUNTIFS({LG}C{a}:C{b},A{r},{LG}J{a}:J{b},\"Sesuai\")", N0); put(rk, r, 4, f"=B{r}-C{r}", N0)
        put(rk, r, 5, f"=IFERROR(C{r}/B{r},0)", P1); put(rk, r, 6, f"=SUMIF({LG}C{a}:C{b},A{r},{LG}I{a}:I{b})", N0)
    widths(rk, [14, 12, 10, 12, 10, 10])
    bar(rk, "H5", "Kedatangan per pemasok", Reference(rk, min_col=1, min_row=6, max_row=10),
        [Reference(rk, min_col=3, min_row=5, max_row=10), Reference(rk, min_col=4, min_row=5, max_row=10)], w=16, colors=("0E9F6E", "E0453A"))
    return wb

def picking():
    wb = wb_new()
    o = sheet(wb, "Daftar order", "Daftar Order & Baris Barang", tab=ACC)
    p = sheet(wb, "Picking list", "Picking List", note="Ketik nomor order di sel kuning. Daftar barang dan lokasinya muncul otomatis, siap dicetak.")
    s = sheet(wb, "Status", "Status Picking")
    rows = []; st = ["Belum", "Dipick", "Siap kirim"]
    for k in range(40):
        on = f"ORD-{1001 + k // 3}"; it = random.choice(ITEMS)
        rows.append([on, day(k // 8), f"Pelanggan {chr(65 + (k // 3) % 8)}", it[0], it[1], random.randint(1, 12),
                     f"{random.choice('ABCD')}-{random.randint(1, 4):02d}-{random.randint(1, 4):02d}", random.choice(st),
                     "=IF(A{r}=\"\",\"\",IF(A{r}='Picking list'!$C$5,COUNTIF($A$6:A{r},'Picking list'!$C$5),\"\"))"])
    a, b = table(o, 5, 1, ["No. order","Tanggal","Pelanggan","SKU","Nama barang","Qty","Lokasi rak","Status","Urutan (bantu)"], rows,
                 [None,D,None,None,None,N0,None,None,N0], inputs=set(range(8)), blank=300)
    dv_list(o, f"H{a}:H{b}", st)
    status_color(o, f"H{a}:H{b}", "Belum", "FFE9C7"); status_color(o, f"H{a}:H{b}", "Siap", "D3F2E4")
    widths(o, [11, 12, 13, 10, 28, 6, 11, 11, 10]); o.freeze_panes = "B6"
    note(p, 5, 1, "No. order", bold=True); put(p, 5, 3, "ORD-1003", inp=True)
    note(p, 6, 1, "Pelanggan", bold=True); put(p, 6, 3, f"=IFERROR(INDEX('Daftar order'!C{a}:C{b},MATCH(C5,'Daftar order'!A{a}:A{b},0)),\"-\")")
    note(p, 7, 1, "Jumlah baris", bold=True); put(p, 7, 3, f"=COUNTIF('Daftar order'!A{a}:A{b},C5)", N0)
    header(p, 9, 1, ["No", "Lokasi rak", "SKU", "Nama barang", "Qty", "Diambil (✓)"])
    O = "'Daftar order'!"
    for k in range(20):
        r = 10 + k; n = k + 1
        put(p, r, 1, f"=IF({n}>$C$7,\"\",{n})", align="center")
        for c, col in ((2, "G"), (3, "D"), (4, "E"), (5, "F")):
            put(p, r, c, f"=IF(A{r}=\"\",\"\",INDEX({O}${col}${a}:${col}${b},MATCH(A{r},{O}$I${a}:$I${b},0)))", N0 if c == 5 else None)
        put(p, r, 6, "")
    widths(p, [6, 12, 11, 30, 7, 12])
    note(p, 31, 1, "Tips: urutkan Daftar order berdasarkan Lokasi rak supaya rute ambil barang lebih pendek.", 9, color=MUTE)
    header(s, 5, 1, ["Status", "Baris", "Order (unik, perkiraan)"])
    for k, x in enumerate(st):
        r = 6 + k; put(s, r, 1, x); put(s, r, 2, f"=COUNTIF({O}H{a}:H{b},A{r})", N0)
        put(s, r, 3, f"=SUMPRODUCT(({O}H{a}:H{b}=A{r})/COUNTIFS({O}A{a}:A{b},{O}A{a}:A{b}&\"\",{O}H{a}:H{b},{O}H{a}:H{b}&\"\"))", N1)
    kpi(s, 10, 1, "TOTAL BARIS", "=SUM(B6:B8)", N0); kpi(s, 10, 3, "% SIAP KIRIM", "=IFERROR(B8/SUM(B6:B8),0)", P1)
    widths(s, [14, 10, 20, 12])
    pie(s, "F5", "Status baris picking", Reference(s, min_col=1, min_row=6, max_row=8), Reference(s, min_col=2, min_row=5, max_row=8))
    return wb

def rak():
    wb = wb_new()
    m = sheet(wb, "Master lokasi", "Master Lokasi Rak", tab=ACC)
    s = sheet(wb, "Status lokasi", "Status Isi Lokasi")
    d = sheet(wb, "Dashboard", "Dashboard Utilisasi Rak")
    rows = []
    for z in "ABCD":
        for rk in range(1, 4):
            for lv in range(1, 5):
                rows.append([f"{z}-{rk:02d}-{lv:02d}", z, rk, lv, 2 if lv < 4 else 1])
    a, b = table(m, 5, 1, ["Kode lokasi","Zona","Rak","Level","Kapasitas (palet)"], rows, [None,None,N0,N0,N0], inputs=set(range(5)), blank=100)
    widths(m, [12, 8, 7, 7, 14]); m.freeze_panes = "A6"
    sr = []
    for x in rows:
        q = random.choice([0, 1, 2, 2, 2, 1]) if x[4] == 2 else random.choice([0, 1, 1])
        sr.append([x[0], "=IFERROR(INDEX('Master lokasi'!$B:$B,MATCH(A{r},'Master lokasi'!$A:$A,0)),\"\")",
                   "=IFERROR(INDEX('Master lokasi'!$E:$E,MATCH(A{r},'Master lokasi'!$A:$A,0)),0)", q,
                   random.choice(ITEMS)[0] if q else "", "=IF(A{r}=\"\",\"\",IF(D{r}=0,\"Kosong\",IF(D{r}>=C{r},\"Penuh\",\"Sebagian\")))"])
    a2, b2 = table(s, 5, 1, ["Kode lokasi","Zona (otomatis)","Kapasitas (otomatis)","Terisi (palet)","SKU","Status"], sr,
                   [None,None,N0,N0,None,None], inputs={0,3,4}, blank=100)
    for w, c in (("Kosong", "D3F2E4"), ("Penuh", "FFD9D5"), ("Sebagian", "FFF1C2")): status_color(s, f"F{a2}:F{b2}", w, c)
    widths(s, [12, 14, 16, 13, 11, 11]); s.freeze_panes = "A6"
    S = "'Status lokasi'!"
    kpi(d, 5, 1, "TOTAL LOKASI", f"=COUNTA({S}A{a2}:A{b2})", N0)
    kpi(d, 5, 3, "UTILISASI PALET", f"=IFERROR(SUM({S}D{a2}:D{b2})/SUM({S}C{a2}:C{b2}),0)", P1)
    kpi(d, 5, 5, "LOKASI KOSONG", f"=COUNTIF({S}F{a2}:F{b2},\"Kosong\")", N0)
    kpi(d, 5, 7, "LOKASI PENUH", f"=COUNTIF({S}F{a2}:F{b2},\"Penuh\")", N0)
    header(d, 9, 1, ["Zona", "Kapasitas", "Terisi", "Utilisasi"])
    for k, z in enumerate("ABCD"):
        r = 10 + k; put(d, r, 1, z, align="center")
        put(d, r, 2, f"=SUMIF({S}B{a2}:B{b2},A{r},{S}C{a2}:C{b2})", N0); put(d, r, 3, f"=SUMIF({S}B{a2}:B{b2},A{r},{S}D{a2}:D{b2})", N0)
        put(d, r, 4, f"=IFERROR(C{r}/B{r},0)", P1)
    widths(d, [11] * 9)
    bar(d, "F9", "Utilisasi per zona", Reference(d, min_col=1, min_row=10, max_row=13), [Reference(d, min_col=4, min_row=9, max_row=13)], w=14)
    return wb

def kpi_gudang():
    wb = wb_new()
    i = sheet(wb, "Input bulanan", "KPI Gudang · Input Bulanan", tab=ACC)
    t = sheet(wb, "Target", "Target KPI", note="Isi target sesuai kebijakan perusahaan Anda. Angka bawaan adalah CONTOH.")
    d = sheet(wb, "Dashboard", "Dashboard KPI Gudang")
    bl = ["Jan","Feb","Mar","Apr","Mei","Jun","Jul","Agu","Sep","Okt"]; rows = []
    for m in bl:
        o = random.randint(1800, 2600); lc = random.randint(300, 400)
        rows.append([f"{m} 2026", o, int(o * random.uniform(.9, .98)), lc, int(lc * random.uniform(.95, .995)), random.randint(60, 90), round(random.uniform(60, 130), 0),
                     random.randint(9000, 13000), random.randint(700, 900),
                     "=IF(A{r}=\"\",\"\",IFERROR(C{r}/B{r},0))", "=IF(A{r}=\"\",\"\",IFERROR(E{r}/D{r},0))", "=IF(A{r}=\"\",\"\",IFERROR(G{r}/F{r},0))", "=IF(A{r}=\"\",\"\",IFERROR(H{r}/I{r},0))"])
    a, b = table(i, 5, 1, ["Bulan","Total order","Order tepat waktu","Lokasi dihitung","Lokasi akurat","Jumlah penerimaan","Total jam dock to stock","Baris dipick","Jam kerja picker",
                           "Ketepatan order","Akurasi stok","Dock to stock (jam / penerimaan)","Produktivitas (baris / jam)"], rows,
                 [None,N0,N0,N0,N0,N0,N0,N0,N0,P1,P1,N1,N1], inputs=set(range(9)), blank=14)
    widths(i, [11, 10, 12, 11, 10, 12, 13, 10, 11, 11, 10, 14, 14]); i.freeze_panes = "B6"
    header(t, 5, 1, ["KPI", "Target", "Arah"])
    tg = [("Ketepatan order", .95, P1, "Lebih tinggi lebih baik"), ("Akurasi stok", .98, P1, "Lebih tinggi lebih baik"),
          ("Dock to stock (jam / penerimaan)", 1.5, N1, "Lebih rendah lebih baik"), ("Produktivitas (baris / jam)", 13, N1, "Lebih tinggi lebih baik")]
    for k, (n, v, f, ar) in enumerate(tg):
        put(t, 6 + k, 1, n); put(t, 6 + k, 2, v, f, inp=True); put(t, 6 + k, 3, ar)
    widths(t, [32, 10, 24])
    d["A5"] = "Bulan yang ditampilkan"; d["A5"].font = Font(name=F, bold=True)
    put(d, 5, 4, "Okt 2026", inp=True)
    header(d, 7, 1, ["KPI", "", "", "Aktual", "Target", "Status"])
    I = "'Input bulanan'!"
    for k, (n, v, f, ar) in enumerate(tg):
        r = 8 + k; col = "JKLM"[k]
        d.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3); put(d, r, 1, n, bold=True)
        put(d, r, 4, f"=IFERROR(INDEX({I}{col}{a}:{col}{b},MATCH($D$5,{I}A{a}:A{b},0)),\"-\")", f, size=12, bold=True)
        put(d, r, 5, f"=Target!B{6 + k}", f)
        cmp = ">=" if "tinggi" in ar else "<="
        put(d, r, 6, f"=IF(D{r}=\"-\",\"-\",IF(D{r}{cmp}E{r},\"Tercapai\",\"Belum\"))", align="center")
    status_color(d, "F8:F11", "Tercapai", "D3F2E4"); status_color(d, "F8:F11", "Belum", "FFD9D5")
    widths(d, [10, 10, 10, 13, 11, 12])
    line(d, "H5", "Ketepatan order & akurasi stok", Reference(i, min_col=1, min_row=6, max_row=15),
         [Reference(i, min_col=10, min_row=5, max_row=15), Reference(i, min_col=11, min_row=5, max_row=15)], w=17)
    bar(d, "A14", "Produktivitas picker (baris / jam)", Reference(i, min_col=1, min_row=6, max_row=15), [Reference(i, min_col=13, min_row=5, max_row=15)], w=13, titles=True)
    bar(d, "H21", "Dock to stock (jam / penerimaan)", Reference(i, min_col=1, min_row=6, max_row=15), [Reference(i, min_col=12, min_row=5, max_row=15)], w=17, colors=(ACC,))
    return wb

def checklist_5r():
    wb = wb_new()
    c = sheet(wb, "Checklist", "Checklist 5R & K3 Gudang", tab=ACC, note="Pilih Ya/Tidak/N/A untuk setiap item per area. Item bisa Anda ubah sesuai kondisi gudang.")
    t = sheet(wb, "Temuan", "Daftar Temuan & Tindak Lanjut")
    r_ = sheet(wb, "Rekap skor", "Rekap Skor per Area")
    areas = ["Penerimaan", "Rak penyimpanan", "Area picking", "Area packing", "Area pengiriman", "Kantor gudang"]
    items = [("Ringkas", "Barang tidak terpakai sudah dipisahkan dan diberi label"), ("Rapi", "Setiap barang dan alat punya tempat dan label lokasi"),
             ("Resik", "Lantai dan rak bersih dari sampah, debu, dan tumpahan"), ("Rawat", "Kondisi rapi dan bersih dipertahankan sesuai jadwal"),
             ("Rajin", "Staf mengikuti aturan 5R tanpa harus diingatkan"), ("K3", "Jalur pejalan kaki dan jalur forklift bebas halangan"),
             ("K3", "APAR mudah dijangkau dan tidak terhalang barang"), ("K3", "Staf memakai APD sesuai area"), ("K3", "Tumpukan barang stabil dan tidak melebihi batas")]
    header(c, 5, 1, ["Area", "Kategori", "Item cek"] + ["Hasil"])
    r = 6; rows_area = {}
    for ar in areas:
        st = r
        for kat, it in items:
            put(c, r, 1, ar); put(c, r, 2, kat, align="center"); put(c, r, 3, it)
            put(c, r, 4, random.choice(["Ya"] * 6 + ["Tidak", "N/A"]), inp=True, align="center"); r += 1
        rows_area[ar] = (st, r - 1)
    dv_list(c, f"D6:D{r - 1}", ["Ya", "Tidak", "N/A"])
    c.conditional_formatting.add(f"D6:D{r-1}", CellIsRule(operator="equal", formula=['"Tidak"'], fill=PatternFill("solid", fgColor="FFD9D5")))
    widths(c, [18, 10, 58, 9]); c.freeze_panes = "A6"; last = r - 1
    tm = [[day(3), "Area packing", "Tumpukan karton menghalangi jalur pejalan kaki", "Supervisor packing", day(5), "Selesai"],
          [day(3), "Rak penyimpanan", "Label lokasi rak B-02 rusak", "Admin gudang", day(7), "Proses"],
          [day(4), "Area pengiriman", "APAR terhalang palet kosong", "Kepala gudang", day(4), "Selesai"]]
    a, b = table(t, 5, 1, ["Tanggal", "Area", "Temuan", "PIC", "Target selesai", "Status", "Terlambat?"], [x + ["=IF(A{r}=\"\",\"\",IF(AND(F{r}<>\"Selesai\",E{r}<TODAY()),\"Ya\",\"Tidak\"))"] for x in tm],
                 [D, None, None, None, D, None, None], inputs={0, 1, 2, 3, 4, 5}, blank=60)
    dv_list(t, f"F{a}:F{b}", ["Proses", "Selesai"]); status_color(t, f"G{a}:G{b}", "Ya", "FFD9D5")
    widths(t, [12, 16, 46, 18, 13, 10, 11])
    header(r_, 5, 1, ["Area", "Ya", "Tidak", "Skor", "Temuan terbuka"])
    for k, ar in enumerate(areas):
        rr = 6 + k
        put(r_, rr, 1, ar); put(r_, rr, 2, f"=COUNTIFS(Checklist!$A$6:$A${last},A{rr},Checklist!$D$6:$D${last},\"Ya\")", N0)
        put(r_, rr, 3, f"=COUNTIFS(Checklist!$A$6:$A${last},A{rr},Checklist!$D$6:$D${last},\"Tidak\")", N0)
        put(r_, rr, 4, f"=IFERROR(B{rr}/(B{rr}+C{rr}),0)", P1); put(r_, rr, 5, f"=COUNTIFS(Temuan!B{a}:B{b},A{rr},Temuan!F{a}:F{b},\"Proses\")", N0)
    kpi(r_, 13, 1, "SKOR GUDANG", "=IFERROR(SUM(B6:B11)/(SUM(B6:B11)+SUM(C6:C11)),0)", P1)
    widths(r_, [18, 8, 8, 9, 14])
    bar(r_, "G5", "Skor 5R & K3 per area", Reference(r_, min_col=1, min_row=6, max_row=11), [Reference(r_, min_col=4, min_row=5, max_row=11)], w=16, horizontal=True)
    return wb
