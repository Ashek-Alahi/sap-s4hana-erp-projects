# SAP FI/CO Academic Training-System Project

## Portfolio Summary
This FI/CO project is a core portfolio artifact showing accounting process execution in an SAP S/4HANA academic training system. It demonstrates G/L, A/P, A/R, payments, cost centers, assessment cycles, and integration awareness across FI-MM and FI-SD.

## Business Problem
Finance teams need accurate transaction posting, payment clearing, customer balance visibility, and cost allocation so financial statements and management reports reflect business activity correctly.

## Process Scope
- Review enterprise structure such as company code and controlling area assignment.
- Create and review G/L account master data.
- Post G/L documents.
- Maintain vendor business partner data.
- Enter vendor invoice and execute outgoing payment.
- Maintain customer master data.
- Create customer invoice and post incoming payment.
- Display vendor and customer line items and balances.
- Create cost centers and post FI actual cost documents.
- Execute assessment cycles for cost allocation.
- Review FI-MM and FI-SD integration table relationships.

## SAP Configuration / Execution Evidence
- SAP S/4HANA academic training-system exercises using SAP Fiori and SAP GUI concepts.
- Company codes and controlling areas documented in the evidence PDFs.
- Activities documented for G/L, A/P, A/R, payments, cost centers, and assessment cycles.
- Integration tables discussed include `BKPF`, `BSEG`, `KNA1`, `LFA1`, `BSAD`, `BSID`, `BSAK`, `BSIK`, `MKPF`, `MSEG`, `RBKP`, `RSEG`, `COEP`, and `CSKS`.
- PDF evidence documents the completed academic FI and FI/CO exercises.

## Business Value
FI/CO matters because it converts operational activity into accounting records and management reporting. Vendor invoices affect liabilities and cash, customer invoices affect receivables and revenue visibility, and cost center postings help managers understand where expenses are being consumed.

## KPIs / Controls
- Open A/R balance.
- Open A/P balance.
- Vendor balance and clearing status.
- Customer balance and clearing status.
- Cost center actual expenses.
- Assessment cycle allocation amount.
- Posting period and document type control.
- FI-MM and FI-SD reconciliation checks.

## Interview Defense
- **Q: What is the difference between G/L, A/P, and A/R?** A: G/L is the central ledger, A/P tracks vendor obligations, and A/R tracks customer receivables; subledger activity reconciles back to G/L accounts.
- **Q: Why do payments matter after invoice posting?** A: Payment posting clears open items and changes the financial position from payable or receivable exposure to cash movement.
- **Q: What did the cost center work prove?** A: It showed how expenses can be assigned and allocated for management accounting, not just external financial reporting.
- **Q: How does FI integrate with MM?** A: Goods receipts and invoice verification create accounting impacts through inventory, GR/IR, and vendor liability accounts.
- **Q: How does FI integrate with SD?** A: Billing and incoming payment activity affect customer receivables, revenue-related accounts, and cleared item reporting.

## Limitations
- Academic training-system scenario.
- Not production implementation.
- No company-sensitive data.
- Synthetic analytics data is used only in the separate analytics extension.
- PDF evidence may contain academic identifiers from the original coursework.

## Evidence Files
- `FI Final project.pdf`
- `FICO Final project.pdf`
