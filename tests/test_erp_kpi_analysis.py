"""Regression tests for the SAP-style synthetic ERP analytics extension."""

import sys
from pathlib import Path

import pytest

pd = pytest.importorskip("pandas")

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from analytics.python.erp_kpi_analysis import (  # noqa: E402
    build_cost_center_summary,
    build_fi_balances,
    build_production_variance,
    build_three_way_match_exceptions,
)


def test_build_fi_balances_summarizes_by_company_account_and_status() -> None:
    fi_documents = pd.DataFrame(
        [
            {"company_code": "US00", "account_type": "AR", "status": "Open", "amount": 100.0},
            {"company_code": "US00", "account_type": "AR", "status": "Open", "amount": 50.0},
            {"company_code": "US00", "account_type": "AP", "status": "Cleared", "amount": 75.0},
        ]
    )

    result = build_fi_balances(fi_documents)

    ar_open = result.query("account_type == 'AR' and status == 'Open'").iloc[0]
    assert ar_open["balance_amount"] == 150.0
    assert set(result.columns) == {"company_code", "account_type", "status", "balance_amount"}


def test_build_three_way_match_exceptions_flags_quantity_and_amount_mismatches() -> None:
    purchase_orders = pd.DataFrame(
        [
            {"po_id": "4501", "vendor_id": "V1", "material_id": "M1", "po_quantity": 10, "po_unit_price": 5},
            {"po_id": "4502", "vendor_id": "V2", "material_id": "M2", "po_quantity": 8, "po_unit_price": 3},
        ]
    )
    goods_receipts = pd.DataFrame(
        [
            {"po_id": "4501", "received_quantity": 10},
            {"po_id": "4502", "received_quantity": 7},
        ]
    )
    vendor_invoices = pd.DataFrame(
        [
            {"po_id": "4501", "invoiced_quantity": 10, "invoice_amount": 50},
            {"po_id": "4502", "invoiced_quantity": 8, "invoice_amount": 30},
        ]
    )

    result = build_three_way_match_exceptions(purchase_orders, goods_receipts, vendor_invoices)

    assert result["po_id"].tolist() == ["4502"]
    exception = result.iloc[0]
    assert bool(exception["quantity_exception"]) is True
    assert bool(exception["invoice_amount_exception"]) is True


def test_build_production_variance_calculates_variance_and_completion_rate() -> None:
    production_orders = pd.DataFrame(
        [
            {
                "production_order_id": "1001",
                "plant": "DL00",
                "material_id": "FG1",
                "planned_quantity": 100,
                "actual_quantity": 90,
                "status": "Confirmed with variance",
            }
        ]
    )

    result = build_production_variance(production_orders)

    assert result.iloc[0]["quantity_variance"] == -10
    assert result.iloc[0]["completion_rate"] == 0.9


def test_build_cost_center_summary_groups_actual_expenses() -> None:
    cost_center_actuals = pd.DataFrame(
        [
            {"controlling_area": "NA00", "cost_center": "CC-FIN", "actual_amount": 1000},
            {"controlling_area": "NA00", "cost_center": "CC-FIN", "actual_amount": 250},
            {"controlling_area": "NA00", "cost_center": "CC-MFG", "actual_amount": 500},
        ]
    )

    result = build_cost_center_summary(cost_center_actuals)

    finance_total = result.query("cost_center == 'CC-FIN'").iloc[0]
    assert finance_total["total_actual_expense"] == 1250
