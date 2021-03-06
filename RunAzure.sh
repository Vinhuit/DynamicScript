#!/bin/bash

SOURCE="/headless/.mozilla"
SOURCE2="headless/.mozilla/."
    #BACKUP="gs://decisive-circle-176914.appspot.com/data/"
    DATE=$(date +%Y_%m_%d)

    DESTINATION="$NAME"".tar.gz"
    DESTINATION2="chrome.tar.gz"
    FULLBACKUP="$BACKUP/"$DESTINATION
    HITLEAP="$BACKUP/"$DESTINATION2
    if [ -z "$SYNC" ]
    then
       id=$(yes|drive view-files |  grep  $DESTINATION |sed 's/^.*,//')
       drive clone $id
       tar -xvzf $DESTINATION
       cp -rf $SOURCE2 $SOURCE
       cp -rf /headless/.mozilla/brave /headless/Desktop/backup
       cp -rf /headless/.mozilla/.config/BraveSoftware /headless/.config/
       find /headless/.mozilla/ -name "*.desktop" -exec cp {} ../ \;
       rm -rf /headless/Desktop/backup/brave/SingletonLock
       echo "Done restore"
    fi
    #./gsutil/gsutil cp $FULLBACKUP /headless/Desktop/backup
    
    
    
    #./gsutil/gsutil cp $HITLEAP /headless/Desktop/backup
    #tar -xvzf $DESTINATION2
    #cp -rf $SOURCE2 $SOURCE
    # while sleep 600; do xdg-open /headless/Desktop/backup/firefox.desktop; done
    #while sleep 600; do xdg-open /headless/Desktop/backup/chromium-browser.desktop done
    #cd beepminer-0.6.1
    #export pool_address1=eu.sushipool.com:443
    #export wallet1='NQ56 JVMC 03YP S4DY NU9C 4VER JER8 EJY1 JX9U'
    #./miner --wallet-address="$wallet1" --pool=$pool_address1 --type=nano --architecture=sandybridge
    #cd ..

    echo $DESTINATION
    cp /headless/Desktop/*.desktop $SOURCE
    cp -rf /headless/Desktop/backup/brave $SOURCE
    cp -rf /headless/.config/BraveSoftware $SOURCE    
    tar -zcvf $DESTINATION $SOURCE
    if [ -z "$SYNC" ]
    then
       #./gsutil/gsutil cp $DESTINATION $BACKUP
       drive rm --id $id
       drive add_remote --file $DESTINATION
    fi
    echo "Done Backup"

wget 'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=vi' -O firefox.tar.bz
tar xvf firefox.tar.bz
pip3 install --upgrade pip --user
pip3 install requests python3-xlib pyautogui===0.9.39 --user
python3 -m pip install grequests python3-xlib pyautogui===0.9.39 --user
rm -rf setup*
#setup ngrok tunnel
#wget https://github.com/Vinhuit/azurenimpool/releases/download/NimiqFullBlock13_2_2019/ngrok-stable-linux-amd64.zip
#unzip ngrok-stable-linux-amd64.zip
#./ngrok authtoken 3ppmqTtdMSjD8thesYxjW_5ZjrdxUqgMfQdq91BnXS8
#./ngrok tcp 22 &
num=1
name=$(echo $NAME | cut -c8-)
num=${name##+(0)}
server="http://jsonserver03.herokuapp.com"
url="http://jsonserver03.herokuapp.com/online/"$num
echo $url
tunnel=$(curl $url | jq -r '.tunnel')
user=$(curl $url | jq -r '.device')
link=$(curl $url | jq -r '.link')
service=$(curl $url | jq -r '.service')
ip=$(curl $url | jq -r '.ip')
ip=$(curl ifconfig.me)
timevn=$(TZ=Asia/Ho_Chi_Minh date)
echo "User: "$user
echo "Link: "$link
echo "Service: "$service
echo "Tunnel: "$tunnel
curl -k -s -o /dev/null -w '%{http_code}' -i -H "Accept: application/json" -H "Content-Type:application/json" -X PUT --data "{\"key\":\" \",\"link\":$link,\"device\":\"$user\",\"times\":\"$timevn\",\"ip\":\"$ip\",\"tunnel\":\"$tunnel\",\"service\":\"$service\"}" $url
google-chrome-stable --no-sandbox &
sleep 2
pkill -f google-chrome-stable &

if [ $tunnel == "yes" ]
then
    pkill -f python
    curl -sSL https://github.com/jpillora/chisel/releases/download/1.3.1/chisel_linux_amd64.gz | gzip -d - > /bin/chisel
    chmod +x /bin/chisel
    chisel server --port $PORT --auth rhino:rhino --socks5 --reverse &
    echo "Done Start Proxy Server"
fi
if [ $service == "ssh" ]
then
    chromium-browser --incognito "ssh.cloud.google.com" &
    sleep 3
    pkill -f chromium-browser
    pkill -f google-chrome-stable
    chromium-browser --incognito "ssh.cloud.google.com" &
    python3 consolegg.py $server
    
elif [ $service == "youtube" ]
then
    chmod u+x RunAzure2.sh
    ./RunAzure2.sh no
elif [ $service == "cpm" ]
then
    google-chrome-stable --no-sandbox --incognito "ssh.cloud.google.com" &
    sleep 3
    pkill -f chromium-browser
    pkill -f  google-chrome-stable
    google-chrome-stable --no-sandbox --incognito "ssh.cloud.google.com" &
    python3 consolegg.py $num
    #google-chrome --incognito $link &
    #sleep 10
    #python3 cpmclick.py
elif [ $service == "4k" ]
then
    google-chrome-stable --no-sandbox --incognito $link &
    sleep 20
else
    #google-chrome --incognito "ssh.cloud.google.com" &
    #python3 consolegg.py $num
    google-chrome-stable --no-sandbox --incognito $link &
    sleep 20
    python3 cpmclick.py
fi
#curl -k -H 'Authorization: token ace112b8ef6a5e936f72c334aebd7f6bb2077061' -H 'Accept: application/vnd.github.v3.raw' -o check.py https://raw.githubusercontent.com/Vinhuit/GetMyToken/master/checkc.py
#wget -O check.py https://firebasestorage.googleapis.com/v0/b/jsonserver-b9334.appspot.com/o/checkcard.py?alt=media&token=81c038cc-6031-49a5-8a8d-fdb9601f7cc9 &
#wget -O check.py https://raw.githubusercontent.com/Vinhuit/DynamicScript/master/checkc.py
#sleep 4
#python3 check.py 46701001249 us &
#sleep 2
#python3 check.py 46701001249 us &
#sleep 2
#python3 check.py 46701001249 us &
#sleep 2
#python3 check.py 421542 us &
#sleep 2
#python3 check.py 421542 us &
#sleep 2
echo "Done Restore"
while true;do
sleep 99999
done
#run3.sh
#python3 /headless/Desktop/backup/pygui.py
#if [ -z "$FAH" ]
#    then
      #FAHClient --user=8fek7tcbax69 --team=234980 --passkey=f11cf30f860040d0f11cf30f860040d0 --gpu=false --smp=true
#    else
      #run_3.sh
#    fi
#pkill -f F*
