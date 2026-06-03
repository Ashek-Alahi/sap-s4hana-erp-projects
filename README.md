# SAP ERP Projects Portfolio

## Overview

This repository contains a collection of SAP ERP projects completed during my Master's degree in Enterprise Resource Planning (ERP).

The projects demonstrate hands-on experience in SAP configuration, customization, master data management, financial accounting, procurement processes, controlling, production planning, ABAP development, and human resource management.

The work was completed using SAP training systems with access to IMG/SPRO customization and business process execution.

---

## Modules

1. SAP Financial Accounting & Controlling (FI/CO)
2. SAP Materials Management (MM)
3. SAP Production Planning (PP)
4. SAP ABAP
5. SAP Human Capital Management (HCM)

---

# 1. SAP Financial Accounting (FI)

## Project Objective

Implementation and configuration of core Financial Accounting functions including enterprise structure setup, document processing, accounts payable, accounts receivable, and business partner management.

## Activities Performed

| No | Activity |
|----|-----------|
| 1 | Copy Company Code |
| 2 | Edit Company Code Information |
| 3 | Assign Company Code to Controlling Area |
| 4 | Assign Posting Period Variant |
| 5 | Display Document Number Ranges |
| 6 | Post G/L Account Documents |
| 7 | Create Vendor Master Record |
| 8 | Create Vendor Invoice |
| 9 | Post Outgoing Payment |
| 10 | Display Vendor Balances |
| 11 | Maintain Customer Master |
| 12 | Create Customer Invoice |
| 13 | Post Incoming Payment |
| 14 | Display Customer Balances |

## SAP Areas Covered

- Enterprise Structure
- Financial Accounting
- General Ledger Accounting
- Accounts Payable
- Accounts Receivable
- Business Partner Management
- Document Posting
- Payment Processing

---

# 2. SAP Financial Accounting & Controlling (FI/CO)

## Project Objective

Advanced Financial Accounting and Controlling processes including G/L account management, cost center accounting, assessment cycles, FI-CO integration, and ERP analytics.

## FI Activities Performed

| No | Activity |
|----|-----------|
| 1 | Create G/L Accounts |
| 2 | Create G/L Documents |
| 3 | Maintain Vendor Business Partner |
| 4 | Create Accounts Payable Documents |
| 5 | Execute Outgoing Payments |
| 6 | Display Vendor Line Items |
| 7 | Display Customer Master Data |

## CO Activities Performed

| No | Activity |
|----|-----------|
| 1 | Create Cost Centers |
| 2 | Create Assessment Cycles |
| 3 | Post FI Actual Cost Documents |
| 4 | Execute Assessment Cycles |

## Integration Analysis

### FI - SD Integration

- BKPF
- BSEG
- VBRK
- VBRP
- KNKA
- KNA1
- COEP
- BSAD
- BSID

### FI - MM Integration

- BKPF
- BSEG
- MKPF
- MSEG
- EKKN
- EKPO
- RBKP
- RSEG
- COEP
- GLPCA

## Additional Topics

- SAP Fiori Interface Customization
- ERP Web Interface Configuration
- Artificial Intelligence in ERP Systems

## SAP Areas Covered

- Financial Accounting
- Controlling
- Cost Center Accounting
- Assessment Cycles
- Vendor Accounting
- Customer Accounting
- FI-MM Integration
- FI-SD Integration
- SAP Fiori

---

# 3. SAP Materials Management (MM)

## Project Objective

Execution of a complete Procure-to-Pay (P2P) cycle including vendor management, procurement, inventory management, invoice verification, and payment processing.

## Business Scenario

Client: Global Bike Inc.

Material: Chain Lock Security Pro 157

Material Number: CHSP1157

## Procurement Cycle

| No | Activity |
|----|-----------|
| 1 | Create Vendor |
| 2 | Create Material Master |
| 3 | Create Purchase Requisition |
| 4 | Create Request for Quotation (RFQ) |
| 5 | Create Purchase Order |
| 6 | Post Goods Receipt |
| 7 | Enter Vendor Invoice |
| 8 | Create Purchasing Info Record |
| 9 | Execute Vendor Payment |

## SAP Transactions Used

| Activity | Transaction |
|-----------|-------------|
| Vendor Creation | XK01 |
| Material Creation | MMH1 |
| Purchase Requisition | ME51N |
| RFQ Creation | ME41 |
| Purchase Order | ME21N |
| Goods Receipt | MIGO |
| Invoice Verification | MIRO |
| Info Record | ME11 |
| Vendor Payment | F-53 |

## SAP Areas Covered

- Vendor Master Data
- Material Master Data
- Purchasing
- RFQ Management
- Source Determination
- Purchase Orders
- Inventory Management
- Goods Receipt
- Invoice Verification
- Vendor Payments
- Procure-to-Pay Process

