wget https://github.com/Vinhuit/youtube-live/releases/download/test/qli-Client-1.7.9-Linux-x64.tar.gz
tar xvf qli-Client-1.7.9-Linux-x64.tar.gz
echo "{\"Settings\":{\"overwrites\":{\"AVX512\":false},\"baseUrl\": \"https://ai.diyschool.ch/\",\"amountOfThreads\": 2,\"alias\": \"ops$RANDOM\",\"accessToken\": \"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJJZCI6ImYwODllMDI5LTQ0OTEtNGY3Mi04MmM4LWYwZTM3ZDVjOTNmZSIsIk1pbmluZyI6IiIsIm5iZiI6MTcwODg3Mjc2MSwiZXhwIjoxNzQwNDA4NzYxLCJpYXQiOjE3MDg4NzI3NjEsImlzcyI6Imh0dHBzOi8vcXViaWMubGkvIiwiYXVkIjoiaHR0cHM6Ly9xdWJpYy5saS8ifQ.-WZpcgTJdsKk2wT_qKejPhfAY_SMF5CcT170ie8J9uxbN4q1JBUc1XrceuVgLXBLJfM9JSwoZnZe66N5kBFH_g\"}}" > appsettings.json;
chmod 777 qli*
./qli-Client | tee qli.log
