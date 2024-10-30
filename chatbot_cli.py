from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("Hugging_Face_API_TOKEN")
print(api)

# Initialize the client
client = InferenceClient(api_key=api)

# Start with an empty message history
message_history = []

# Continuous chat loop
while True:
    # Get user input
    user_input = input("User: ")

    # Exit condition (optional)
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Chat ended.")
        break

    # Append the user's message to the history
    message_history.append({"role": "user", "content": user_input})

    # Generate the model's response
    response = ""
    for message in client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=message_history,
        max_tokens=500,
        stream=True,
    ):
        # Collect model's response text
        response += message.choices[0].delta.content
        print(message.choices[0].delta.content, end="")

    # Add the assistant's response to the message history
    print("\n")
    message_history.append({"role": "assistant", "content": response})
