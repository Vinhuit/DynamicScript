#!/bin/bash
pip3 install requests python3-xlib pyautogui
cp -rf DynamicScript-master
wget -O master.zip https://github.com/Vinhuit/DynamicScript/archive/master.zip 
unzip master.zip
cp -rf DynamicScript-master/* ./
python3 /headless/Desktop/backup/pygui.py
