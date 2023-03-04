import os
try:
    import openai
except ImportError:
    print("Error OpenAI api not installed. Run 'pip install openai'")
import json
import platform
try:
    import readline
except ImportError:
    import pyreadline as readline
# Set header for term
header = "OpenAI Chat"
if platform.system() == 'Windows':
    os.system(f'title {header}')
else:
    os.system(f'export PS1="{header} \w$ "')
#
# 
# Load your API key from an environment variable or secret management service
openai.api_key = ("sk-YOUR API KEY HERE")
#
#
# Specify the file path for the conversation history
hist_file = "history.json"
# Load history file or use default history array
if os.path.isfile(hist_file):
    with open(hist_file, "r") as f:
        messages = json.load(f)
else:
    messages = [
        {"role": "system", "content": "You are helpful and kind."},
        {"role": "user", "content": "Hello, how are you doing?"},
        {"role": "assistant", "content": "I'm doing good! How about yourself?"},
        {"role": "user", "content": "I'm good! Thanks for asking."},
        {"role": "assistant", "content": "What would you like to chat about?"}
    ]
# Setting term for convo
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system(f'clear')
# TODO: System message injection after X loops
next = True
while next:
    prompt = input("You: ")
    print()
    if prompt == "end":
        if input("Save? (y/n): ") == "y":
            save = True
        else:
            save = False
        next = False
        response = "Closed"
    elif prompt:
        messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages, max_tokens = 3096)
        data = response['choices'][0]['message']['content']
        print("AI:", data)
        print()
        # Append the latest response to the history
        messages.append({"role": "assistant", "content": data})
# Save conversation to history file
if save:
    with open(hist_file, "w") as f:
        json.dump(messages, f)
    print("Chat Saved.")
print(response)