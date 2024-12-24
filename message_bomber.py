# working : Run the code and place the cursor on the text box in a tome limit of 8 seconds

# for pyautogui installation , terminal command : pip install pyautogui

import pyautogui as pg  # install this library to cotrol the cursor 
import time
import random

animals = ['monkey', 'donkey', 'dog']

time.sleep(8)  # time limit to place the cursor

for i in range(5):              # range for number of messages
    a = random.choice(animals)  # chooses a random element from the list
    pg.write(f"You are a {a}")  # types the message in the text area
    pg.press('enter')           # presses the enter to send the message

