from openai import OpenAI
import os
import json

class UnderwriterAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def make_decision(self, context: dict):
        prompt = f"""
You are a mortgage underwriter AI.

Based on the property details below, return ONLY valid JSON.

Decide one of:
- APPROVE
- REVIEW
- REJECT

JSON format:
{{
  "decision": "APPROVE | REVIEW | REJECT",
  "risk_score": 0.0-1.0,
  "confidence": "HIGH | MEDIUM | LOW",
  "reasoning": "short explanation"
}}

Context:
{json.dumps(context, indent=2)}
"""

        response = self.client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        return response.output_text
