from openai import OpenAI
import os
import json


class WorkflowAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def decide_next_steps(self, context: dict) -> dict:
        prompt = f"""
You are a workflow planning AI for property valuation.

Rules:
1. If input is city-level or area-level → DO NOT use vision.
2. If input is property-level (house, plot, bungalow) → vision MAY be required.
3. Vision is ONLY for verification, not pricing.
4. Return STRICT JSON only.

Input:
{context}

Output format:
{{
  "steps": ["collect_location_data", "estimate_value"],
  "needs_visual_verification": true | false,
  "confidence": "low | medium | high",
  "reason": "short explanation"
}}
"""

        response = self.client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        return json.loads(response.output_text)

