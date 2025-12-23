from fastapi import FastAPI
from dotenv import load_dotenv
from app.mcp.router import MCPRouter
from app.mcp.context import ContextStore
from app.models import StartWorkflowRequest
import uuid

# ✅ Load environment variables FIRST
load_dotenv()

app = FastAPI(title="Property MCP Server")

router = MCPRouter()
context_store = ContextStore()

@app.post("/mcp/start")
def start_workflow(request: StartWorkflowRequest):
    workflow_id = str(uuid.uuid4())

    # Store initial context
    context_store.create_workflow(
        workflow_id,
        request.dict()
    )

    # Route through MCP
    response = router.route({
        "from": "client",
        "to": "mcp",
        "type": "request",
        "payload": request.dict()
    })

    return {
        "workflow_id": workflow_id,
        "mcp_response": response
    }
