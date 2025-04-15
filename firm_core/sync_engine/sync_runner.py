# firm_core/sync_engine/sync_runner.py

import time
from firm_clio.clio_client import get_clio_service
from firm_qbo.qbo_client import get_qbo_client
from firm_core.sync_engine.sync_logger import log_sync_event

# Business logic
from firm_clio.custom_services.matters_service import MatterService
from firm_qbo.qbo_client import create_customer_if_missing


def sync_contacts():
    """
    Sync recent Clio matters → QBO customers (basic matching).
    """
    try:
        clio_service = MatterService()
        matters = clio_service.get_recent_matters(limit=10)
    except Exception as e:
        print(f"❌ Failed to load Clio contacts: {e}")
        return

    print(f"🔄 Found {len(matters)} Clio contacts. Syncing to QBO...")

    for matter in matters:
        display_name = getattr(matter, "display_name", None) or getattr(matter, "name", None) or "Unknown"
        
        try:
            result = create_customer_if_missing(display_name)
            if result:
                log_sync_event(f"✅ Synced: {display_name} → QBO (ID: {result})")
            else:
                log_sync_event(f"⚠️ Could not sync: {display_name}")
        except Exception as e:
            log_sync_event(f"❌ Error syncing {display_name}: {e}")


def run_full_sync():
    """
    Runs the full sync process.
    """
    print("🚀 Running full Clio → QBO sync...")
    start = time.time()

    sync_contacts()

    duration = round(time.time() - start, 2)
    print(f"\n✅ Sync complete in {duration} seconds.")
