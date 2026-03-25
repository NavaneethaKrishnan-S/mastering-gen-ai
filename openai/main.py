from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Hi there! Naveen here!",
    model="openai/gpt-oss-20b",
)
print(response.output_text)
