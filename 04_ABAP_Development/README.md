# SAP ABAP Academic Reporting Design Project

## Portfolio Summary
This ABAP project presents academic reporting designs for FI-focused reports. It shows how SAP tables, selection screens, joins, and ALV-style output can support accounting users without claiming full exported production source code.

## Business Problem
Accounting users often need focused reports that filter by company code, customer, vendor, clearing status, and posting details. Standard reports may require multiple screens or manual reconciliation, so report design skills are valuable for ERP reporting support.

## Process Scope
- Define A/R cleared items report requirements.
- Define customer detail report requirements.
- Define A/P cleared items report requirements.
- Map business questions to SAP tables and joins.
- Define selection-screen filters.
- Define output fields for accounting review.
- Document ALV-style reporting behavior and drilldown use cases.

## SAP Configuration / Execution Evidence
- Report programs are documented in the academic PDF as project outputs.
- Report designs are documented in [`report_design/`](report_design/).
- Tables documented include `KNA1`, `BSAD`, `LFA1`, and `BSAK`.
- Educational sample code, if reviewed, is labeled as reconstructed design material rather than exported source from a production SAP system.

## Business Value
ABAP reporting matters because ERP users need reliable visibility into cleared items, customer activity, vendor payments, and accounting exceptions. A strong report design connects business filters to the right SAP tables and output fields.

## KPIs / Controls
- Report filter coverage.
- Cleared item visibility.
- Customer drilldown.
- Vendor drilldown.
- Field-level reconciliation usability.
- Selection-screen completeness.

## Limitations
- Academic training-system scenario.
- Not production implementation.
- No company-sensitive data.
- Synthetic analytics data is used only in the separate analytics extension.
- PDF evidence may contain academic identifiers from the original coursework.
- Public repository does not claim complete exported SAP source code.

## Evidence Files
- `ABAP Final project pdf.pdf`
- [`report_design/ar_cleared_items_report_design.md`](report_design/ar_cleared_items_report_design.md)
- [`report_design/customer_detail_report_design.md`](report_design/customer_detail_report_design.md)
- [`report_design/ap_cleared_items_report_design.md`](report_design/ap_cleared_items_report_design.md)
