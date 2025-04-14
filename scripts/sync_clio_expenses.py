# This script is used to sync expenses from QBO to Clio using the Firm's custom services.

from firm_qbo.custom_services.qbo_expense_parser import parse_qbo_purchase
from firm_qbo.custom_services.convert_qbo_expense_to_firm_expense import convert_qbo_expense_to_firm_expense
from firm_clio.custom_services.clio_expense_service import sync_firm_expense_to_clio
from firm_core.models.firm_expense import FirmExpense, FirmExpenseLineItem
from firm_qbo.custom_models.qbo_expense_model import QBOExpense, QBOExpenseLine
from datetime import datetime

# Simulating the purchase payload from QBO
raw_purchase = {
    # ...your Purchase object here...

}

qbo_expense = parse_qbo_purchase(raw_purchase)
firm_expense = convert_qbo_expense_to_firm_expense(qbo_expense)
sync_firm_expense_to_clio(firm_expense)
