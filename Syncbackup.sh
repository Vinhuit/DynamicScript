
    cd /headless/Desktop/backup
    rm -rf DynamicScript-master
    wget -O master.zip https://github.com/Vinhuit/DynamicScript/archive/master.zip
    unzip -o master.zip
    cp -rf DynamicScript-master/* ./
    SOURCE="/headless/.mozilla"
    SOURCE2="headless/.mozilla/."
    #BACKUP="gs://decisive-circle-176914.appspot.com/data/"
    DATE=$(date +%Y_%m_%d)

    DESTINATION="$NAME"".tar.gz"
    DESTINATION2="chrome.tar.gz"
    FULLBACKUP="$BACKUP/"$DESTINATION
    HITLEAP="$BACKUP/"$DESTINATION2
    #./gsutil/gsutil cp $FULLBACKUP /headless/Desktop/backup
    id=$(yes|drive view-files |  grep  $DESTINATION |sed 's/^.*,//')
    drive clone $id
    tar -xvzf $DESTINATION
    cp -rf $SOURCE2 $SOURCE
    cp -rf /headless/.mozilla/brave /headless/Desktop/backup
    cp -rf /headless/.mozilla/.config/BraveSoftware /headless/.config/
    find /headless/.mozilla/ -name "*.desktop" -exec cp {} ../ \;
    rm -rf /headless/Desktop/backup/brave/SingletonLock
    
    #./gsutil/gsutil cp $HITLEAP /headless/Desktop/backup
    #tar -xvzf $DESTINATION2
    #cp -rf $SOURCE2 $SOURCE
    # while sleep 600; do xdg-open /headless/Desktop/backup/firefox.desktop; done
    #while sleep 600; do xdg-open /headless/Desktop/backup/chromium-browser.desktop done
    #cd beepminer-0.6.1
    #export pool_address1=eu.sushipool.com:443
    #export wallet1='NQ56 JVMC 03YP S4DY NU9C 4VER JER8 EJY1 JX9U'
    #./miner --wallet-address="$wallet1" --pool=$pool_address1 --type=nano --architecture=sandybridge
    #cd ..
    echo "Done restore"
while true; do
    echo $DESTINATION
    cp /headless/Desktop/*.desktop $SOURCE
    cp -rf /headless/Desktop/backup/brave $SOURCE
    cp -rf /headless/.config/BraveSoftware $SOURCE    
    tar -zcvf $DESTINATION $SOURCE
    if [ -z "$SYNC" ]
    then
       #./gsutil/gsutil cp $DESTINATION $BACKUP
       drive rm --id $id
       drive add_remote --file $DESTINATION
    fi
    echo "Done Backup"
    pkill firefox
    #xdg-open /headless/Desktop/backup/firefox.desktop
    sleep 8
    ./RunAzure2.sh
    sleep $1
done
