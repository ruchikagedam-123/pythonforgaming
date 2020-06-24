# Match Maker Project has card which has perfect match for itself in window
import random
import time
from tkinter import Tk, Button, DISABLED

# show_symbols is used to show symbols on the cards and make it match if two cards are matching
def show_symbols(x,y):
    global first
    global previousx, previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()
    # First is True until and unless get perfect match once it got then both of that cards are shown and fixed
    if first:
        previousx = x
        previousy = y
        first = False
    # Else make the clicked card Empty if not matched with anyone
    elif previousx!=x or previousy!=y:
        if buttons[previousx,previousy]['text']!=buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] =' '
        # If match found then That card gets disabled
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
            first = True




win = Tk()
win.title('Matchmaker')
win.resizable(width=False, height=False)
first = True
previousx = 0
previousy = 0
# Create Number of Buttons
buttons = {}
# Create number of button with symbols
button_symbols = {}
# Creating Number of Random Symbols
symbol = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
          u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728',
          u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
          u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728',
          u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
          u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728'
          ]
# shuffling the Symbols every time
random.shuffle(symbol)

for x in range(6):
    for y in range(6):
        button = Button(command = lambda x=x, y=y: show_symbols(x,y), width = 10, height = 5)
        button.grid(column = x,row = y)
        # To store the Symbol of particular button
        buttons[x,y]=button
        button_symbols[x,y] = symbol.pop()


win.mainloop()
