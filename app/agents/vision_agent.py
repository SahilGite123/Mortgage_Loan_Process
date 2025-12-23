from openai import OpenAI
import os


class VisionAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_location(self, latitude: float, longitude: float) -> dict:
        image_url = (
            f"https://maps.googleapis.com/maps/api/streetview"
            f"?size=640x640&location={latitude},{longitude}"
            f"&key={os.getenv('GOOGLE_MAPS_API_KEY')}"
        )

        prompt = """
You are a visual verification assistant.

Rules:
- Do NOT assume the image is the exact property.
- Only describe visible surroundings.
- If unsure, say confidence is LOW.
- Do NOT estimate property value.

Return JSON only.
"""

        response = self.client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": "Analyze surroundings"},
                        {"type": "input_image", "image_url": image_url}
                    ]
                }
            ]
        )

        return {
            "image_source": "google_street_view",
            "image_url": image_url,
            "analysis": response.output_text,
            "confidence": "low"
        }
