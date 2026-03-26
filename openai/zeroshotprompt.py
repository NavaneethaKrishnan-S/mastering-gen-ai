from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = "You should answer only coding related answers. If something else, just say sorry."

response = client.responses.create(
    input=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role": "user", "content":"Can you write a program which tells a joke?"}
        ],
    model="openai/gpt-oss-20b",
)
print(response.output_text)

# you ask an AI to do a task without giving any examples, that's called zero-shot prompting. 
