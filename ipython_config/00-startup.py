# IPython startup file: 00-startup.py

from IPython import get_ipython
import os
import sys
from dotenv import load_dotenv

# 🌱 Load environment variables early
load_dotenv()
print("🌱 .env loaded in IPython startup")

# 🔧 Add project root to sys.path
project_root = os.path.expanduser(r"E:\Projects\firmsync")
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(f"✅ Added project root to PYTHONPATH: {project_root}")

# 🔁 Autoreload setup
ip = get_ipython()
if ip:
    ip.run_line_magic("load_ext", "autoreload")
    ip.run_line_magic("autoreload", "2")
    print("🔁 Autoreload enabled.")

# 📁 Set working directory
os.chdir(project_root)
print(f"📁 Working directory set to: {project_root}")

# 🔄 QuickBooks loader
def load_qbo_tools():
    try:
        from firm_qbo.qbo_client import get_qbo_client
        from quickbooks.objects.customer import Customer
        from utils.token_storage import get_token_path

        print(f"🔍 Resolved QBO token path: {get_token_path('qbo')}")
        global qbo_client
        qbo_client = get_qbo_client()

        print("\n🧠 QuickBooks tools loaded:")
        print("   - get_qbo_client()")
        print("   - qbo_client")
        print("   - Customer.all(qb=qbo_client)")
        print("✅ QBO ready for API interaction.")
    except Exception as e:
        print(f"⚠️ QBO tools failed to load: {e}")

# 🔄 Clio loader
def load_clio_tools():
    try:
        from firm_clio.clio_client import get_clio_client, get_clio_service
        from custom_services.matter_service import MatterService
        from firm_clio.custom_models.matter import MatterModel

        global clio_client, matter_service
        clio_client = get_clio_client()
        matter_service = get_clio_service()

        print("\n🧠 Clio SDK tools loaded:")
        print("   - get_clio_client(), get_clio_service()")
        print("   - matter_service.get_recent_matters(limit)")
        print("   - matter_service.get_matter_by_id(id)")
        print("   - MatterModel")
        print("✅ Clio ready for API interaction.")
    except Exception as e:
        print(f"⚠️ Clio tools failed to load: {e}")

# 🔍 Optional: Inspect .env keys
def show_env_keys():
    from dotenv import dotenv_values
    keys = dotenv_values().keys()
    print(f"📄 Loaded .env keys: {', '.join(keys)}")

# 🧰 Load both sets of tools
try:
    load_qbo_tools()
    load_clio_tools()
    print("\n🔄-----------------------------")
    print("  ✅ IPython environment ready")
    print("🔄-----------------------------")
except Exception as e:
    print(f"⚠️ IPython startup failed: {e}")

# 📚 Launch API documentation in browser
def open_api_docs():
    import webbrowser
    webbrowser.open("https://docs.developers.clio.com/api-reference/")
    webbrowser.open("https://developer.intuit.com/app/developer/qbo/docs/api")
    print("📖 Opened Clio + QuickBooks API docs in browser.")
