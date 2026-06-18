# A/R Cleared Items Report Design

## Scope Note
Educational report design reconstructed from documented academic project evidence, not exported from a production SAP system.

## Business Use Case
Accounting users need a focused view of customer invoices that have been cleared so they can validate incoming payment activity and customer account status.

## Primary Tables
| Table | Purpose | Join Logic |
|---|---|---|
| `BSAD` | A/R cleared items | Main transaction table filtered by company code, customer, posting date, and clearing date |
| `KNA1` | Customer master | Join `BSAD-KUNNR` to `KNA1-KUNNR` for customer name and country |
| `BKPF` | Accounting document header | Optional join on company code, document number, and fiscal year for header-level posting context |

## Selection-Screen Logic
- Company code as required parameter.
- Customer account range as optional select-option.
- Posting date range as optional select-option.
- Clearing date range as optional select-option.
- Fiscal year as optional parameter.

## Output Fields
| Field | Business Meaning |
|---|---|
| Company code | Legal entity for accounting review |
| Customer number | A/R subledger account |
| Customer name | Readable customer context |
| Document number | Accounting document reference |
| Fiscal year | Accounting year |
| Posting date | Date posted to accounting |
| Clearing document | Payment or clearing reference |
| Clearing date | Date item was cleared |
| Debit/credit indicator | Direction of accounting entry |
| Amount | Cleared item value |
| Currency | Transaction currency |

## Controls Supported
- Cleared item visibility.
- Customer payment follow-up.
- Reconciliation between customer master and cleared item activity.
