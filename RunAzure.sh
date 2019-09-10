#!/bin/bash
pip3 install --upgrade pip --user
pip3 install requests python3-xlib pyautogui===0.9.39 --user
python3 -m pip install requests python3-xlib pyautogui===0.9.39 --user
rm -rf setup*
#run_3.sh
#python3 /headless/Desktop/backup/pygui.py
if [ -z "$FAH" ]
    then
      run_3.sh
    else
      FAHClient --user=8fek7tcbax69 --team=234980 --passkey=f11cf30f860040d0f11cf30f860040d0 --gpu=false --smp=true
    fi
#pkill -f F*
