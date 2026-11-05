from lib import *
from inv import ITEMS

KOTA = ["Jakarta", "Bandung", "Surabaya", "Semarang", "Medan", "Makassar", "Denpasar", "Balikpapan"]
OPSI = ["Opsi A", "Opsi B", "Opsi C"]

def tracker():
    wb = wb_new()
    k = sheet(wb, "Daftar kiriman", "Tracker Pengiriman", tab=ACC)
    d = sheet(wb, "Dashboard", "Dashboard Ketepatan Waktu")
    t = sheet(wb, "Rekap tujuan", "Rekap per Kota Tujuan")
    rows = []
    for n in range(40):
        kt = random.choice(KOTA); sla = {"Jakarta": 1, "Bandung": 2, "Surabaya": 3, "Semarang": 2}.get(kt, 4)
        snd = day(n // 2); lat = random.choice([0] * 8 + [1, 2]); got = None if n > 35 else snd + dt.timedelta(days=sla + lat - random.choice([0, 0, 1]))
        rows.append([f"KRM-{n + 1:04d}", snd, f"Pelanggan {chr(65 + n % 10)}", kt, random.choice(OPSI), random.randint(1, 8), sla,
                     "=IF(A{r}=\"\",\"\",B{r}+G{r})", got,
                     "=IF(A{r}=\"\",\"\",IF(I{r}=\"\",IF(TODAY()>H{r},\"Terlambat (belum sampai)\",\"Dalam perjalanan\"),IF(I{r}<=H{r},\"Tepat waktu\",\"Terlambat\")))",
                     "=IF(OR(A{r}=\"\",I{r}=\"\"),\"\",MAX(0,I{r}-H{r}))"])
    a, b = table(k, 5, 1, ["No. kiriman","Tanggal kirim","Penerima","Kota tujuan","Layanan","Koli","Janji (hari)","Target tiba","Tanggal diterima","Status","Terlambat (hari)"], rows,
                 [None,D,None,None,None,N0,N0,D,D,None,N0], inputs={0,1,2,3,4,5,6,8}, blank=300)
    for w, c in (("Tepat", "D3F2E4"), ("Terlambat", "FFD9D5"), ("perjalanan", "FFF1C2")): status_color(k, f"J{a}:J{b}", w, c)
    widths(k, [12, 12, 13, 13, 10, 6, 10, 12, 14, 22, 12]); k.freeze_panes = "B6"
    K = "'Daftar kiriman'!"
    kpi(d, 5, 1, "TOTAL KIRIMAN", f"=COUNTA({K}A{a}:A{b})", N0)
    kpi(d, 5, 3, "SUDAH DITERIMA", f"=COUNT({K}I{a}:I{b})", N0)
    kpi(d, 5, 5, "TEPAT WAKTU", f"=IFERROR(COUNTIF({K}J{a}:J{b},\"Tepat waktu\")/C6,0)", P1)
    kpi(d, 5, 7, "RATA-RATA TERLAMBAT", f"=IFERROR(AVERAGEIF({K}K{a}:K{b},\">0\"),0)", '0.0" hari"')
    header(d, 9, 1, ["Status", "Jumlah"])
    for n, s in enumerate(["Tepat waktu", "Terlambat", "Dalam perjalanan", "Terlambat (belum sampai)"]):
        r = 10 + n; put(d, r, 1, s); put(d, r, 2, f"=COUNTIF({K}J{a}:J{b},A{r})", N0)
    widths(d, [22, 10, 12, 12, 12, 12, 12, 12])
    pie(d, "D9", "Status kiriman", Reference(d, min_col=1, min_row=10, max_row=13), Reference(d, min_col=2, min_row=9, max_row=13))
    header(t, 5, 1, ["Kota tujuan", "Kiriman", "Diterima", "Tepat waktu", "% tepat waktu"])
    for n, c in enumerate(KOTA):
        r = 6 + n; put(t, r, 1, c, inp=True); put(t, r, 2, f"=COUNTIF({K}D{a}:D{b},A{r})", N0)
        put(t, r, 3, f"=COUNTIFS({K}D{a}:D{b},A{r},{K}I{a}:I{b},\"<>\")", N0)
        put(t, r, 4, f"=COUNTIFS({K}D{a}:D{b},A{r},{K}J{a}:J{b},\"Tepat waktu\")", N0); put(t, r, 5, f"=IFERROR(D{r}/C{r},0)", P1)
    widths(t, [14, 10, 10, 12, 13])
    bar(t, "G5", "% tepat waktu per kota", Reference(t, min_col=1, min_row=6, max_row=13), [Reference(t, min_col=5, min_row=5, max_row=13)], w=16, horizontal=True)
    return wb

def berat_volume():
    wb = wb_new()
    c = sheet(wb, "Kalkulator", "Kalkulator Berat Volume & Ongkir", tab=ACC)
    l = sheet(wb, "Daftar paket", "Daftar Paket")
    p = sheet(wb, "Panduan", "Panduan", note="Penjelasan rumus berat volume.")
    lab = [("Panjang (cm)", 40, N0), ("Lebar (cm)", 30, N0), ("Tinggi (cm)", 25, N0), ("Berat aktual (kg)", 3.2, N1),
           ("Pembagi berat volume", 6000, N0), ("Tarif per kg (Rp)", 12000, RP)]
    for n, (t_, v, f) in enumerate(lab):
        r = 5 + n; note(c, r, 1, t_, bold=True); put(c, r, 3, v, f, inp=True)
    out = [("Berat volume (kg)", "=IFERROR(C5*C6*C7/C9,0)", N2), ("Berat ditagih (sebelum pembulatan)", "=MAX(C8,C12)", N2),
           ("Berat ditagih (dibulatkan ke atas, kg)", "=ROUNDUP(C13,0)", N0), ("Estimasi ongkir", "=C14*C10", RP)]
    for n, (t_, f, fm) in enumerate(out):
        r = 12 + n; note(c, r, 1, t_, bold=True); put(c, r, 3, f, fm, bold=True, size=12)
    note(c, 17, 1, "Pembulatan tiap layanan bisa berbeda (misalnya per 0,5 kg atau per 1 kg). Cek aturan resmi layanan yang Anda pakai.", 9, color=MUTE)
    c.merge_cells("A17:F17"); widths(c, [36, 2, 16, 4, 4, 4])
    note(l, 5, 1, "Pembagi", bold=True); put(l, 5, 2, "=Kalkulator!C9", N0); note(l, 5, 3, "Tarif/kg", bold=True); put(l, 5, 4, "=Kalkulator!C10", RP)
    rows = []
    for n in range(10):
        rows.append([f"PKT-{n + 1:03d}", random.choice([20, 30, 40, 50, 60]), random.choice([15, 20, 30, 40]), random.choice([10, 15, 20, 30]), round(random.uniform(.5, 9), 1),
                     "=IF(A{r}=\"\",\"\",B{r}*C{r}*D{r}/$B$5)", "=IF(A{r}=\"\",\"\",ROUNDUP(MAX(E{r},F{r}),0))", "=IF(A{r}=\"\",\"\",G{r}*$D$5)",
                     "=IF(A{r}=\"\",\"\",IF(F{r}>E{r},\"Berat volume\",\"Berat aktual\"))"])
    a, b = table(l, 7, 1, ["No. paket", "P (cm)", "L (cm)", "T (cm)", "Berat aktual (kg)", "Berat volume (kg)", "Berat ditagih (kg)", "Estimasi ongkir", "Penentu"], rows,
                 [None, N0, N0, N0, N1, N2, N0, RP, None], inputs={0, 1, 2, 3, 4}, blank=90)
    put(l, b + 1, 7, f"=SUM(G{a}:G{b})", N0, bold=True); put(l, b + 1, 8, f"=SUM(H{a}:H{b})", RP, bold=True); put(l, b + 1, 6, "Total", bold=True)
    widths(l, [11, 8, 8, 8, 13, 13, 13, 15, 13]); l.freeze_panes = "A8"
    txt = ["Berat volume = panjang × lebar × tinggi (cm) ÷ pembagi.",
           "Acuan IATA untuk kargo udara memakai pembagi 6.000 (volume dalam cm³ ÷ 6.000 = kg). Sebagian layanan ekspres memakai 5.000. Selalu cek angka resmi layanan Anda.",
           "Berat yang ditagih adalah berat aktual atau berat volume, mana yang lebih besar.",
           "Ukur sisi terluar paket, termasuk kemasan dan bantalan.",
           "Penjelasan lengkap: ngertilogistik.web.id/blog/berat-volume"]
    widths(p, [100])
    for n, s in enumerate(txt): note(p, 5 + n * 2, 1, s, 11); p.row_dimensions[5 + n * 2].height = 30
    return wb

def armada():
    wb = wb_new()
    j = sheet(wb, "Jadwal", "Jadwal Armada Mingguan", tab=ACC)
    l = sheet(wb, "Log ritase", "Log Ritase")
    d = sheet(wb, "Dashboard", "Dashboard Armada")
    note(j, 5, 1, "Master armada", bold=True, color=NAVY2)
    fl = [("TRK-01", "Truk engkel", 2000), ("TRK-02", "Truk engkel", 2000), ("TRK-03", "Truk double", 4500), ("TRK-04", "Truk double", 4500),
          ("TRK-05", "Pikap", 800), ("TRK-06", "Pikap", 800), ("TRK-07", "Truk double", 4500), ("TRK-08", "Truk engkel", 2000)]
    a, b = table(j, 6, 1, ["Kode armada", "Jenis", "Kapasitas (kg)"], [list(x) for x in fl], [None, None, N0], inputs={0, 1, 2}, blank=12)
    note(j, b + 1, 1, "Kapasitas di atas adalah CONTOH. Isi sesuai kapasitas resmi kendaraan Anda.", 9, color=MUTE)
    hr = b + 3; note(j, hr, 1, "Jadwal rute per hari (isi kode rute)", bold=True, color=NAVY2)
    days_ = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    header(j, hr + 1, 1, ["Kode armada"] + days_)
    for n, x in enumerate(fl):
        r = hr + 2 + n; put(j, r, 1, x[0])
        for c in range(7): put(j, r, 2 + c, random.choice(["R1", "R2", "R3", "R4", ""]) if c < 6 else "", inp=True, align="center")
    widths(j, [13, 13, 14, 9, 9, 9, 9, 9])
    rows = []; rutes = {"R1": "Gudang - Kota A", "R2": "Gudang - Kota B", "R3": "Gudang - Kota C", "R4": "Gudang - Kota D"}
    for n in range(36):
        f = random.choice(fl); rt = random.choice(list(rutes))
        rows.append([day(n // 5), f[0], rt, rutes[rt], int(f[2] * random.uniform(.5, .98)),
                     f"=IFERROR(INDEX(Jadwal!$C${a}:$C${b},MATCH(B{{r}},Jadwal!$A${a}:$A${b},0)),0)", "=IF(B{r}=\"\",\"\",IFERROR(E{r}/F{r},0))", random.randint(40, 260)])
    a2, b2 = table(l, 5, 1, ["Tanggal", "Kode armada", "Kode rute", "Rute", "Muatan (kg)", "Kapasitas (otomatis)", "Utilisasi", "Jarak (km)"], rows,
                   [D, None, None, None, N0, N0, P1, N0], inputs={0, 1, 2, 3, 4, 7}, blank=300)
    widths(l, [12, 13, 10, 18, 12, 16, 10, 10]); l.freeze_panes = "A6"
    L_ = "'Log ritase'!"
    kpi(d, 5, 1, "TOTAL RITASE", f"=COUNTA({L_}B{a2}:B{b2})", N0)
    kpi(d, 5, 3, "UTILISASI RATA-RATA", f"=IFERROR(AVERAGE({L_}G{a2}:G{b2}),0)", P1)
    kpi(d, 5, 5, "TOTAL MUATAN", f"=SUM({L_}E{a2}:E{b2})", '#,##0" kg"', w=2)
    kpi(d, 5, 7, "TOTAL JARAK", f"=SUM({L_}H{a2}:H{b2})", '#,##0" km"')
    header(d, 9, 1, ["Armada", "Ritase", "Muatan (kg)", "Utilisasi rata-rata"])
    for n, x in enumerate(fl):
        r = 10 + n; put(d, r, 1, f"=Jadwal!A{a + n}"); put(d, r, 2, f"=COUNTIF({L_}B{a2}:B{b2},A{r})", N0)
        put(d, r, 3, f"=SUMIF({L_}B{a2}:B{b2},A{r},{L_}E{a2}:E{b2})", N0); put(d, r, 4, f"=IFERROR(AVERAGEIF({L_}B{a2}:B{b2},A{r},{L_}G{a2}:G{b2}),0)", P1)
    widths(d, [12, 9, 13, 16, 11, 11, 11, 11])
    bar(d, "F9", "Ritase per armada", Reference(d, min_col=1, min_row=10, max_row=17), [Reference(d, min_col=2, min_row=9, max_row=17)], w=15)
    bar(d, "F25", "Utilisasi rata-rata per armada", Reference(d, min_col=1, min_row=10, max_row=17), [Reference(d, min_col=4, min_row=9, max_row=17)], w=15, colors=(ACC,))
    return wb

def tarif():
    wb = wb_new()
    i = sheet(wb, "Input tarif", "Perbandingan Tarif · Input", tab=ACC, note="Isi tarif per kg, minimum berat, dan estimasi hari tiap opsi. Semua angka bawaan adalah CONTOH.")
    c = sheet(wb, "Perbandingan", "Perbandingan per Rute")
    s = sheet(wb, "Ringkasan", "Ringkasan")
    rows = []
    for kt in KOTA[1:]:
        base = random.randint(6, 30) * 1000
        row = [f"Jakarta - {kt}", random.choice([10, 25, 50, 100])]
        for o in OPSI: row += [int(base * random.uniform(.8, 1.25) / 500) * 500, random.choice([5, 10]), random.randint(2, 7)]
        rows.append(row)
    names = ["Rute", "Berat kiriman (kg)"]
    for o in OPSI: names += [f"{o} tarif/kg", f"{o} min. kg", f"{o} estimasi hari"]
    a, b = table(i, 5, 1, names, rows, [None, N0] + [RP, N0, N0] * 3, inputs=set(range(11)), blank=30)
    widths(i, [22, 12] + [12, 9, 11] * 3); i.freeze_panes = "C6"
    header(c, 5, 1, ["Rute", "Biaya " + OPSI[0], "Biaya " + OPSI[1], "Biaya " + OPSI[2], "Termurah", "Selisih termurah vs termahal", "Tercepat"])
    I = "'Input tarif'!"
    for k in range(b - a + 1):
        r = a + k
        put(c, r, 1, f"=IF({I}A{r}=\"\",\"\",{I}A{r})")
        for n, (tc, mc) in enumerate((("C", "D"), ("F", "G"), ("I", "J"))):
            put(c, r, 2 + n, f"=IF({I}A{r}=\"\",\"\",{I}{tc}{r}*MAX({I}B{r},{I}{mc}{r}))", RP)
        put(c, r, 5, f"=IF(A{r}=\"\",\"\",IF(B{r}=MIN(B{r}:D{r}),\"{OPSI[0]}\",IF(C{r}=MIN(B{r}:D{r}),\"{OPSI[1]}\",\"{OPSI[2]}\")))")
        put(c, r, 6, f"=IF(A{r}=\"\",\"\",MAX(B{r}:D{r})-MIN(B{r}:D{r}))", RP)
        mn = f"MIN({I}E{r},{I}H{r},{I}K{r})"
        put(c, r, 7, f"=IF(A{r}=\"\",\"\",IF({I}E{r}={mn},\"{OPSI[0]}\",IF({I}H{r}={mn},\"{OPSI[1]}\",\"{OPSI[2]}\")))")
    widths(c, [22, 15, 15, 15, 11, 18, 11])
    header(s, 5, 1, ["Opsi", "Rute termurah", "Rute tercepat"])
    for n, o in enumerate(OPSI):
        r = 6 + n; put(s, r, 1, o); put(s, r, 2, f"=COUNTIF(Perbandingan!E{a}:E{b},A{r})", N0); put(s, r, 3, f"=COUNTIF(Perbandingan!G{a}:G{b},A{r})", N0)
    kpi(s, 10, 1, "POTENSI HEMAT (PILIH TERMURAH VS TERMAHAL)", f"=SUM(Perbandingan!F{a}:F{b})", RP, w=3)
    note(s, 13, 1, "Biaya = tarif per kg × berat (atau minimum kg bila berat lebih kecil). Biaya tambahan seperti asuransi atau packing belum dihitung.", 9, color=MUTE)
    widths(s, [14, 14, 14])
    bar(s, "E5", "Jumlah rute termurah & tercepat per opsi", Reference(s, min_col=1, min_row=6, max_row=8),
        [Reference(s, min_col=2, min_row=5, max_row=8), Reference(s, min_col=3, min_row=5, max_row=8)], w=15)
    return wb

def retur():
    wb = wb_new()
    l = sheet(wb, "Log retur", "Tracker Retur Barang", tab=ACC)
    a_ = sheet(wb, "Alasan", "Daftar Alasan & Keputusan", note="Ubah daftar alasan dan keputusan sesuai kebutuhan. Daftar ini dipakai sebagai pilihan di Log retur.")
    d = sheet(wb, "Dashboard", "Dashboard Retur")
    als = ["Barang rusak", "Salah kirim barang", "Salah ukuran / varian", "Tidak sesuai deskripsi", "Kedaluwarsa", "Pelanggan berubah pikiran"]
    kep = ["Restock", "Perbaikan", "Kembali ke pemasok", "Dimusnahkan"]
    header(a_, 5, 1, ["Alasan retur"]); header(a_, 5, 3, ["Keputusan"])
    for n, x in enumerate(als): put(a_, 6 + n, 1, x, inp=True)
    for n, x in enumerate(kep): put(a_, 6 + n, 3, x, inp=True)
    widths(a_, [28, 3, 22])
    rows = []
    for n in range(27):
        done = n < 19; t0 = day(n)
        rows.append([f"RTR-{n + 1:03d}", t0, f"ORD-{2000 + n * 3}", random.choice(ITEMS)[0], random.randint(1, 4), random.choice(als),
                     random.choice(["Baik", "Rusak ringan", "Rusak berat"]), random.choice(kep) if done else "", t0 + dt.timedelta(days=random.randint(1, 6)) if done else None,
                     "=IF(A{r}=\"\",\"\",IF(I{r}=\"\",\"Proses\",\"Selesai\"))", "=IF(OR(A{r}=\"\",I{r}=\"\"),\"\",I{r}-B{r})"])
    a, b = table(l, 5, 1, ["No. retur", "Tanggal masuk", "No. order", "SKU", "Qty", "Alasan", "Kondisi", "Keputusan", "Tanggal selesai", "Status", "Lama proses (hari)"], rows,
                 [None, D, None, None, N0, None, None, None, D, None, N0], inputs=set(range(9)), blank=300)
    for col, rng in (("F", "Alasan!$A$6:$A$20"), ("H", "Alasan!$C$6:$C$20")):
        dv = DataValidation(type="list", formula1=rng, allow_blank=True); l.add_data_validation(dv); dv.add(f"{col}{a}:{col}{b}")
    dv_list(l, f"G{a}:G{b}", ["Baik", "Rusak ringan", "Rusak berat"])
    status_color(l, f"J{a}:J{b}", "Proses", "FFF1C2"); status_color(l, f"J{a}:J{b}", "Selesai", "D3F2E4")
    widths(l, [11, 13, 11, 10, 6, 24, 13, 18, 14, 10, 12]); l.freeze_panes = "B6"
    L_ = "'Log retur'!"
    kpi(d, 5, 1, "RETUR MASUK", f"=COUNTA({L_}A{a}:A{b})", N0); kpi(d, 5, 3, "SELESAI", f"=COUNTIF({L_}J{a}:J{b},\"Selesai\")", N0)
    kpi(d, 5, 5, "MASIH PROSES", f"=COUNTIF({L_}J{a}:J{b},\"Proses\")", N0); kpi(d, 5, 7, "RATA-RATA LAMA", f"=IFERROR(AVERAGE({L_}K{a}:K{b}),0)", '0.0" hari"')
    header(d, 9, 1, ["Alasan", "Jumlah"]); header(d, 9, 4, ["Keputusan", "Jumlah"])
    for n in range(len(als)):
        r = 10 + n; put(d, r, 1, f"=Alasan!A{6 + n}"); put(d, r, 2, f"=COUNTIF({L_}F{a}:F{b},A{r})", N0)
    for n in range(len(kep)):
        r = 10 + n; put(d, r, 4, f"=Alasan!C{6 + n}"); put(d, r, 5, f"=COUNTIF({L_}H{a}:H{b},D{r})", N0)
    widths(d, [26, 9, 3, 20, 9, 11, 11, 11])
    bar(d, "A18", "Alasan retur", Reference(d, min_col=1, min_row=10, max_row=15), [Reference(d, min_col=2, min_row=9, max_row=15)], w=14, horizontal=True)
    pie(d, "G18", "Keputusan retur", Reference(d, min_col=4, min_row=10, max_row=13), Reference(d, min_col=5, min_row=9, max_row=13))
    return wb

def surat_jalan():
    wb = wb_new()
    dbg = sheet(wb, "Data barang", "Data Barang Kiriman", tab=ACC, note="Isi data dokumen dan barang di sheet ini. Packing list dan surat jalan terisi otomatis, siap cetak.")
    pl = sheet(wb, "Packing list", "PACKING LIST", note=" ")
    sj = sheet(wb, "Surat jalan", "SURAT JALAN", note=" ")
    wb.move_sheet("Data barang", 0)
    info = [("No. dokumen", "SJ-0012"), ("Tanggal", dt.date(2026, 11, 5)), ("Pengirim", "Nama perusahaan Anda"), ("Alamat pengirim", "Alamat lengkap pengirim"),
            ("Penerima", "Nama penerima"), ("Alamat penerima", "Alamat lengkap penerima"), ("No. referensi / PO", "PO-260115"), ("Kendaraan / no. polisi", "(isi)"), ("Pengemudi", "(isi)")]
    for n, (k, v) in enumerate(info):
        note(dbg, 5 + n, 1, k, bold=True); put(dbg, 5 + n, 2, v, D if isinstance(v, dt.date) else None, inp=True)
    rows = []
    for n, it in enumerate(ITEMS[:6]):
        rows.append([n + 1, it[1], it[0], random.randint(5, 40), it[2], random.randint(1, 4), round(random.uniform(8, 30), 1), f"{random.choice([40,50,60])}x{random.choice([30,40])}x{random.choice([25,30,40])}",
                     "=IF(B{r}=\"\",\"\",F{r}*G{r})"])
    a, b = table(dbg, 16, 1, ["No", "Nama barang", "SKU", "Qty", "Satuan", "Koli", "Berat per koli (kg)", "Dimensi koli (cm)", "Berat total (kg)"], rows,
                 [N0, None, None, N0, None, N0, N1, None, N1], inputs=set(range(8)), blank=14)
    widths(dbg, [22, 34, 10, 7, 8, 7, 14, 15, 13])
    DB = "'Data barang'!"
    def doc(ws, cols, srcs, fmts, sign):
        for n, (k, _) in enumerate(info[:7] if ws is pl else info):
            note(ws, 5 + n, 1, k, bold=True); put(ws, 5 + n, 2, f"={DB}B{5 + n}", D if k == "Tanggal" else None)
            ws.merge_cells(start_row=5 + n, start_column=2, end_row=5 + n, end_column=len(cols))
        hr = 16; header(ws, hr, 1, cols)
        for k in range(b - a + 1):
            r = hr + 1 + k; sr = a + k
            for j, (sc, fm) in enumerate(zip(srcs, fmts)):
                put(ws, r, 1 + j, f"=IF({DB}B{sr}=\"\",\"\",{DB}{sc}{sr})", fm)
        tr = hr + 2 + (b - a)
        put(ws, tr, 1, "TOTAL", bold=True)
        for j, sc in enumerate(srcs):
            if sc in ("F", "I", "D"): put(ws, tr, 1 + j, f"=SUM({L(1 + j)}{hr + 1}:{L(1 + j)}{tr - 1})", fmts[j], bold=True)
        for j, who in enumerate(sign):
            c = 1 + j * max(1, len(cols) // len(sign)); note(ws, tr + 3, c, who, bold=True); note(ws, tr + 8, c, "(..........................)")
        ws.print_area = f"A1:{L(len(cols))}{tr + 9}"; ws.page_setup.fitToWidth = 1; ws.sheet_properties.pageSetUpPr.fitToPage = True
    doc(pl, ["No", "Nama barang", "SKU", "Qty", "Satuan", "Koli", "Berat/koli (kg)", "Dimensi (cm)", "Berat total (kg)"], list("ABCDEFGHI"), [N0, None, None, N0, None, N0, N1, None, N1], ["Disiapkan oleh", "Diperiksa oleh"])
    widths(pl, [22, 34, 10, 7, 8, 7, 12, 13, 13])
    doc(sj, ["No", "Nama barang", "SKU", "Qty", "Satuan", "Koli", "Keterangan"], ["A", "B", "C", "D", "E", "F", "H"], [N0, None, None, N0, None, N0, None], ["Pengirim", "Pengemudi", "Penerima"])
    widths(sj, [22, 34, 10, 7, 8, 7, 16])
    return wb
