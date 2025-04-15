# firm_core/sync_engine/sync_logger.py

import os
import datetime

LOG_PATH = "logs/sync_log.txt"

def log_sync_event(message: str):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"📜 Log entry: {message}")