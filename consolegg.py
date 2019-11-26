import pyautogui
import os ,time, sys, requests

def AddDeviceApi(num,email,name):
	data1= {"device": email.rstrip(),"name":name,"isStart":"False"}
	data = json.dumps(data1)
	print(data)
	headers = {'content-type': 'application/json'}
	if int(num)>499:
		url="http://jsonserver01.herokuapp.com/newaccount/"+str(num)
	else:
		url="http://jsonserver01.herokuapp.com/temp/"+str(num)
	#url = 'http://xjsonserver01.herokuapp.com/temp/'+str(num)
	print(url)
	response = requests.put(url, data=data,headers=headers)
	return response
  
num=os.environ['NAME']
num=num[7:]

url="http://jsonserver01.herokuapp.com/temp/"+str(int(num))
mail=requests.get(url).json()

time.sleep(4)
pyautogui.click(x=505, y=595)
pyautogui.click(x=558, y=564)
pyautogui.typewrite(mail['mail'])
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('anhvinh12')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=656, y=786)
time.sleep(3)
pyautogui.click(x=271, y=666)
time.sleep(1)
pyautogui.click(x=339, y=741)
time.sleep(20)
pyautogui.press('f5')
time.sleep(1)
pyautogui.click(x=814, y=233)
time.sleep(1)
pyautogui.click(x=656, y=786)
time.sleep(3)
pyautogui.click(x=271, y=666)
time.sleep(1)
pyautogui.click(x=339, y=741)
time.sleep(20)
pyautogui.click(x=316, y=976)
time.sleep(2)
pyautogui.typewrite('wget https://raw.githubusercontent.com/Vinhuit/DynamicScript/master/googlessh.sh; ./googlessh.sh {0}\n'.format(num))
