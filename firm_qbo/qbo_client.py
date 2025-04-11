# firm_qbo/qbo_client.py

import os
from dotenv import load_dotenv
from quickbooks import QuickBooks

load_dotenv()

qb_client = QuickBooks(
    sandbox=True,
    access_token=os.getenv("ACCESS_TOKEN"),
    refresh_token=os.getenv("REFRESH_TOKEN"),
    company_id=os.getenv("REALM_ID")
)
