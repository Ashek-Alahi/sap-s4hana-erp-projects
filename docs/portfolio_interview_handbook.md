# Portfolio Interview Handbook

## 30-Second Explanation
This is an academic SAP S/4HANA ERP portfolio built from training-system coursework across FI/CO, MM, PP, ABAP reporting design, and HCM. I translated the evidence into business-process documentation and added a small Python analytics extension using synthetic SAP-style data to show KPI and exception-reporting skills.

## 1-Minute Explanation
The portfolio demonstrates how I understand ERP as connected business processes rather than isolated screens. FI/CO covers G/L, A/P, A/R, payments, cost centers, and assessment cycles. MM covers procure-to-pay from vendor and RFQ through PO, goods receipt, invoice verification, and payment clearing. PP covers make-to-stock planning with PIR, MRP, BOM, routing, production order execution, confirmation, and finished goods receipt. ABAP is documented as report design using SAP tables and selection-screen logic, and HCM is included as a supporting academic group project. The analytics folder uses synthetic data to generate balances, three-way match exceptions, production variance, and cost center summaries.

## 3-Minute Explanation
This repository is structured for ERP, SAP, and business analytics interviews. The module READMEs explain the business problem, process scope, SAP evidence, business value, KPIs, limitations, and interview defense. The documents folder includes a KPI catalog, SAP table reference, evidence index, public scope note, and recruiter summary. The analytics extension proves that I can convert ERP process logic into data outputs using Python and SQL-style thinking. The project is carefully scoped as academic SAP S/4HANA training-system work, academic-only rather than a live rollout or production system project.

## 10 ERP Interview Questions and Answers
1. **What is ERP?** ERP integrates business processes such as finance, procurement, production, and HR into shared master data, transactions, controls, and reports.
2. **Why does SAP integration matter?** A procurement or production transaction can create financial impact, so teams need consistent data across modules.
3. **What did FI/CO demonstrate?** It demonstrated accounting postings, vendor and customer processes, payments, cost centers, and allocation thinking.
4. **What did MM demonstrate?** It demonstrated procure-to-pay controls from vendor selection through invoice verification and payment clearing.
5. **What did PP demonstrate?** It demonstrated make-to-stock planning and production execution from PIR and MRP through goods receipt.
6. **What did ABAP demonstrate?** It demonstrated report design logic: choosing tables, filters, joins, and output fields for accounting users.
7. **What did HCM demonstrate?** It demonstrated supporting HR process knowledge across organizational management, qualifications, and hiring action documentation.
8. **How do master data and transactions differ?** Master data describes stable business objects, while transactions record business events.
9. **What is a control-risk finding?** It is a process issue that can cause inaccurate data, duplicate activity, incorrect payment, or reporting error.
10. **How would you support users in an ERP role?** I would clarify the business issue, trace master data and transaction flow, check controls, and document the resolution clearly.

## 10 Business Analytics Questions and Answers
1. **Why add analytics to an SAP portfolio?** Analytics shows how ERP transactions become management information and exception reports.
2. **What does the Python script do?** It reads synthetic CSV files and produces KPI and exception outputs for FI, MM, PP, and CO.
3. **What is an exception report?** It highlights records that need attention, such as mismatches between PO, goods receipt, and invoice.
4. **What is a KPI?** A KPI is a measurable indicator of process performance or control status.
5. **How would you validate ERP data?** I would reconcile totals, check missing keys, review dates, compare process steps, and verify exceptions with business users.
6. **Why use synthetic data?** It allows safe public demonstration without exposing real company or client data.
7. **How does A/R differ from A/P analytics?** A/R focuses on customer receivables and collections; A/P focuses on vendor liabilities and payments.
8. **What does production variance show?** It shows whether actual output matched the planned production quantity.
9. **What does cost center analysis show?** It shows actual expense totals by responsibility area for management review.
10. **How would SQL fit this portfolio?** SQL can reproduce the same joins, summaries, and exception checks against relational ERP-style tables.

## 10 Project Defense Questions and Answers
1. **Was this a live company SAP rollout?** No. It is academic SAP S/4HANA training-system work with synthetic analytics assets.
2. **Did you use real client data?** No. Public documentation avoids real client data, and analytics data is synthetic.
3. **Why keep PDFs?** They provide academic evidence for the documented exercises.
4. **Why not edit the PDFs?** They are retained as original academic evidence; public markdown adds safer professional framing.
5. **Why include HCM if it is supporting?** It shows cross-functional ERP awareness while clearly limiting the claim.
6. **Are the ABAP samples exported from SAP?** No. Any public sample code is educational and reconstructed from documented report design.
7. **How did you improve recruiter readability?** I standardized module READMEs, added evidence mapping, added interview material, and created analytics outputs.
8. **What is the strongest module?** FI/CO is one of the strongest because it connects accounting fundamentals with SAP process evidence and integration logic.
9. **What is the main MM insight?** The duplicate PO situation is framed as a procurement control-risk finding tied to inventory accuracy.
10. **What is the main PP insight?** MRP and production execution show how demand becomes supply and finished goods inventory.

## What Not to Claim in Interviews
- Do not claim this was a live client rollout.
- Do not claim ownership of a production SAP landscape.
- Do not claim the synthetic analytics files came from SAP.
- Do not claim PDF evidence is cleaned of all academic identifiers.
- Do not claim complete exported ABAP source code unless the file is explicitly present and labeled.
- Do not claim HCM specialization beyond the supporting academic group project evidence.
