wget https://github.com/indigo-dc/udocker/releases/download/1.3.12/udocker-1.3.12.tar.gz
wget https://github.com/Vinhuit/youtube-live/releases/download/test/appserver.py
python3 appserver.py &
tar zxvf udocker-1.3.12.tar.gz
export PATH=`pwd`/udocker-1.3.12/udocker:$PATH
udocker-1.3.12/udocker/udocker --allow-root pull caubequay00/qumine2
udocker-1.3.12/udocker/udocker --allow-root run caubequay00/qumine2
