import pyautogui
import os ,time
import requests
def AddDeviceApi(num,email,name):
	data= {"device": email.rstrip(),"name":name,"isStart":"False"}
	#data = json.dumps(data1)
	headers = {'content-type': 'application/json'}
	url = 'http://xjsonserver01.herokuapp.com/temp/'+str(num)
	response = requests.put(url, data=data,headers=headers)
  return response

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
try:
  if len(mail['name'])>0:
    name=mail['name']
  else:
    name="Vinh"
except:
  name="Vinh"
AddDeviceApi(str(int(num)),mail['device'],name)
time.sleep(40)
pyautogui.click(x=591, y=527)
pyautogui.typewrite("\ngit clone https://github.com/Vinhuit/az \n")
pyautogui.typewrite("cd az;./loop.sh "+name+ " "+ mail['device']+ " "+ str(int(num))+"; exit \n")
time.sleep(10)
mail=requests.get(url).json()
while mail['isStart'].rstrip() == "False":
  pyautogui.click(x=509, y=313)
  time.sleep(30)
  pyautogui.click(x=591, y=527)
  pyautogui.typewrite("\ngit clone https://github.com/Vinhuit/az \n")
  pyautogui.typewrite("cd az;./loop.sh "+name+ " "+ mail['device']+ " "+ str(int(num))+"; exit \n")
  time.sleep(20)
  mail=requests.get(url).json()

