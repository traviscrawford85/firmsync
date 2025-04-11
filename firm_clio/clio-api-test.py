import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from firm_clio.clio_client import get_clio_client
from firm_clio.clio_sdk.api.matters_api import MattersApi

def test_matters():
    client = get_clio_client()
    matters_api = MattersApi(client)

    response = matters_api.matter_index(limit=3)
    for matter in response["data"]:
        print(f"📁 Matter: {matter['display_number']} - {matter['description']} (ID: {matter['id']})")

if __name__ == "__main__":
    test_matters()
