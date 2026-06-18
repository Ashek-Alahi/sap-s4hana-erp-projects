-- Synthetic SAP-style data only; not a SAP export.
SELECT company_code, account_type, status, SUM(amount) AS balance_amount
FROM fi_documents
GROUP BY company_code, account_type, status
ORDER BY company_code, account_type, status;
