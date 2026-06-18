# SAP MM Academic Procure-to-Pay Project

## Portfolio Summary
This MM project demonstrates procure-to-pay execution in an SAP S/4HANA academic training system, including sourcing, purchasing, goods receipt, invoice verification, payment clearing, and procurement control analysis.

## Business Problem
Procurement teams need controlled purchasing from vendor selection through payment. Weak controls can create duplicate purchases, inventory discrepancies, invoice mismatches, and inaccurate vendor liabilities.

## Process Scope
- Create vendor master data.
- Create material master data for Chain Lock Security Pro 157 (`CHSP1157`).
- Create purchase requisition.
- Create RFQs for vendor comparison.
- Compare quotations and select vendor.
- Create purchase order.
- Post goods receipt.
- Enter vendor invoice with invoice verification.
- Maintain purchasing info record.
- Execute vendor payment and confirm clearing.
- Analyze duplicate PO inventory discrepancy as a control-risk finding.

## SAP Configuration / Execution Evidence
- Transactions documented include `XK01`, `MMH1`, `ME51N`, `ME41`, `ME49`, `ME21N`, `MIGO`, `MIRO`, `ME11`, and `F-53`.
- Process evidence includes vendor creation, material creation, RFQ, quotation comparison, PO, goods receipt, vendor invoice, info record, and payment clearing.
- The duplicate PO inventory discrepancy is documented as a procurement and inventory control risk.
- Relevant SAP tables for analytics discussion include `EKKO`, `EKPO`, `MKPF`, `MSEG`, `RBKP`, and `RSEG`.

## Business Value
MM matters because it protects company cash and inventory. A controlled P2P process helps ensure the company buys from the right vendor, receives the right quantity, pays the right invoice, and identifies exceptions before they affect financial statements or operations.

## KPIs / Controls
- PO-to-GR cycle monitoring.
- Three-way match exception review.
- Vendor price variance.
- Duplicate PO risk.
- GR/IR reconciliation.
- Vendor comparison documentation.
- Payment clearing status.

## Limitations
- Academic training-system scenario.
- Not production implementation.
- No company-sensitive data.
- Synthetic analytics data is used only in the separate analytics extension.
- PDF evidence may contain academic identifiers from the original coursework.

## Evidence Files
- `Final project MM.pdf`
