import uuid
from datetime import datetime

def create_envelope(from_agent, to_agent, msg_type, payload):
    return {
        "mcp_message_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "from": from_agent,
        "to": to_agent,
        "type": msg_type,
        "payload": payload
    }
