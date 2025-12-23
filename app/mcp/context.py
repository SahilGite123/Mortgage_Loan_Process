class ContextStore:
    def __init__(self):
        self.store = {}

    def create_workflow(self, workflow_id, initial_data):
        self.store[workflow_id] = {
            "inputs": initial_data,
            "agent_outputs": {},
            "status": "IN_PROGRESS"
        }

    def update_agent_output(self, workflow_id, agent_name, output):
        self.store[workflow_id]["agent_outputs"][agent_name] = output

    def get_context(self, workflow_id):
        return self.store.get(workflow_id)
