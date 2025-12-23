import json
import os
from datetime import datetime

LOG_DIR = "data/logs"
LOG_FILE = os.path.join(LOG_DIR, "audit_log.json")

# Ensure directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def log_event(event):
    event["logged_at"] = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")
