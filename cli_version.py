from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a famous podcaster, Andrew Huberman."}
]

def chat(user_input):
    # Add user's message to history
    conversation_history.append({"role": "user", "content": user_input})

    # Get response from Groq
    stream = client.chat.completions.create(
        messages=conversation_history, model="llama-3.2-90b-vision-preview", stream=True
    )

    # Collect and print the response
    full_response = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content is not None:
            full_response += content
            print(content, end="", flush=True)
    print()  # New line after response

    # Add assistant's response to history
    conversation_history.append({"role": "assistant", "content": full_response})

    return full_response


def view_history():
    for message in conversation_history:
        print(f"{message['role'].upper()}: {message['content']}\n")


# Looping
print("Chat started (type 'quit' to exit, 'history' to view conversation history)")
while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "quit":
        break
    elif user_input.lower() == "history":
        view_history()
    elif user_input:
        chat(user_input)
