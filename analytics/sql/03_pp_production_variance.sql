-- Synthetic SAP-style data only; not a SAP export.
SELECT production_order_id, plant, material_id, planned_quantity, actual_quantity,
       actual_quantity - planned_quantity AS quantity_variance,
       CAST(actual_quantity AS REAL) / planned_quantity AS completion_rate
FROM production_orders
ORDER BY production_order_id;
