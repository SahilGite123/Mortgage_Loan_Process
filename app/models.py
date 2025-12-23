from pydantic import BaseModel

class StartWorkflowRequest(BaseModel):
    address: str
