import pyautogui
import os ,time

def AddDeviceApi(num,email,name):
	data1= {"device": email.rstrip(),"name":name,"isStart":"False"}
	data = json.dumps(data1)
	print(data)
	headers = {'content-type': 'application/json'}
	if int(num)>499:
		url="http://xjsonserver01.herokuapp.com/newaccount/"+str(num)
	else:
		url="http://xjsonserver01.herokuapp.com/temp/"+str(num)
	#url = 'http://xjsonserver01.herokuapp.com/temp/'+str(num)
	print(url)
	response = requests.put(url, data=data,headers=headers)
	return response
  
num=os.environ['NAME']
num=num[3:]

url="http://xjsonserver01.herokuapp.com/temp/"+str(int(num))
mail=requests.get(url).json()


pyautogui.click(x=505, y=595)
pyautogui.typewrite(mail['device'])
time.sleep(2)
pyautogui.press('enter')
pyautogui.typewrite('anhvinh12')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=656, y=786)
time.sleep(3)
pyautogui.click(x=271, y=666)
time.sleep(1)
pyautogui.click(x=339, y=741)
time.sleep(10)
pyautogui.click(x=316, y=976)
pyautogui.typewrite('wget https://github.com/Vinhuit/azurenimpool/releases/download/NimiqFullBlock13_2_2019/googlessh.sh \n')
