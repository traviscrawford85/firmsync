from clio_sdk.models import ActivityBase
from datetime import datetime
from firm_clio.clio_client import get_clio_client  # assuming you have this setup
from firmsync.utils.helpers import to_clio_currency_dict
from firm_clio.custom_models.firm_expense_model import FirmExpense

def sync_firm_expense_to_clio(firm_expense: FirmExpense):
    clio = get_clio_client()

    for line in firm_expense.line_items:
        activity_data = ActivityBase(
            type="HardCostEntry",
            date=firm_expense.date,
            quantity=line.amount,
            price=line.amount,
            total=line.amount,
            flat_rate=True,
            billed=False,
            on_bill=False,
            note=line.description or firm_expense.note,
            reference=firm_expense.reference,
            currency=to_clio_currency_dict("USD"),  # Assuming USD
        )

        clio.activities.create(activity_data.model_dump(by_alias=True))
