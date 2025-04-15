# main.py

import os
from dotenv import load_dotenv

# ✅ Load environment first — before anything else runs
load_dotenv()
print("🌱 Environment loaded.")

# 🔁 Import modules *after* env is loaded
from firm_core.sync_engine.sync_runner import run_full_sync

# 🧠 Main logic
if __name__ == "__main__":
    print("🚀 Starting FirmSync...")
    run_full_sync()
