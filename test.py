# test_clients.py
import os
from dotenv import load_dotenv
load_dotenv()

from utils.token_storage import load_token_data
from firm_clio.clio_client import get_clio_client
from firm_qbo.qbo_client import get_qbo_client

# ✅ Test Clio
print("\n🔹 Clio Test")
clio = get_clio_client()
print(clio)  # or make a sample call

# ✅ Test QBO
print("\n🔹 QBO Test")
qbo = get_qbo_client()
print(qbo)  # or sample QBO call like list customers
