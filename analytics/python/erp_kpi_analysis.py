"""Generate SAP-style ERP KPI outputs from synthetic CSV data.

The input files are synthetic training assets for portfolio demonstration.
They are not SAP exports and do not contain company or client data.
"""
from pathlib import Path

try:
    import pandas as pd
except ModuleNotFoundError:  # Allows portfolio outputs in constrained environments without installed dependencies.
    pd = None
import csv
from collections import defaultdict

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "analytics" / "data" / "synthetic"
OUTPUT_DIR = ROOT_DIR / "analytics" / "outputs"


def read_csv(file_name: str) -> pd.DataFrame:
    """Read one synthetic CSV file from the analytics data folder."""
    return pd.read_csv(DATA_DIR / file_name)


def build_fi_balances(fi_documents: pd.DataFrame) -> pd.DataFrame:
    """Summarize open and cleared A/R and A/P balances for finance review."""
    return (
        fi_documents.groupby(["company_code", "account_type", "status"], as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "balance_amount"})
    )


def build_three_way_match_exceptions(
    purchase_orders: pd.DataFrame,
    goods_receipts: pd.DataFrame,
    vendor_invoices: pd.DataFrame,
) -> pd.DataFrame:
    """Compare PO, GR, and invoice quantities/amounts to identify procurement exceptions."""
    merged = purchase_orders.merge(goods_receipts, on="po_id", how="left").merge(
        vendor_invoices, on="po_id", how="left", suffixes=("_gr", "_invoice")
    )
    merged["expected_invoice_amount"] = merged["po_quantity"] * merged["po_unit_price"]
    merged["quantity_exception"] = merged["po_quantity"] != merged["received_quantity"]
    merged["invoice_quantity_exception"] = merged["po_quantity"] != merged["invoiced_quantity"]
    merged["invoice_amount_exception"] = merged["expected_invoice_amount"] != merged["invoice_amount"]

    return merged.loc[
        merged[
            ["quantity_exception", "invoice_quantity_exception", "invoice_amount_exception"]
        ].any(axis=1),
        [
            "po_id",
            "vendor_id",
            "material_id",
            "po_quantity",
            "received_quantity",
            "invoiced_quantity",
            "expected_invoice_amount",
            "invoice_amount",
            "quantity_exception",
            "invoice_quantity_exception",
            "invoice_amount_exception",
        ],
    ]


def build_production_variance(production_orders: pd.DataFrame) -> pd.DataFrame:
    """Calculate planned vs actual production output variance for PP review."""
    output = production_orders.copy()
    output["quantity_variance"] = output["actual_quantity"] - output["planned_quantity"]
    output["completion_rate"] = (output["actual_quantity"] / output["planned_quantity"]).round(4)
    return output[
        [
            "production_order_id",
            "plant",
            "material_id",
            "planned_quantity",
            "actual_quantity",
            "quantity_variance",
            "completion_rate",
            "status",
        ]
    ]


def build_cost_center_summary(cost_center_actuals: pd.DataFrame) -> pd.DataFrame:
    """Summarize CO actual expenses by cost center for management review."""
    return (
        cost_center_actuals.groupby(["controlling_area", "cost_center"], as_index=False)[
            "actual_amount"
        ]
        .sum()
        .rename(columns={"actual_amount": "total_actual_expense"})
    )


