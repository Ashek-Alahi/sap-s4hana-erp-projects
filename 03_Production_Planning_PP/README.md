# SAP PP Academic Make-to-Stock Project

## Portfolio Summary
This PP project demonstrates a make-to-stock production planning and execution cycle in an SAP S/4HANA academic training system, connecting demand planning, MRP, BOM, routing, production orders, confirmations, and inventory movement.

## Business Problem
Manufacturing teams need to translate demand into feasible production while checking component availability, routing steps, order completion, and finished goods inventory. Poor planning creates shortages, delays, and unreliable stock positions.

## Process Scope
- Maintain finished goods and component material master views.
- Review multilevel BOM for finished product and components.
- Review routing and work center operations.
- Enter planned independent requirements.
- Run MRP for single-item, multilevel planning.
- Review stock/requirements list.
- Post goods receipt for raw material availability.
- Create and release production order.
- Post goods issue of components to production order.
- Confirm production order yield.
- Post goods receipt for finished goods into inventory.

## SAP Configuration / Execution Evidence
- Product documented: Women’s Off Road Bike (`ORWN1148`) in plant `DL00`.
- Transactions documented include `MM02`, `CS03`, `CA03`, `MD61`, `MD02`, `MD04`, `MIGO`, `CO01`, `CO02`, and `CO11N`.
- Planning strategy documented: make-to-stock strategy `40` with PIR consumption.
- MRP results documented: materials planned, planned orders, dependent requirements, and runtime.
- Production execution evidence includes goods issue, confirmation yield, and finished goods receipt.

## Business Value
PP matters because it links demand, materials, production capacity, and inventory. The process gives managers visibility into whether the company can produce the planned quantity, whether components are available, and whether finished goods stock increased after production.

## KPIs / Controls
- Planned vs produced quantity.
- Component availability.
- Production order completion.
- Finished goods stock movement.
- MRP exception review.
- Goods issue accuracy.
- Confirmation yield.

## Interview Defense
- **Q: What is make-to-stock planning?** A: It is production based on expected demand, where finished goods are produced for inventory before a specific sales order is required.
- **Q: Why are BOM and routing important?** A: The BOM defines required components, while routing defines the operations and work centers needed to build the product.
- **Q: What does MRP do?** A: MRP compares demand, stock, and supply elements to create procurement or production proposals.
- **Q: Why post goods issue to a production order?** A: Goods issue records component consumption and connects inventory reduction to the production order.
- **Q: What proves production completion?** A: Confirmation records yield and operational completion, and goods receipt increases finished goods inventory.

## Limitations
- Academic training-system scenario.
- Not production implementation.
- No company-sensitive data.
- Synthetic analytics data is used only in the separate analytics extension.
- PDF evidence may contain academic identifiers from the original coursework.

## Evidence Files
- `PP Final project.pdf`
