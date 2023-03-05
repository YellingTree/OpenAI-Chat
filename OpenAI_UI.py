import os
import platform
# Module to center text on screen
def CenterText(text):
    term_size = os.get_terminal_size()
    term_width = term_size.columns
    center_screen = term_width // 2 - len(text) // 2
    center_text = ' ' * center_screen + text
    print(center_text)
# Moduel to write dashes across the term
def ScreenBreak():
    term_size = os.get_terminal_size()
    term_width = term_size.columns
    dash = "-"
    while len(dash) < term_width:
        dash = dash + "-"
    print(dash)
