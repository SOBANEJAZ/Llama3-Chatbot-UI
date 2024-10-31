from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

stream = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a famous podcaster, Andrew Huberman."},
        {
            "role": "user",
            "content": "Who are you?",
        },
    ],
    model="llama-3.2-90b-vision-preview",
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
