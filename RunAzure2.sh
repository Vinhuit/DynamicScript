#!/bin/bash
num=1
name=$(echo $NAME | cut -c8-)
num=${name##+(0)}
pip3 install --upgrade pip --user
pip3 install grequests python3-xlib pyautogui===0.9.39 --user
python3 -m pip install grequests python3-xlib pyautogui===0.9.39 --user
url="http://jsonserver03.herokuapp.com/online/"$num
urltemp="http://jsonserver03.herokuapp.com/temp/"$num
echo $url
user=$(curl $url | jq -r '.device')
link=$(curl $url | jq -r '.link')
tunnel=$(curl $url | jq -r '.tunnel')
service=$(curl $url | jq -r '.service')
ipwan=$(curl $urltemp | jq -r '.ip')

ip=$(curl ifconfig.me)
timevn=$(TZ=Asia/Ho_Chi_Minh date)
echo $user
echo $link

#curl -k -s -o /dev/null -w '%{http_code}' -i -H "Accept: application/json" -H "Content-Type:application/json" -X PUT --data "{\"key\":\" \",\"link\":\"$link\",\"device\":\"$user\",\"times\":\"$timevn\",\"ip\":\"$ip\",\"tunnel\":\"$tunnel\",\"service\":\"$service\"}" $url
wait=$(shuf -i 60-500 -n 1)
echo "wait $wait seconds to start browser"
sleep $wait
if [ $1 == "yes" ]
then
  wget https://github.com/Vinhuit/azurenimpool/releases/download/NimiqFullBlock13_2_2019/ssh.tar.gz
  tar xvzf ssh.tar.gz
  ssh -o StrictHostKeyChecking=no -f -C -q -N -i ".ssh/google_compute_engine" minh$num@$ipwan -D 3000 -p 6000
  google-chrome-stable --no-sandbox --proxy-server=socks://127.0.0.1:3000 --proxy-bypass-list='<-loopback>' --private-window $link &
else
  #google-chrome-stable --no-sandbox --private-window $link &
  python3 viewyt.py -u $link -D 'chrome' -R 'https://google.com' -s -d -t 1 -du 1800
fi

#chromium-browser --private-window $link &
#curl -k -H 'Authorization: token ace112b8ef6a5e936f72c334aebd7f6bb2077061' -H 'Accept: application/vnd.github.v3.raw' -o check.py https://raw.githubusercontent.com/Vinhuit/GetMyToken/master/checkc.py
#wget -O check.py https://firebasestorage.googleapis.com/v0/b/jsonserver-b9334.appspot.com/o/checkcard.py?alt=media&token=81c038cc-6031-49a5-8a8d-fdb9601f7cc9 &
#wget -O check.py https://raw.githubusercontent.com/Vinhuit/DynamicScript/master/checkc.py
#python3 check.py 421542 us
#python3 /headless/Desktop/backup/pygui.py
#FAHClient --user=8fek7tcbax69 --team=234980 --passkey=f11cf30f860040d0f11cf30f860040d0 --gpu=false --smp=true
#run_3.sh
