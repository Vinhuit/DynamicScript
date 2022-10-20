#!/bin/bash
sudo apt update
#https://nimchain121.moviescloud.repl.co
sudo apt install unzip wget jq screen -y
ip=`curl ifconfig.me`
if [ -z $5 ]
  then
   entry=1
  else
    entry=$5
fi
version=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .version| cut -d '"' -f 2`
acc=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .name| cut -d '"' -f 2`
echo $version > version.txt

if pgrep -x "rclone" > /dev/null
then
          echo FoundRclone
          sleep 1
else
  if ! [[ -f ./rclone ]]
  then
  curl https://rclone.org/install.sh | sudo bash
  wget https://downloads.rclone.org/v1.59.1/rclone-v1.59.1-linux-amd64.zip -O rclone-v1.59.1-linux-amd64.zip
  unzip -o rclone-v1.59.1-linux-amd64.zip
  cp -rf rclone-v1.59.1-linux-amd64/rclone ./
  chmod 777 ./rclone
  fi
fi

mkdir -p ~/.config/rclone/ 
wget https://gitlab.com/tan37/tan/-/raw/main/rclone.conf?inline=false -O rclone.conf
wget https://gitlab.com/tan37/tan/-/raw/main/rclone.conf?inline=false -O ~/.config/rclone/rclone.conf

drivers=$acc"_"$3

if pgrep -x "chia_plot" > /dev/null
then
          echo FoundChia_plot
          sleep 1
else
        wget https://gitlab.com/tan37/tan/-/raw/main/chia_plot?inline=false -O ./chia_plot
        chmod 777 ./chia_plot 
        nohup ./chia_plot -r $2 -n -1 -t ./ -d ./ -c xch1t750ggens3f8j2fjf355ml0ylez78jy4wm35n3f78zsfvzxk0jcq5jpjxs -f 8d6e20cc99bd3d27fc9dc66a5fa5e0bbad9a16e067faf6683039f6383dc27f158a2d05184a6e3559f306882019841ce3 | tee output.txt &
fi 
for session in $(screen -ls | grep -o '[0-9]*\.monitor'); do screen -S "${session}" -X quit; done
screen -S "monitor" -d -m
screen -r "monitor" -X stuff $"curl https://gitlab.com/tan37/tan/-/raw/main/monitor.sh | bash -s 23200 $entry $acc;\n"
echo $drivers > drivers.txt
if [ -z $4 ]
  then
   numplot=3
  else
    numplot=$4
fi

