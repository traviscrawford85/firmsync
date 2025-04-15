# firm_qbo/custom_services/purchase_service.py

from quickbooks.objects.purchase import Purchase
from quickbooks.objects.account import Account
from quickbooks.objects.vendor import Vendor
from firm_qbo.qbo_client import get_qbo_client
from firm_qbo.mappers.purchase_mapper import activity_to_qbo_purchase


class PurchaseService:
    def __init__(self):
        self.qb = get_qbo_client()

    def get_recent_purchases(self, limit: int = 10):
        """
        Fetch the most recent QBO purchases (unordered).
        """
        try:
            purchases = Purchase.all(qb=self.qb)
            return purchases[:limit]
        except Exception as e:
            print(f"❌ Failed to fetch purchases: {e}")
            return []

    def create_purchase_from_activity(self, activity_model):
        """
        Create a QBO purchase record from an internal Clio activity model.
        """
        try:
            purchase = activity_to_qbo_purchase(activity_model)
            purchase.save(qb=self.qb)
            print(f"✅ Purchase created: {purchase.Id}")
            return purchase
        except Exception as e:
            print(f"❌ Failed to create purchase: {e}")
            return None
