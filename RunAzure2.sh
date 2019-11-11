#!/bin/bash
num=1
name=$(echo $NAME | cut -c8-)
num=${name##+(0)}
pip3 install --upgrade pip --user
pip3 install grequests python3-xlib pyautogui===0.9.39 --user
python3 -m pip install grequests python3-xlib pyautogui===0.9.39 --user
url="http://jsonserver01.herokuapp.com/online/"$num
echo $url
user=$(curl $url | jq -r '.device')
link=$(curl $url | jq -r '.link')
tunnel=$(curl $url | jq -r '.tunnel')
service=$(curl $url | jq -r '.service')
ip=$(curl ifconfig.me)
timevn=$(TZ=Asia/Ho_Chi_Minh date)
echo $user
echo $link

#curl -k -s -o /dev/null -w '%{http_code}' -i -H "Accept: application/json" -H "Content-Type:application/json" -X PUT --data "{\"key\":\" \",\"link\":\"$link\",\"device\":\"$user\",\"times\":\"$timevn\",\"ip\":\"$ip\",\"tunnel\":\"$tunnel\",\"service\":\"$service\"}" $url
wait=$(shuf -i 60-500 -n 1)
sleep $wait
firefox $link &
#curl -k -H 'Authorization: token ace112b8ef6a5e936f72c334aebd7f6bb2077061' -H 'Accept: application/vnd.github.v3.raw' -o check.py https://raw.githubusercontent.com/Vinhuit/GetMyToken/master/checkc.py
#wget -O check.py https://firebasestorage.googleapis.com/v0/b/jsonserver-b9334.appspot.com/o/checkcard.py?alt=media&token=81c038cc-6031-49a5-8a8d-fdb9601f7cc9 &
#wget -O check.py https://raw.githubusercontent.com/Vinhuit/DynamicScript/master/checkc.py
#python3 check.py 421542 us
#python3 /headless/Desktop/backup/pygui.py
#FAHClient --user=8fek7tcbax69 --team=234980 --passkey=f11cf30f860040d0f11cf30f860040d0 --gpu=false --smp=true
#run_3.sh