echo $numplot > numplot.txt
start=1
current=$3
count=0
newstart=$3
loops=0
while true;
 do
  
       numrclone=`pgrep "rclone" | wc -l`       
       drivers=`cat drivers.txt`
       numplot=`cat numplot.txt`
       nversion=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .version| cut -d '"' -f 2`
       newstart=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .latest`
      #  if [[ ${nversion//.} -eq "null" ]]
      #  then
      #       nversion=`cat version.txt`
      #       newstart=$3
      #       echo "NotFountServer"
      #  fi
       
        version=`cat version.txt`
        echo "New_version:" $nversion
        echo "Current_version:" $version
        echo "Current_init: "$newstart
        echo "Current_driver: "$current
       # drivers=$1"_"$newstart
        if ! [[ ${nversion//.} -eq ${version//.} ]]
        then         
          sleep ${RANDOM:0:2}
          newstart=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .latest`
          acc=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .name| cut -d '"' -f 2`
          curl https://gitlab.com/tan37/tan/-/raw/main/upload2rclone.sh | bash -s $acc 5 $newstart $numplot $entry &        
          echo "NewVersionUpdated"
          echo $nversion > version.txt
          exit 0
        fi
      
     
       grep -rl "Failed" ./*.txt | grep -oE "plot-.*.plot" |xargs -i bash -c "mv ../{}/{} ./ && rm -rf {}*.txt && rm -rf ../{}"
       currentplot=`ls *.plot  | wc -l`
       if [[ $numrclone -lt $numplot && $currentplot -gt 0 ]]; then
           echo "Start copy."
           
           ./rclone size $drivers: --json
           if [[ $? -gt 0 ]]  
            then 
                newstart=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .latest`
             
                current=$newstart
                echo "Start current2"   
                drivers=$acc"_"$current        
           fi
           numsize=`./rclone size $drivers: --json | jq .count`                      
           currentcp=`./rclone size --max-size 1M $drivers: --json | jq .count`
           isfull=0
          while [[ $numsize -gt 48 || $currentcp -gt 2 ]]
          do
            while [[ $numsize -gt 48 ]]
            do 
              isfull=1     
             ./rclone size $drivers: --json
             if [[ $? -gt 0 ]]  
             then                 
                current=$newstart
                echo "Start current2"
                
             else
                newstart=$current
                current=$(($current+1))  
                 echo "StartContinue1"                 
             fi
              
              drivers=$acc"_"$current
              echo $drivers > drivers.txt
              numsize=`./rclone size $drivers: --json | jq .count`  
              echo "NewDriver1:"$drivers
              sleep 2
            done
            
              currentcp=`./rclone size --max-size 1M $drivers: --json | jq .count`
              if [[ $currentcp -gt 2 ]]
              then
                while [[ $currentcp -gt 2 ]]
                do                          
                ./rclone size $drivers: --json
                if [[ $? -gt 0 ]]  
                then 
                    current=$newstart
                    echo "Error"
                else
                    if [[ $isfull -eq 0 && $count -gt 20 ]]
                    then
                      current=$newstart
                      echo "Startnew"
                      count=0
                    else
                      current=$(($current+1))    
                      echo "StartContinue2"                  
                    fi
                fi
                    drivers=$acc"_"$current
                    echo $drivers > drivers.txt
                    currentcp=`./rclone size --max-size 1M $drivers: --json | jq .count`
                    echo "NewDriver2:"$drivers
                    echo "Current:" $newstart
                    echo "Lopp: "$count
                    loops=$(($loops+1))
                    sleep 2
                    if [[ $loops -gt 20 ]]
                    then
                      newstart=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .latest`
                      acc=`curl https://jsonserver-1.moviescloud.repl.co/other/$entry | jq .name| cut -d '"' -f 2`
                      sleep ${RANDOM:0:2}
                      curl https://gitlab.com/tan37/tan/-/raw/main/upload2rclone.sh | bash -s $acc 5 $newstart $numplot $entry &        
                      echo UpdatedLoop
                      exit 0
                    fi
                    curl https://gitlab.com/tan37/tan/-/raw/main/error2.sh | bash -s 23234
                done
              fi
              
              if [[ $current -eq $newstart ]]
              then
                count=$(($count+1))
                echo "Loop"$count
                
              else
                count=0
                loops=0
              fi
          done
          loops=0  
          count=0
           ls *.plot | head -1 | xargs -i bash -c 'mkdir -p ../{} && mv {} ../{} && touch {}.$2.txt && ./rclone copy  --log-file={}.$2.txt --ignore-size --ignore-checksum --no-traverse -P {}.$2.txt $1: && ./rclone copy  --log-file={}.$2.txt --ignore-size --ignore-checksum --no-traverse -P ../{}/{} $1: && ./rclone deletefile $1:{}.$2.txt || ./rclone deletefile $1:{}.$2.txt && rm -rf ../{} | tee ../{}.$2.txt & ' -s $drivers $ip
       
       else
           echo "Plot not found $count"           
       fi
      space=`df --output=avail ./ | tail -n1`
      if [[ $space -lt 111812352 ]]; then
        kill -9 `pidof chia_plot`
        rm -rf *.tmp
        start=0
      else
        if [[ $start -eq 0 ]]; then
        start=1
        nohup ./chia_plot -r $2 -n -1 -t ./ -d ./ -c xch1t750ggens3f8j2fjf355ml0ylez78jy4wm35n3f78zsfvzxk0jcq5jpjxs -f 8d6e20cc99bd3d27fc9dc66a5fa5e0bbad9a16e067faf6683039f6383dc27f158a2d05184a6e3559f306882019841ce3 | tee output.txt &
        fi
        echo "Nothing"
      fi
echo "Finding Plot..."

wget https://gitlab.com/tan37/tan/-/raw/main/rclone.conf?inline=false -O ~/.config/rclone/rclone.conf
wget https://gitlab.com/tan37/tan/-/raw/main/rclone.conf?inline=false -O rclone.conf
curl https://gitlab.com/tan37/tan/-/raw/main/error.sh | bash -s 23234
sleep 300
 done
