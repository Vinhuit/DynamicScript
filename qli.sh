wget https://github.com/Vinhuit/youtube-live/releases/download/test/qli-Client-1.7.9-Linux-x64.tar.gz
tar xvf qli-Client-1.7.9-Linux-x64.tar.gz
echo "{\"Settings\":{\"overwrites\":{\"AVX512\":false},\"baseUrl\": \"https://ai.diyschool.ch/\",\"amountOfThreads\": 2,\"alias\": \"ops$RANDOM\",\"accessToken\": \"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJJZCI6ImYwODllMDI5LTQ0OTEtNGY3Mi04MmM4LWYwZTM3ZDVjOTNmZSIsIk1pbmluZyI6IiIsIm5iZiI6MTcwMDM3OTM2OSwiZXhwIjoxNzMxOTE1MzY5LCJpYXQiOjE3MDAzNzkzNjksImlzcyI6Imh0dHBzOi8vcXViaWMubGkvIiwiYXVkIjoiaHR0cHM6Ly9xdWJpYy5saS8ifQ.y_XfrG-axVq868JSUqZpRRtgOSlWxrmaUn4a7zaE267oMJhVwcfUkfAt8X9qqeDSuAzfKFvBkK09UlATU9Nyzw\"}}" > appsettings.json;
chmod 777 qli*
./qli-Client | tee qli.log
