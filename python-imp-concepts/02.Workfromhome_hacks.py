# create the .py file and open terminal
# then install pyautogui in this way "pip install pyautogui"
# write the python code as below

import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(200)
    for i in range(0, 100):
        pyautogui.moveTo(0, i*5)
    for i in range(0, 3):
        pyautogui.press('shift')
