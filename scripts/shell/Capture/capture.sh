#!/bin/bash
currentDate=`date '+%Y-%m-%d'`
currentTime=`date +'%Y%m%d%H%M%S'`
packageStoreDir=/root/package/location/$currentDate
if [ ! -d "$packageStoreDir" ] ; then 
   mkdir "$packageStoreDir" 
fi
#tcpdump -i eth1 port 6973 and host 120.26.132.144 -w $packageStoreDir/$currentTime.cap
/usr/sbin/tcpdump -i eth1 port 6973 and host 10.6.12.14 -tttt -s0 -w $packageStoreDir/$currentTime.cap 
