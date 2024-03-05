wget https://github.com/indigo-dc/udocker/releases/download/1.3.12/udocker-1.3.12.tar.gz -O udocker-1.3.12.tar.gz
wget https://github.com/Vinhuit/youtube-live/releases/download/test/appserver.py -O appserver.py
#python3 appserver.py &
#./static-web-server -p 8000 - . -z &
tar zxvf udocker-1.3.12.tar.gz
chmod 777 -R udocker-1.3.12
export PATH=`pwd`/udocker-1.3.12/udocker:$PATH
udocker-1.3.12/udocker/udocker --allow-root pull caubequay00/qumineproxy2
udocker-1.3.12/udocker/udocker --allow-root run caubequay00/qumineproxy2 | tee qli.log
