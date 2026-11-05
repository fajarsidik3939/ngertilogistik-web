import datetime as dt, random
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.chart import BarChart, LineChart, PieChart, DoughnutChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule

NAVY, NAVY2, ACC, MUTE = "0B1220", "1F3A6B", "FFC400", "6B7891"
F = "Arial"
thin = Side(style="thin", color="D5DCE6")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
INFILL = PatternFill("solid", fgColor="FFF6CC")
HFILL = PatternFill("solid", fgColor="14203A")
KFILL = PatternFill("solid", fgColor="F3F6FB")
D = 'dd/mm/yyyy'; RP = '"Rp"#,##0;-"Rp"#,##0;"-"'; N0 = '#,##0;-#,##0;"-"'; N1 = '#,##0.0'; N2 = '#,##0.00'; P1 = '0.0%'
random.seed(7)
BASE = dt.date(2026, 10, 1)
def day(n): return BASE + dt.timedelta(days=n)

def wb_new():
    wb = Workbook(); wb.remove(wb.active); return wb

def sheet(wb, name, title, note=None, tab=None):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    ws["A1"] = title; ws["A1"].font = Font(name=F, size=16, bold=True, color=NAVY)
    ws.row_dimensions[1].height = 26
    ws["A2"] = note or "Sel berwarna kuning dengan teks biru adalah input, silakan diisi. Sel lain berisi rumus. Data bawaan adalah CONTOH, bukan data nyata."
    ws["A2"].font = Font(name=F, size=9, italic=True, color=MUTE)
    ws["A3"] = "Template gratis dari Ngerti Logistik · ngertilogistik.web.id"
    ws["A3"].font = Font(name=F, size=9, color=MUTE)
    if tab: ws.sheet_properties.tabColor = tab
    return ws

def widths(ws, ws_w):
    for i, w in enumerate(ws_w, 1): ws.column_dimensions[L(i)].width = w

def header(ws, r, c, names):
    for j, n in enumerate(names):
        x = ws.cell(r, c + j, n)
        x.font = Font(name=F, bold=True, color="FFFFFF", size=10); x.fill = HFILL
        x.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True); x.border = BOX
    ws.row_dimensions[r].height = 30

def put(ws, r, c, v, fmt=None, inp=False, bold=False, color=None, align=None, size=10):
    x = ws.cell(r, c, v)
    x.font = Font(name=F, size=size, bold=bold, color=("0000FF" if inp else (color or "000000")))
    if inp: x.fill = INFILL
    if fmt: x.number_format = fmt
    x.border = BOX
    if align: x.alignment = Alignment(horizontal=align, vertical="center", wrap_text=True)
    return x

def table(ws, r, c, names, rows, fmts=None, inputs=None, blank=0):
    """rows: list of lists; a str starting with '=' is formula. '{r}' replaced with row number.
    inputs: set of column offsets that are input. blank: extra empty rows (formulas repeated, inputs empty)."""
    header(ws, r, c, names)
    fmts = fmts or [None] * len(names); inputs = inputs or set()
    allrows = rows + [[None if j in inputs else rows[-1][j] for j in range(len(names))] for _ in range(blank)]
    for i, row in enumerate(allrows):
        rr = r + 1 + i
        for j, v in enumerate(row):
            if isinstance(v, str) and "{r}" in v: v = v.replace("{r}", str(rr))
            put(ws, rr, c + j, v, fmts[j], inp=(j in inputs))
    return r + 1, r + len(allrows)

def kpi(ws, r, c, label, formula, fmt=None, w=2):
    ws.merge_cells(start_row=r, start_column=c, end_row=r, end_column=c + w - 1)
    ws.merge_cells(start_row=r + 1, start_column=c, end_row=r + 1, end_column=c + w - 1)
    a = ws.cell(r, c, label); a.font = Font(name=F, size=9, bold=True, color=MUTE); a.fill = KFILL
    b = ws.cell(r + 1, c, formula); b.font = Font(name=F, size=20, bold=True, color=NAVY); b.fill = KFILL
    b.alignment = Alignment(horizontal="left", vertical="center")
    if fmt: b.number_format = fmt
    ws.row_dimensions[r + 1].height = 34

def section(ws, r, text):
    x = ws.cell(r, 1, text); x.font = Font(name=F, size=12, bold=True, color=NAVY2)

def dv_list(ws, rng, items):
    d = DataValidation(type="list", formula1='"' + ",".join(items) + '"', allow_blank=True)
    ws.add_data_validation(d); d.add(rng)

def status_color(ws, rng, word, color):
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'ISNUMBER(SEARCH("{word}",{rng.split(":")[0]}))'],
        fill=PatternFill("solid", fgColor=color)))

def _style(ch, title, h=7.5, w=15):
    ch.title = title; ch.height = h; ch.width = w; ch.legend.position = "b"
    return ch

def bar(ws, anchor, title, cats, data_refs, titles=True, h=7.5, w=15, horizontal=False, colors=(NAVY2, ACC, "0E9F6E", "E0453A")):
    ch = BarChart(); ch.type = "bar" if horizontal else "col"; _style(ch, title, h, w)
    for i, ref in enumerate(data_refs):
        ch.add_data(ref, titles_from_data=titles)
    ch.set_categories(cats)
    for i, s in enumerate(ch.series): s.graphicalProperties.solidFill = colors[i % len(colors)]; s.graphicalProperties.line.noFill = True
    if len(data_refs) == 1 and not titles: ch.legend = None
    ws.add_chart(ch, anchor); return ch

def line(ws, anchor, title, cats, data_refs, h=7.5, w=15, colors=(NAVY2, ACC, "0E9F6E")):
    ch = LineChart(); _style(ch, title, h, w)
    for ref in data_refs: ch.add_data(ref, titles_from_data=True)
    ch.set_categories(cats)
    for i, s in enumerate(ch.series): s.graphicalProperties.line.solidFill = colors[i % len(colors)]; s.graphicalProperties.line.width = 28000; s.smooth = False
    ws.add_chart(ch, anchor); return ch

def pie(ws, anchor, title, cats, ref, h=7.5, w=11, donut=True):
    ch = DoughnutChart() if donut else PieChart(); _style(ch, title, h, w)
    ch.add_data(ref, titles_from_data=True); ch.set_categories(cats)
    ch.dataLabels = DataLabelList(); ch.dataLabels.showPercent = True; ch.dataLabels.showVal = False; ch.dataLabels.showCatName = False; ch.dataLabels.showSerName = False; ch.dataLabels.showLegendKey = False
    ws.add_chart(ch, anchor); return ch

def note(ws, r, c, text, size=10, bold=False, color="000000"):
    x = ws.cell(r, c, text); x.font = Font(name=F, size=size, bold=bold, color=color)
    x.alignment = Alignment(wrap_text=True, vertical="top"); return x
