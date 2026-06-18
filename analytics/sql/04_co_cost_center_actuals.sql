-- Synthetic SAP-style data only; not a SAP export.
SELECT controlling_area, cost_center, SUM(actual_amount) AS total_actual_expense
FROM cost_center_actuals
GROUP BY controlling_area, cost_center
ORDER BY controlling_area, cost_center;
