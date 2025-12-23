from dotenv import load_dotenv
from app.agents.vision_agent import VisionAgent

load_dotenv()

agent = VisionAgent()

result = agent.analyze_location(
    latitude=18.9219841,
    longitude=72.8346543
)

print(result)
