from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = '''
You are an HR recruiter. Check whether the candidate is suitable for a Java Backend Developer role.

Example 1:
Candidate Skills: Java, Spring Boot, REST API, MySQL
Output: Suitable

Example 2:
Candidate Skills: HTML, CSS, Photoshop, Figma
Output: Not Suitable

Example 3:
Candidate Skills: Java, Hibernate, Microservices, SQL
Output: Suitable

'''

response = client.responses.create(
    input=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role": "user", "content":"React, Java, Spring Boot, PostgreSQL"}
        ],
    model="openai/gpt-oss-20b",
)
print(response.output_text)

# Teaching the model by showing a few input-output examples before asking it to solve the actual task.
