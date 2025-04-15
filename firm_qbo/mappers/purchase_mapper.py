# firm_qbo/mappers/purchase_mapper.py

from firm_core.custom_models.activity import ActivityModel
from quickbooks.objects.purchase import Purchase, PurchaseLine
from quickbooks.objects.account import Account
from quickbooks.objects.vendor import Vendor
from firm_qbo.mappers.vendor_mapper import get_or_create_vendor

def to_internal_activity(purchase_line: dict, purchase_meta: dict) -> ActivityModel:
    return ActivityModel(
        id=None,
        source="qbo",
        external_id=purchase_meta["Id"],
        date=purchase_meta["TxnDate"],
        description=purchase_line["Description"],
        amount=float(purchase_line["Amount"]),
        quantity=purchase_line.get("Qty", 1.0),
        type="purchase",
        contact_id=purchase_meta.get("EntityRef", {}).get("value"),
    )

def to_qbo_purchase_line(activity: ActivityModel) -> dict:
    return {
        "Description": activity.description,
        "Amount": activity.amount,
        "DetailType": "AccountBasedExpenseLineDetail",
        "AccountRef": {"value": "EXPENSE_ACCOUNT_ID"}
    }

def activity_to_qbo_purchase(activity: ActivityModel) -> Purchase:
    purchase = Purchase()

    purchase.AccountRef = Account()
    purchase.AccountRef.value = "57"  # Or map this dynamically

    purchase.VendorRef = Vendor()
    vendor_id = get_or_create_vendor(activity.contact_id or "Unknown Vendor")
    purchase.VendorRef.value = vendor_id


    line = PurchaseLine()
    line.Amount = activity.amount or (activity.rate or 0) * (activity.quantity or 1)
    line.Description = activity.description

    purchase.Line = [line]
    purchase.TotalAmt = line.Amount

    return purchase
