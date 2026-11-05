import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import inv, gdg, krm
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
J = {"kartu-stok-dashboard": inv.kartu_stok, "reorder-point-safety-stock": inv.rop, "analisis-abc": inv.abc, "aging-stok-dead-stock": inv.aging,
     "inventory-turnover": inv.turnover, "formulir-stock-opname": inv.opname, "cycle-count": gdg.cycle_count, "log-penerimaan-barang": gdg.receiving,
     "picking-list": gdg.picking, "utilisasi-rak-gudang": gdg.rak, "dashboard-kpi-gudang": gdg.kpi_gudang, "checklist-5r-k3": gdg.checklist_5r,
     "tracker-pengiriman": krm.tracker, "kalkulator-berat-volume": krm.berat_volume, "jadwal-armada-ritase": krm.armada,
     "perbandingan-tarif-ekspedisi": krm.tarif, "tracker-retur": krm.retur, "packing-list-surat-jalan": krm.surat_jalan}
for k, f in J.items():
    wb = f(); wb.properties.creator = "Ngerti Logistik"; wb.properties.title = k; wb.active = 0
    wb.save(os.path.join(OUT, k + ".xlsx")); print("ok", k)
