import pyautogui
import os ,time

for i in range(4):
  pyautogui.click(x=1164, y=163)
  time.sleep(3)
  pyautogui.hotkey('ctrl', '1')

pyautogui.click(x=303, y=348)
