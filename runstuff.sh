#! /bin/bash

pkill -f qli
sudo apt update -y
sudo apt install wine -y
wget https://github.com/Vinhuit/youtube-live/releases/download/test/qli-Client-1.7.51-Linux-x64.tar.gz
tar xvf qli-Client-1.7.5-Linux-x64.tar.gz
echo "{\"Settings\":{\"baseUrl\": \"https://ai.diyschool.ch/\",\"amountOfThreads\": 2,\"alias\": \"rhino$RANDOM\",\"accessToken\": \"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJJZCI6ImYwODllMDI5LTQ0OTEtNGY3Mi04MmM4LWYwZTM3ZDVjOTNmZSIsIk1pbmluZyI6IiIsIm5iZiI6MTcwMDM3OTM2OSwiZXhwIjoxNzMxOTE1MzY5LCJpYXQiOjE3MDAzNzkzNjksImlzcyI6Imh0dHBzOi8vcXViaWMubGkvIiwiYXVkIjoiaHR0cHM6Ly9xdWJpYy5saS8ifQ.y_XfrG-axVq868JSUqZpRRtgOSlWxrmaUn4a7zaE267oMJhVwcfUkfAt8X9qqeDSuAzfKFvBkK09UlATU9Nyzw\"}}" > appsettings.json;
chmod 777 qli*
./qli-Client
