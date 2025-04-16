from typing import List, Optional
from datetime import datetime

from firm_core.custom_models.internal_expense import InternalExpense
from firm_core.custom_models.internal_contact import InternalContact
# Assuming you have a wrapper client
from firm_clio.clio_client import ClioClient
# Assuming you have a wrapper client
from firm_qbo.qbo_client import QBOClient
# Assuming you have a wrapper client
from firm_core.db_client.qbo_sync_db_client import QBOSyncDBClient


class ExpenseSyncManager:
    def __init__(self, clio_client, qbo_client):
        self.clio = clio_client
        self.qbo = qbo_client
        self.qbo_db = QBOSyncDBClient()

    def should_sync(self, activity_id: str) -> bool:
        # Check if the activity ID is already synced
        return activity_id not in self.qbo_db.get_synced_activity_ids()

    def record_sync(self, expense, qbo_purchase_id, vendor_id, customer_id, error=None):
        self.qbo_db.insert_purchase_sync(
            clio_activity_id=expense.id,
            amount=expense.amount,
            qbo_purchase_id=qbo_purchase_id,
            vendor_id=vendor_id,
            customer_id=customer_id,
            description=expense.description,
            error=error,
        )

    def pull_clio_activities(self) -> List[InternalExpense]:
        # Pull hard costs and map to InternalExpense
        clio_activities = self.clio.get_hard_cost_entries()
        return [self.map_clio_activity(activity) for activity in clio_activities]

    def map_to_internal(self, clio_activity):
        return InternalExpense(
            id=clio_activity.id,
            source="clio",
            amount=clio_activity.total,
            vendor_name=clio_activity.note,  # or derive from Contact
            clio_matter_id=clio_activity.matter_id,
            description=clio_activity.note,
            date=clio_activity.date
        )

    def map_clio_activity(self, activity: dict) -> InternalExpense:
        matter = activity.get("matter", {})
        return InternalExpense(
            id=str(activity["id"]),
            source="clio",
            amount=activity.get("total", 0.0),
            vendor_name=activity.get("contact", {}).get(
                "name"),  # vendor is often set here
            vendor_id=None,
            clio_matter_id=matter.get("id"),
            # used to find QBO sub-customer
            qbo_account_ref=matter.get("display_number"),
            description=activity.get("note", ""),
            date=datetime.fromisoformat(activity["date"]),
            synced=False,
        )

    # Match QBO vendor by name, create if not found
    def resolve_qbo_vendor(self, name: str) -> Optional[str]:
        vendor = self.qbo.get_vendor_by_name(name)
        if not vendor:
            vendor = self.qbo.create_vendor({"DisplayName": name})
        return vendor["Id"]

    # Match QBO sub-customer by display number, create if not found
    # and link to parent customer by name
    def resolve_qbo_subcustomer(self, display_number: str, client_name: str) -> Optional[str]:
        parent_customer = self.qbo.get_customer_by_name(client_name)
        if not parent_customer:
            parent_customer = self.qbo.create_customer(
                {"DisplayName": client_name})

        sub_customer = self.qbo.get_customer_by_name(display_number)
        if not sub_customer:
            sub_customer = self.qbo.create_customer({
                "DisplayName": display_number,
                "ParentRef": {"value": parent_customer["Id"]},
                "Job": True
            })
        return sub_customer["Id"]

    # Push expense to QBO as a purchase
    # or as an expense based on the vendor type
    def push_expense_to_qbo(self, expense: InternalExpense) -> bool:
        vendor_id = self.resolve_qbo_vendor(expense.vendor_name)
        subcustomer_id = self.resolve_qbo_subcustomer(
            expense.qbo_account_ref, expense.vendor_name)

        payload = {
            "VendorRef": {"value": vendor_id},
            "EntityRef": {"value": subcustomer_id, "type": "Customer"},
            "TxnDate": expense.date.date().isoformat(),
            "Line": [{
                "DetailType": "AccountBasedExpenseLineDetail",
                "Amount": expense.amount,
                "Description": expense.description,
                "AccountBasedExpenseLineDetail": {
                    "CustomerRef": {"value": subcustomer_id}
                }
            }]
        }

        result = self.qbo.create_purchase(payload)
        return bool(result)

    def push_to_qbo(self, expense: InternalExpense):
        # Map vendor and matter, post as Purchase or Expense
        ...

    # This function will orchestrate the sync process
    def sync_all_clio_to_qbo(self):
        activities = self.pull_clio_activities()
        for activity in activities:
            success = self.push_expense_to_qbo(activity)
            if success:
                self.clio.mark_activity_as_synced(activity.id)

    def should_sync(self, activity_id: str) -> bool:
        return activity_id not in self.qbo_db.get_synced_activity_ids()
