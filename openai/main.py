from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input=[
        {"role": "system", "content":"You are expert in Maths. So answer only related maths. Say sorry for any unrelated questions."},
        {"role": "user", "content":"What is my name?"}
        ],
    model="openai/gpt-oss-20b",
)
print(response.output_text)
