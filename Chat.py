import OpenAI_Chat as Chat
import OpenAI_UI as UI
import OpenAI_tools as Tools
import os
import platform

term_size = os.get_terminal_size()
term_width = term_size.columns
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system(f'clear')
UI.CenterText("OpenAI-Chat")
UI.CenterText("Main Menu")
UI.ScreenBreak()
print()
UI.CenterText("Select an Option:")
print()
UI.CenterText("Chat")
print()
UI.ScreenBreak()
user_input = input("Selection: ")
selection = False
while selection == False:
    if user_input == "Chat" or "chat":
        Chat.StartChat()
    else:
        print("Wrong Selection")