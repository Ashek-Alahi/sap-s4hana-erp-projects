# SAP S/4HANA Academic ERP Portfolio

Academic SAP S/4HANA training-system portfolio demonstrating FI/CO, MM, PP, ABAP reporting design, HCM process knowledge, and a small runnable SAP-style analytics extension using clearly labeled synthetic data.

## Important Scope Note

This repo is based on academic SAP S/4HANA training-system exercises and SAP-style synthetic analytics assets. It is not a production SAP implementation.

The PDF files are retained as academic evidence. They may contain academic identifiers from the original coursework; public markdown pages avoid exposing teammate names and academic ID values.

## Target Roles

- ERP Analyst
- SAP FI/CO Junior Consultant
- SAP MM Analyst
- SAP PP Analyst
- Business / Data Analyst with ERP focus

## Portfolio Project Summary

| Area | Business process | SAP activities performed | Business value | Evidence available | Interview talking point |
|---|---|---|---|---|---|
| FI/CO | Record-to-report, accounts payable, accounts receivable, cost center accounting | Company code review, G/L postings, vendor invoice, outgoing payment, customer invoice, incoming payment, cost centers, assessment cycles, FI-MM and FI-SD table analysis | Shows how accounting transactions move through the ledger, subledgers, payments, and management accounting | [`01_Financial_Accounting_FI/`](01_Financial_Accounting_FI/) PDFs and README | Explain how an invoice, payment, and cost allocation affect financial visibility and period-end control |
| MM | Procure-to-pay | Vendor and material master, PR, RFQ, quotation comparison, PO, goods receipt, invoice verification, payment clearing | Demonstrates procurement control, three-way match thinking, inventory accuracy, and vendor balance clearing | [`02_Materials_Management_MM/`](02_Materials_Management_MM/) PDF and README | Explain the duplicate PO inventory discrepancy as a control-risk finding |
| PP | Make-to-stock production planning and execution | PIR, MRP, BOM, routing, production order, goods issue, confirmation, goods receipt | Connects demand planning, component availability, shop-floor execution, and finished goods inventory | [`03_Production_Planning_PP/`](03_Production_Planning_PP/) PDF and README | Explain how MRP converts demand into planned supply and production execution |
| ABAP | SAP financial reporting design | Report specifications for A/R cleared items, customer detail, and A/P cleared items using SAP FI master and line-item tables | Shows ERP reporting logic, selection-screen thinking, joins, and accounting use cases | [`04_ABAP_Development/`](04_ABAP_Development/) PDF, report designs, and educational example | Defend table selection, filters, output fields, and business users for each report |
| HCM | Organizational management and personnel administration | OM structure changes, qualifications, position assignment, hiring action documentation | Demonstrates supporting HR process knowledge without overstating specialization | [`05_Human_Capital_Management_HCM/`](05_Human_Capital_Management_HCM/) PDF and README | Explain HCM as a supporting academic group project and describe the process evidence |
| Analytics | SAP-style KPI analysis | Python and SQL over synthetic CSV files for FI, MM, PP, and CO KPIs | Converts ERP process knowledge into recruiter-friendly analytics outputs | [`analytics/`](analytics/) runnable extension | Explain how transactional ERP fields become KPI summaries and exception reports |

## How to Review This Repository

### Recruiter / Hiring Manager Path

1. Start with [`docs/recruiter_review_checklist.md`](docs/recruiter_review_checklist.md) for the fastest review path and honest positioning language.
2. Review [`00_Portfolio_Executive_Showcase/README.md`](00_Portfolio_Executive_Showcase/README.md) for the executive business-process narrative.
3. Use [`docs/evidence_index.md`](docs/evidence_index.md) to map each PDF to the process evidence it supports.
4. Review [`docs/portfolio_interview_handbook.md`](docs/portfolio_interview_handbook.md) for interview-ready explanations and boundaries.
5. Run the analytics extension from the repository root:

   ```bash
   pip install -r requirements.txt
   python analytics/python/erp_kpi_analysis.py
   pytest
   ```

6. Open [`analytics/outputs/kpi_summary.csv`](analytics/outputs/kpi_summary.csv) and [`analytics/outputs/exception_report.csv`](analytics/outputs/exception_report.csv) to review generated KPI outputs.

## Repository Structure

| Path | Purpose |
|---|---|
| [`01_Financial_Accounting_FI/`](01_Financial_Accounting_FI/) | FI/CO process documentation and academic PDF evidence |
| [`02_Materials_Management_MM/`](02_Materials_Management_MM/) | MM procure-to-pay process documentation and academic PDF evidence |
| [`03_Production_Planning_PP/`](03_Production_Planning_PP/) | PP make-to-stock process documentation and academic PDF evidence |
| [`04_ABAP_Development/`](04_ABAP_Development/) | ABAP reporting design documentation and academic PDF evidence |
| [`05_Human_Capital_Management_HCM/`](05_Human_Capital_Management_HCM/) | HCM supporting academic group project documentation |
| [`docs/`](docs/) | Interview handbook, KPI catalog, SAP table reference, evidence index, recruiter checklist, and recruiter summary |
| [`analytics/`](analytics/) | Runnable synthetic SAP-style analytics extension |

## Personal Contribution Statement

Personal contribution: documentation, process explanation, portfolio translation, and business analysis framing based on academic project evidence.
