
wget https://github.com/indigo-dc/udocker/releases/download/1.3.12/udocker-1.3.12.tar.gz
tar zxvf udocker-1.3.12.tar.gz
export PATH=`pwd`/udocker-1.3.12/udocker:$PATH
udocker-1.3.12/udocker/udocker pull caubequay00/qumine2
udocker-1.3.12/udocker/udocker run caubequay00/qumine2
