import pyautogui
import os ,time
import requests
pyautogui.click(x=485, y=472)
time.sleep(2)
pyautogui.click(x=146, y=618)
time.sleep(2)
pyautogui.click(x=427, y=426)
time.sleep(2)
num=os.environ['NAME']
num=num[3:]
url="http://xjsonserver01.herokuapp.com/temp/"+str(int(num))
mail=requests.get(url).json()
pyautogui.click(x=419, y=411)
time.sleep(2)
pyautogui.typewrite(mail['device'])
pyautogui.click(x=593, y=564)
time.sleep(3)
pyautogui.click(x=409, y=487)
time.sleep(3)
pyautogui.click(x=370, y=447)
time.sleep(2)
pyautogui.typewrite("Anhvinh12@#")
pyautogui.click(x=593, y=564)
time.sleep(6)
pyautogui.click(x=485, y=573)
time.sleep(10)
pyautogui.click(x=485, y=573)
time.sleep(10)
pyautogui.click(x=490, y=560)
time.sleep(10)
pyautogui.click(x=490, y=560)
time.sleep(10)
pyautogui.click(x=490, y=560)
time.sleep(10)
pyautogui.click(x=485, y=552)
time.sleep(40)
pyautogui.click(x=591, y=527)
pyautogui.typewrite("git clone https://github.com/Vinhuit/az \n")
pyautogui.typewrite("cd az;./loop.sh \n")


