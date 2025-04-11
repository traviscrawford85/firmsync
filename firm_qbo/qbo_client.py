import os
from firm_auth.oauth_flow import load_authenticated_client
from quickbooks import QuickBooks

def get_qbo_client():
    auth_client = load_authenticated_client()

    return QuickBooks(
        sandbox=True,
        auth_client=auth_client,
        refresh_token=auth_client.refresh_token,
        company_id=os.getenv("QB_REALM_ID")
    )
