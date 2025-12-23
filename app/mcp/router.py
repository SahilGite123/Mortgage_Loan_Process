from app.agents.workflow_agent import WorkflowAgent
from app.agents.data_collector_agent import DataCollectorAgent
from app.agents.vision_agent import VisionAgent
from app.agents.valuation_agent import ValuationAgent
from app.mcp.envelope import create_envelope
from app.utils.logger import log_event
from app.utils.address_utils import is_precise_address


class MCPRouter:
    def route(self, envelope: dict):

        log_event(envelope)

        if envelope.get("type") != "request":
            return None

        response_payload = {}

        workflow_agent = WorkflowAgent()
        data_collector = DataCollectorAgent()
        vision_agent = VisionAgent()
        valuation_agent = ValuationAgent()

        # 1️⃣ Planning
        workflow_decision = workflow_agent.decide_next_steps({
            "inputs": envelope["payload"]
        })
        response_payload["workflow_decision"] = workflow_decision

        # 2️⃣ Location data
        location_data = data_collector.collect_location_data(
            envelope["payload"]["address"]
        )
        response_payload["location_data"] = location_data

        # 3️⃣ Vision (STRICTLY CONDITIONAL)
        vision_analysis = {
            "status": "skipped",
            "reason": "Address not precise enough"
        }

        if (
            workflow_decision.get("needs_visual_verification") is True
            and is_precise_address(location_data)
        ):
            vision_analysis = vision_agent.analyze_location(
                location_data["latitude"],
                location_data["longitude"]
            )

        response_payload["vision_analysis"] = vision_analysis

        # 4️⃣ Valuation
        valuation = valuation_agent.estimate_value({
            "address": envelope["payload"]["address"],
            "location_data": location_data,
            "vision_analysis": vision_analysis,
            "confidence": workflow_decision.get("confidence")
        })

        response_payload["property_valuation"] = valuation

        return create_envelope(
            from_agent="mcp",
            to_agent="client",
            msg_type="response",
            payload=response_payload
        )
