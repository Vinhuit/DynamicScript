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
num=os.environ['NAME']
num=num[3:]
if int(num)>499:
	url="http://xjsonserver01.herokuapp.com/rerunaccount/"+str(int(num))
	os.system("xdg-open /headless/Desktop/backup/firefox2.desktop")
	time.sleep(10)
else:
	url="http://xjsonserver01.herokuapp.com/temp/"+str(int(num))
pyautogui.click(x=136, y=645)
time.sleep(2)
pyautogui.click(x=146, y=618)
time.sleep(2)
pyautogui.click(x=427, y=426)
time.sleep(2)

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
pyautogui.typewrite("anhvinh12")
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
time.sleep(1)
pyautogui.click(x=131, y=601)
time.sleep(1)
pyautogui.click(x=733, y=517)
time.sleep(4)
pyautogui.click(x=566, y=689)
time.sleep(4)
pyautogui.click(x=544, y=692)
time.sleep(40)

os.system("xdg-open /headless/Desktop/backup/firefox3.desktop")
time.sleep(4)
pyautogui.click(x=733, y=517)
time.sleep(4)
pyautogui.click(x=96, y=302)
time.sleep(4)
pyautogui.click(x=96, y=338)
time.sleep(4)
pyautogui.click(x=727, y=521)
time.sleep(4)
pyautogui.click(x=96, y=302)
time.sleep(2)
pyautogui.click(x=96, y=338)
time.sleep(2)
pyautogui.click(x=797, y=613)
time.sleep(2)

pyautogui.click(x=508, y=203)
time.sleep(30)
pyautogui.click(x=797, y=613)
time.sleep(2)
pyautogui.click(x=661, y=512)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
pyautogui.click(x=664, y=528)
pyautogui.typewrite("azure"+str(num))
time.sleep(1)
pyautogui.click(x=858, y=525)
pyautogui.typewrite("azure"+str(num))
time.sleep(1)
pyautogui.click(x=603, y=591)
#pyautogui.click(x=777, y=593)
time.sleep(30)

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
		#profile
		time.sleep(1)
		#profile
		pyautogui.click(x=757, y=634)
		time.sleep(2)
		pyautogui.click(x=764, y=694)
		time.sleep(2)
		pyautogui.click(x=391, y=452)
		pyautogui.press('end')
		time.sleep(1)
		pyautogui.click(x=623, y=569)
		pyautogui.click(x=610, y=521)
		time.sleep(1)
		pyautogui.click(x=610, y=521)
		time.sleep(4)
		pyautogui.click(x=488, y=569)
		time.sleep(1)
		pyautogui.click(x=391, y=452)
		pyautogui.press('home')
		time.sleep(2)
		pyautogui.click(x=509, y=313)
		pyautogui.click(x=508, y=203)
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
	time.sleep(1300)
	pyautogui.click(x=695, y=612)
	time.sleep(20)
	pyautogui.click(x=591, y=527)
	pyautogui.typewrite("\nrm -rf az;git clone https://github.com/Vinhuit/az \n")
	pyautogui.typewrite("cd az;./loop.sh "+name+ " "+ mail['device']+ " "+ str(int(num))+"; exit \n")
	time.sleep(20)
	time.sleep(3700)
	print(AddDeviceApi(str(int(num)),mail['device'],name))
		
	