---
# 4. SAP Production Planning (PP)

## Project Objective

Implementation of core Production Planning processes in SAP ERP, including material planning, bill of materials management, work center configuration, routing setup, production order processing, and manufacturing execution.

## Business Scenario

The project simulates a manufacturing environment where finished products are planned, produced, and monitored using SAP Production Planning.

The objective is to manage the complete production cycle from demand planning through production execution and goods receipt.

## Activities Performed

| No | Activity                                            |
| -- | --------------------------------------------------- |
| 1  | Define Production Planning Organizational Structure |
| 2  | Create Material Master for Finished Goods           |
| 3  | Create Material Master for Raw Materials            |
| 4  | Create Bill of Materials (BOM)                      |
| 5  | Create Work Centers                                 |
| 6  | Create Routings                                     |
| 7  | Create Production Version                           |
| 8  | Execute Material Requirements Planning (MRP)        |
| 9  | Convert Planned Orders                              |
| 10 | Create Production Orders                            |
| 11 | Release Production Orders                           |
| 12 | Confirm Production Operations                       |
| 13 | Post Goods Receipt for Finished Products            |
| 14 | Analyze Production Planning Results                 |

## SAP Transactions Used

| Activity           | Transaction |
| ------------------ | ----------- |
| Material Master    | MM01        |
| Bill of Materials  | CS01        |
| Work Center        | CR01        |
| Routing            | CA01        |
| Production Version | C223        |
| MRP Run            | MD01 / MD02 |
| Planned Order      | MD11        |
| Production Order   | CO01        |
| Order Confirmation | CO11N       |
| Goods Receipt      | MIGO        |

## Production Planning Process

1. Create Material Master Records
2. Create Bill of Materials (BOM)
3. Create Work Centers
4. Create Routings
5. Maintain Production Versions
6. Run Material Requirements Planning (MRP)
7. Generate Planned Orders
8. Convert Planned Orders into Production Orders
9. Release Production Orders
10. Confirm Production Activities
11. Receive Finished Goods into Inventory

## SAP Areas Covered

* Production Planning (PP)
* Material Requirements Planning (MRP)
* Bill of Materials (BOM)
* Work Centers
* Routings
* Production Orders
* Shop Floor Control
* Capacity Planning
* Manufacturing Execution
* Inventory Integration

## Learning Outcomes

* Understanding end-to-end manufacturing processes in SAP.
* Managing production master data.
* Executing MRP runs and production planning activities.
* Creating and processing production orders.
* Integrating production with inventory management.
* Monitoring production execution and confirmations.



# 5. SAP ABAP

## Project Objective

ABAP development exercises including report development, data retrieval, screen programming, and SAP application development.

## Activities Performed

| No | Activity |
|----|-----------|
| 1 | ABAP Programming Fundamentals |
| 2 | Internal Tables |
| 3 | Data Dictionary Objects |
| 4 | Selection Screens |
| 5 | Reports |
| 6 | Database Access |
| 7 | ALV Reporting |
| 8 | Modularization |
| 9 | SAP Development Tools |

---

# 6. SAP Human Capital Management (HCM)

## Project Objective

Configuration and execution of Human Resource Management processes within SAP ERP.

## Activities Performed

| No | Activity |
|----|-----------|
| 1 | Organizational Management |
| 2 | Personnel Administration |
| 3 | Employee Master Data |
| 4 | Recruitment Process |
| 5 | Payroll Concepts |
| 6 | Time Management |
| 7 | HR Reporting |

---

# Technical Skills Demonstrated

- SAP ERP
- SAP S/4HANA
- SAP FI
- SAP CO
- SAP MM
- SAP PP
- SAP HCM
- SAP ABAP
- SAP Fiori
- SAP IMG
- SAP SPRO
- Enterprise Structure Configuration
- Master Data Management
- Procure-to-Pay (P2P)
- Accounts Payable
- Accounts Receivable
- Cost Center Accounting
- Financial Reporting
- ERP Process Design

---

# Repository Structure

```text
SAP-ERP-Projects
│
├── SAP_FI
├── SAP_FI_CO
├── SAP_MM
├── SAP_ABAP
├── SAP_HCM
│
└── README.md
```

---

## Author

**Alahi Ashek**

Master's Degree in ERP  
Accounting & ERP Professional  
SAP FICO |MM  | PP | HCM | ABAP 
Interested in SAP S/4HANA, ERP Consulting, Business Analytics, and Financial Systems

GitHub: [Ashek-Alahi GitHub Profile](https://github.com/Ashek-Alahi?utm_source=chatgpt.com)
