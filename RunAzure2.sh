#!/bin/bash
num=1
name=$(echo $NAME | cut -c8-)
num=${name##+(0)}
pip3 install --upgrade pip
pip3 install requests python3-xlib pyautogui===0.9.39
python3 -m pip install requests python3-xlib pyautogui===0.9.39 --user
url="http://jsonserver01.herokuapp.com/online/"$num
echo $url
user=$(curl $url | jq -r '.device')
link=$(curl $url | jq -r '.link')
echo $user
echo $link
firefox $link
#python3 /headless/Desktop/backup/pygui.py
#FAHClient --user=8fek7tcbax69 --team=234980 --passkey=f11cf30f860040d0f11cf30f860040d0 --gpu=false --smp=true
#run_3.sh
