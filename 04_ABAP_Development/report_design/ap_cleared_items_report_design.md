# A/P Cleared Items Report Design

## Scope Note
Educational report design reconstructed from documented academic project evidence, not exported from a production SAP system.

## Business Use Case
Accounts payable users need visibility into vendor invoices that have been cleared so they can answer vendor payment questions and validate payment status.

## Primary Tables
| Table | Purpose | Join Logic |
|---|---|---|
| `BSAK` | A/P cleared items | Main transaction table filtered by company code, vendor, posting date, and clearing date |
| `LFA1` | Vendor master | Join `BSAK-LIFNR` to `LFA1-LIFNR` for vendor name and country |
| `BKPF` | Accounting document header | Optional join on company code, document number, and fiscal year for document header context |

## Selection-Screen Logic
- Company code as required parameter.
- Vendor account range as optional select-option.
- Posting date range.
- Clearing date range.
- Fiscal year as optional parameter.

## Output Fields
| Field | Business Meaning |
|---|---|
| Company code | Legal entity for vendor payment review |
| Vendor number | A/P subledger account |
| Vendor name | Readable vendor context |
| Document number | Accounting document reference |
| Posting date | Date recorded in accounting |
| Clearing document | Payment or clearing reference |
| Clearing date | Date invoice was cleared |
| Posting key | Vendor line-item posting behavior |
| Amount | Cleared payment value |
| Currency | Transaction currency |

## Controls Supported
- Cleared vendor invoice visibility.
- Vendor payment support.
- A/P reconciliation and payment-status review.
