import pyautogui
import os ,time
import requests, json
def AddDeviceApi(num,email,name):
	data1= {"device": email.rstrip(),"name":name,"isStart":"False"}
	data = json.dumps(data1)
	print(data)
	headers = {'content-type': 'application/json'}
	if int(num)>499:
		url="http://xjsonserver01.herokuapp.com/rerunaccount/"+str(num)
	else:
		url="http://xjsonserver01.herokuapp.com/temp/"+str(num)
	#url = 'http://xjsonserver01.herokuapp.com/temp/'+str(num)
	print(url)
	response = requests.put(url, data=data,headers=headers)
	return response

pyautogui.click(x=485, y=472)
time.sleep(2)
pyautogui.click(x=136, y=645)
time.sleep(2)
pyautogui.click(x=146, y=618)
time.sleep(2)
pyautogui.click(x=427, y=426)
time.sleep(2)
num=os.environ['NAME']
num=num[3:]
if int(num)>499:
	url="http://xjsonserver01.herokuapp.com/rerunaccount/"+str(int(num))
	os.system("xdg-open /headless/Desktop/backup/firefox2.desktop")
	time.sleep(10)
else:
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
time.sleep(1)
try:
	if len(mail['name'])>0:
		name=mail['name']
	else:
		name="Vinh"
except:
	name="Vinh"
print(AddDeviceApi(str(int(num)),mail['device'],name))
pyautogui.click(x=145, y=639)
time.sleep(40)
pyautogui.click(x=591, y=527)
pyautogui.typewrite("\nrm -rf az;git clone https://github.com/Vinhuit/az \n")
pyautogui.typewrite("cd az;./loop.sh "+name+ " "+ mail['device']+ " "+ str(int(num))+"; exit \n")
time.sleep(20)
mail=requests.get(url).json()
count=0
for i in range(10):
	while mail['isStart'].rstrip() == "False":
		pyautogui.click(x=145, y=639)
		time.sleep(1)
		pyautogui.press('home')
		time.sleep(3)
		pyautogui.click(x=145, y=639)
		time.sleep(1)
		pyautogui.click(x=127, y=614)
		time.sleep(2)
		pyautogui.click(x=552, y=699)
		time.sleep(2)
		pyautogui.click(x=510, y=588)
		time.sleep(2)
		pyautogui.click(x=493, y=557)
		time.sleep(1)
		pyautogui.click(x=509, y=313)
		time.sleep(30)
		mail=requests.get(url).json()
		pyautogui.click(x=591, y=527)
		pyautogui.typewrite("\nrm -rf az;git clone https://github.com/Vinhuit/az \n")
		pyautogui.typewrite("cd az;./loop.sh "+name+ " "+ mail['device']+ " "+ str(int(num))+"; exit \n")
		time.sleep(20)
		mail=requests.get(url).json()
		try:
			if mail["startAdHoc"] == "True":
				print(AddDeviceApi(str(int(num)),mail['device'],name))
				os.system("bash -c 'pkill -f bash'")
		except:
			pass
		count=count+1
		if count>10:
			count=0
			pyautogui.press('f5')
			time.sleep(11)
			pyautogui.click(x=145, y=639)
	time.sleep(7300)
	print(AddDeviceApi(str(int(num)),mail['device'],name))
		
	
