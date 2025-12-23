import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make a real GenAI call
response = client.responses.create(
    model="gpt-4o-mini",
    input="Say hello and confirm you are a real GenAI model working correctly."
)

# Print response
print(response.output_text)
