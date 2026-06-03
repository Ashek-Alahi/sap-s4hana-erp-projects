# SAP S/4HANA Material Management (MM) – Procure-to-Pay Implementation

## Overview
End-to-end implementation of the Procure-to-Pay (P2P) business process 
in SAP S/4HANA MM module, completed as a final project for MSc in ERP 
studies. Executed on a live SAP S/4HANA training environment using the 
Global Bike Inc. (GBI) dataset.

## Business Scenario
Procurement of **Chain Lock Security Pro 157 (CHSP1157)** for Global 
Bike Inc., involving vendor selection through competitive quotation and 
full payment cycle execution.

## Process Flow Implemented

| Step | Transaction Code | Document Created |
|------|-----------------|-----------------|
| Vendor Master Creation | XK01 | Vendor 125561, 125562 |
| Material Master Creation | MMH1 | Material CHSP1157 |
| Purchase Requisition | ME51N | PR 0010000233 |
| Request for Quotation (×2) | ME41 | RFQ 6000000534, 6000000536 |
| Price Comparison & Vendor Selection | ME49 | Rejected high-price vendor |
| Purchase Order | ME21N | PO 4500000402 |
| Goods Receipt | MIGO_GR | Material Doc 5000000691 |
| Invoice Verification | MIRO | Invoice Doc 5105600443, 5105600445 |
| Purchasing Info Record | ME11 | Info Record 5300000378 |
| Vendor Payment | F-53 / Fiori | Payment Doc 1500000444 |

## Key Concepts Demonstrated
- MM organizational structure: Client → Company Code → Plant → 
  Storage Location
- Master data management: Vendor master, Material master, 
  Purchasing Info Record
- Competitive sourcing: RFQ creation, quotation comparison, 
  vendor rejection workflow
- Three-way matching: PO → Goods Receipt → Invoice verification
- Financial integration: Automatic G/L posting upon GR and 
  invoice, vendor account clearing

## Technical Environment
- **System:** SAP S/4HANA (UWM training instance)  
- **Company Code:** US00 (Global Bike Inc.)  
- **Purchasing Org:** US00 | **Plant:** MI00  
- **UI:** SAP GUI + SAP Fiori

## Outcomes & Observations
- Successfully executed full P2P cycle from vendor onboarding to 
  payment clearing
- Identified and documented a data discrepancy: stock showed 300 
  units (unrestricted) vs. expected 150 due to an erroneous 
  duplicate purchase order — demonstrating understanding of how 
  incorrect PO postings affect inventory valuation
- Vendor balance cleared to 0.00 USD post-payment, confirming 
  correct financial accounting integration

## Skills Applied
`SAP S/4HANA` `MM Module` `Procure-to-Pay` `Vendor Management` 
`Inventory Management` `SAP Fiori` `Financial Accounting Integration` 
`Master Data Management`
