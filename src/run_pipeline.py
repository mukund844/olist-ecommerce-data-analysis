from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from data_loader import load_olist_data
from cleaning import clean_tables
from features import build_master_table, get_delivered
from rfm import build_rfm

def main():
    raw = load_olist_data(ROOT / "data" / "raw")
    clean = clean_tables(raw)
    master = build_master_table(clean)
    delivered = get_delivered(master)
    rfm = build_rfm(delivered)

    out = ROOT / "data" / "processed"
    out.mkdir(parents=True, exist_ok=True)

    # Useful derived outputs; raw data remains untouched.
    master.to_csv(out / "olist_master_table.csv", index=False)
    delivered.to_csv(out / "olist_delivered_orders.csv", index=False)
    rfm.to_csv(out / "olist_rfm_segments.csv")

    print(f"Master table: {master.shape[0]:,} rows x {master.shape[1]} columns")
    print(f"Delivered rows: {delivered.shape[0]:,}")
    print(f"RFM customers: {rfm.shape[0]:,}")
    print(f"Saved outputs to: {out}")

if __name__ == "__main__":
    main()
