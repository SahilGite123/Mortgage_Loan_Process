from openai import OpenAI
import os
import json


class ValuationAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def estimate_value(self, context: dict) -> dict:
        prompt = f"""
You are a real estate valuation assistant.

Use:
- Government land rates (assumed reference)
- Location accessibility
- Vision analysis ONLY if available

Do NOT hallucinate numbers.
If data is limited, say confidence is low.

Return JSON only.

Context:
{json.dumps(context, indent=2)}

Output format:
{{
  "estimated_value_in_inr": number,
  "valuation_reasoning": "text",
  "confidence_level": "low | medium | high"
}}
"""

        response = self.client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        return json.loads(response.output_text)
