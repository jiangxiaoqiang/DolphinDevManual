#!/bin/bash

err() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2 >> /root/package/scripts/log/capture.log
}

currentTime='date +'%Y-%m-%d-%H-%M%S''
for processId in $(ps -ef|grep "tcpdump"|grep -v grep|cut -c 10-15); do
   if [ $processId != 1 ] 
      then   
      kill -9 $processId
      err $currentTime + " kill $processId success"
   fi
done