def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    with (DATA_DIR / file_name).open(newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def write_rows(file_name: str, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    fieldnames = sorted({field for row in rows for field in row.keys()})
    with (OUTPUT_DIR / file_name).open("w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main_without_pandas() -> None:
    """Dependency-light fallback for constrained review environments.

    The intended local workflow uses pandas. This fallback keeps the repository
    runnable when package installation is blocked by the environment.
    """
    fi_totals: dict[tuple[str, str, str], float] = defaultdict(float)
    for row in read_csv_rows("fi_documents.csv"):
        fi_totals[(row["company_code"], row["account_type"], row["status"])] += float(row["amount"])

    kpi_rows: list[dict[str, object]] = [
        {
            "company_code": company_code,
            "account_type": account_type,
            "status": status,
            "balance_amount": amount,
            "kpi_area": "FI_AR_AP_BALANCE",
        }
        for (company_code, account_type, status), amount in fi_totals.items()
    ]

    for row in read_csv_rows("production_orders.csv"):
        target_qty = float(row["planned_quantity"])
        actual_qty = float(row["actual_quantity"])
        kpi_rows.append({
            "production_order_id": row["production_order_id"],
            "plant": row["plant"],
            "material_id": row["material_id"],
            "planned_quantity": row["planned_quantity"],
            "actual_quantity": row["actual_quantity"],
            "quantity_variance": actual_qty - target_qty,
            "completion_rate": round(actual_qty / target_qty, 4),
            "status": row["status"],
            "kpi_area": "PP_PRODUCTION_VARIANCE",
        })

    cc_totals: dict[tuple[str, str], float] = defaultdict(float)
    for row in read_csv_rows("cost_center_actuals.csv"):
        cc_totals[(row["controlling_area"], row["cost_center"])] += float(row["actual_amount"])
    for (controlling_area, cost_center), total in cc_totals.items():
        kpi_rows.append({
            "controlling_area": controlling_area,
            "cost_center": cost_center,
            "total_actual_expense": total,
            "kpi_area": "CO_COST_CENTER_ACTUALS",
        })

    pos = {row["po_id"]: row for row in read_csv_rows("purchase_orders.csv")}
    grs = {row["po_id"]: row for row in read_csv_rows("goods_receipts.csv")}
    invs = {row["po_id"]: row for row in read_csv_rows("vendor_invoices.csv")}
    exception_rows = []
    for po_id, po in pos.items():
        gr = grs.get(po_id, {})
        inv = invs.get(po_id, {})
        expected = float(po["po_quantity"]) * float(po["po_unit_price"])
        quantity_exception = po["po_quantity"] != gr.get("received_quantity", "")
        invoice_quantity_exception = po["po_quantity"] != inv.get("invoiced_quantity", "")
        invoice_amount_exception = expected != float(inv.get("invoice_amount", 0))
        if quantity_exception or invoice_quantity_exception or invoice_amount_exception:
            exception_rows.append({
                "po_id": po_id,
                "vendor_id": po["vendor_id"],
                "material_id": po["material_id"],
                "po_quantity": po["po_quantity"],
                "received_quantity": gr.get("received_quantity", ""),
                "invoiced_quantity": inv.get("invoiced_quantity", ""),
                "expected_invoice_amount": expected,
                "invoice_amount": inv.get("invoice_amount", ""),
                "quantity_exception": quantity_exception,
                "invoice_quantity_exception": invoice_quantity_exception,
                "invoice_amount_exception": invoice_amount_exception,
            })

    write_rows("kpi_summary.csv", kpi_rows)
    write_rows("exception_report.csv", exception_rows)
    print(f"Wrote {OUTPUT_DIR / 'kpi_summary.csv'}")
    print(f"Wrote {OUTPUT_DIR / 'exception_report.csv'}")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if pd is None:
        main_without_pandas()
        return

    fi_documents = read_csv("fi_documents.csv")
    purchase_orders = read_csv("purchase_orders.csv")
    goods_receipts = read_csv("goods_receipts.csv")
    vendor_invoices = read_csv("vendor_invoices.csv")
    production_orders = read_csv("production_orders.csv")
    cost_center_actuals = read_csv("cost_center_actuals.csv")

    fi_balances = build_fi_balances(fi_documents)
    three_way_exceptions = build_three_way_match_exceptions(
        purchase_orders, goods_receipts, vendor_invoices
    )
    production_variance = build_production_variance(production_orders)
    cost_center_summary = build_cost_center_summary(cost_center_actuals)

    kpi_summary = pd.concat(
        [
            fi_balances.assign(kpi_area="FI_AR_AP_BALANCE"),
            production_variance.assign(kpi_area="PP_PRODUCTION_VARIANCE"),
            cost_center_summary.assign(kpi_area="CO_COST_CENTER_ACTUALS"),
        ],
        ignore_index=True,
        sort=False,
    )

    kpi_summary.to_csv(OUTPUT_DIR / "kpi_summary.csv", index=False)
    three_way_exceptions.to_csv(OUTPUT_DIR / "exception_report.csv", index=False)

    print(f"Wrote {OUTPUT_DIR / 'kpi_summary.csv'}")
    print(f"Wrote {OUTPUT_DIR / 'exception_report.csv'}")


if __name__ == "__main__":
    main()
