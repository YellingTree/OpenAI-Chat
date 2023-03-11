import os
try:
    import openai
except ImportError:
    print("Error OpenAI api not installed. Run 'pip install openai'")
import json
import platform
# Windows Support
try:
    import readline
except ImportError:
    import curses

###API KEY
openai.api_key = ("sk-YOUR API KEY")
###FILE LOAD
hist_file = "history.json"
sys_file = "sysMsg.json"
persona = "Persona.json"
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
if os.path.isfile(sys_file):
    with open(sys_file, "r") as f:
        sys_msg = json.load(f)
else:
    sys_msg = []
if os.path.isfile(persona):
    with open(persona, "r") as f:
        persona = json.load(f)
else:
    persona = []

def CleanScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system(f'clear')

def ErrorMsg(messages):
    print("Error, it is likely your message attempted to request too many tokens. Reduce the max_tokens or shorten your message.")
    if input("Save? (y/n)") == "y":
        with open(hist_file, "w") as f:
            json.dump(messages, f)
            print("Chat Saved.")
    if input("Would you like the system to repopulate the persona and system and appened the last 5 msgs to histoy?\nThis is to atempt to continue the converstation by lowering used tokens.\nTHIS WILL EFFECT HISTORY FILE IF YOU SAVE AGAIN BACKUP IF YOU WISH FOR UNALTERED\n(y/n)") == "y":
        last_five = messages[-5:]
        messages = []
        messages.append(sys_msg)
        messages.append(persona)
        messages.append(last_five)
    else:
        next = False
    return(next)

def Chat():
    CleanScreen()
    save = False
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
            flag = False
            messages.append({"role": "user", "content": prompt})
            try: 
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages, max_tokens = 1596)
            except:
                flag = True
            if flag == True:
              next = ErrorMsg(messages)
            else:
                data = response['choices'][0]['message']['content']
                print("AI:", data)
                print()
                messages.append({"role": "assistant", "content": data})
    # Save conversation to history file
    if save:
        with open(hist_file, "w") as f:
            json.dump(messages, f)
            print("Chat Saved.")
    print(response)

def SysMsgCreate():
    CleanScreen()
    print("Type 'end' to save and exit.")
    next = True
    save = False
    while next:
        msg = input("System Msg: ")
        print
        if msg == "end":
            if input("Save? (y/n): ") == "y":
                save = True
            else:
                save = False
            next = False
            print("Closed")
        elif msg:
            sys_msg.append({"role": "system", "content": msg})
    if save:
        with open(sys_file, "w") as f:
            json.dump(sys_msg, f)
            print("Saved.")

def HistoryGen():
    CleanScreen()
    save = False
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
            data = input("AI: ")
            print()
            messages.append({"role": "assistant", "content": data})
    # Save conversation to history file
    if save:
        with open(hist_file, "w") as f:
            json.dump(messages, f)
            print("Chat Saved.")
    print(response)

def MainMenu():
    menu = True
    while menu:  
        CleanScreen()  
        print("What would you like to do?")
        options = ["(1) Chat", "(2) System Message Creator", "(3) Chat History Creator", "(4) Quit"]
        for option in options:
            print("")
            print(option)
        print()
        selection = input("Selection #: ")
        if selection == "1":
            Chat()
        if selection == "2":
            SysMsgCreate()
        if selection == "3":
            HistoryGen()
        if selection == "4":
            menu = False
        else:
            print("Invalid Selection - Numbers Only")
    
MainMenu()
print("Shutting Down")
