# Customer Detail Report Design

## Scope Note
Educational report design reconstructed from documented academic project evidence, not exported from a production SAP system.

## Business Use Case
Accounting users need a drilldown-style customer view that shows customer identity, accounting line items, G/L accounts, and clearing references in one output.

## Primary Tables
| Table | Purpose | Join Logic |
|---|---|---|
| `KNA1` | Customer master | Main customer context table |
| `BSAD` | Cleared A/R line items | Join `KNA1-KUNNR` to `BSAD-KUNNR` |
| `BSEG` | Accounting document segment | Optional join by company code, document number, and fiscal year for G/L account and posting key detail |

## Selection-Screen Logic
- Company code as required parameter.
- Single customer or customer range.
- Posting date range.
- Clearing document as optional filter.
- Include debit/credit indicator as optional report filter.

## Output Fields
| Field | Business Meaning |
|---|---|
| Customer number | Customer account identifier |
| Customer name | Customer master description |
| City and country | Customer location context |
| Company code | Accounting entity |
| Document number | Accounting document |
| G/L account | Reconciliation or related ledger account |
| Posting key | Accounting line-item behavior |
| Debit/credit indicator | Debit or credit sign logic |
| Clearing document | Matched payment or clearing document |
| Amount | Transaction value |

## Controls Supported
- Customer drilldown.
- Cleared debit and credit pair review.
- Faster review of customer account history for accounting support.
