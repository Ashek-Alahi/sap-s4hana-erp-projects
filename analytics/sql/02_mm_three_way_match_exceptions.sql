-- Synthetic SAP-style data only; not a SAP export.
SELECT po.po_id, po.vendor_id, po.material_id, po.po_quantity, gr.received_quantity,
       inv.invoiced_quantity, po.po_quantity * po.po_unit_price AS expected_invoice_amount,
       inv.invoice_amount
FROM purchase_orders po
LEFT JOIN goods_receipts gr ON gr.po_id = po.po_id
LEFT JOIN vendor_invoices inv ON inv.po_id = po.po_id
WHERE po.po_quantity <> gr.received_quantity
   OR po.po_quantity <> inv.invoiced_quantity
   OR po.po_quantity * po.po_unit_price <> inv.invoice_amount;
