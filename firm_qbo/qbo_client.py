# firm_qbo/qbo_client.py

import os
from firm_qbo.auth.oauth_flow import load_authenticated_client
from quickbooks import QuickBooks

def get_qbo_client():
    auth_client = load_authenticated_client()
    return QuickBooks(
        sandbox=os.getenv("QB_ENVIRONMENT", "sandbox").lower() == "sandbox",
        auth_client=auth_client,
        refresh_token=auth_client.refresh_token,
        company_id=os.getenv("QB_REALM_ID")
    )
