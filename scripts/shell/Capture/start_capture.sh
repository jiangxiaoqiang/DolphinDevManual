#!/bin/bash
process_exists=false
currentTime=`date +'%Y%m%d%H%M%S'`

err() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2 >> /root/package/scripts/log/capture.log
}
err "Start run capture script..."
for processId in $(ps -ef|grep "tcpdump"|grep -v grep|cut -c 10-15); do	
    if [ $processId != 1 ] ;then
       process_exists=true
	err "tcpdump process aready exists,will not start capture process"
    fi
done
if [ "$process_exists" != true ] ;then
    nohup /root/package/scripts/capture.sh &
fi
