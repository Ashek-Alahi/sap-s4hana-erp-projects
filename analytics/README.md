# SAP-Style Synthetic ERP Analytics Extension

## Purpose
This runnable extension translates the portfolio's SAP process knowledge into simple analytics outputs. It uses synthetic SAP-style CSV files to demonstrate FI, MM, PP, and CO KPI analysis without claiming any real SAP extract.

## Scope Note
The data in `analytics/data/synthetic/` is synthetic SAP-style sample data. It is not real SAP data, not a client extract, and not connected to any production SAP system.

## How to Run
From the repository root:

```bash
pip install -r requirements.txt
python analytics/python/erp_kpi_analysis.py
pytest
```


## Quality Checks

The analytics functions are covered by lightweight regression tests in `tests/test_erp_kpi_analysis.py`. These tests verify FI balance aggregation, MM exception detection, PP variance calculation, and CO cost center summarization so reviewers can confirm the logic is reproducible.

## Business Questions Answered
| Area | Question |
|---|---|
| FI | What are the A/R and A/P balances by open and cleared status? |
| MM | Which purchase orders have three-way match exceptions between PO, GR, and invoice? |
| PP | Which production orders have planned vs actual quantity variance? |
| CO | Which cost centers have actual expense totals for management review? |

## Output Files Generated
| File | Description |
|---|---|
| `analytics/outputs/kpi_summary.csv` | Combined FI balance, PP variance, and CO actual expense KPI summary |
| `analytics/outputs/exception_report.csv` | MM three-way match exception report |

## Data Model
| File | Business Meaning |
|---|---|
| `customers.csv` | Synthetic customer master data |
| `vendors.csv` | Synthetic vendor master data |
| `fi_documents.csv` | Synthetic A/R and A/P documents |
| `purchase_orders.csv` | Synthetic purchase order data |
| `goods_receipts.csv` | Synthetic goods receipt data |
| `vendor_invoices.csv` | Synthetic invoice verification data |
| `production_orders.csv` | Synthetic production order data |
| `cost_center_actuals.csv` | Synthetic CO actual expense data |
