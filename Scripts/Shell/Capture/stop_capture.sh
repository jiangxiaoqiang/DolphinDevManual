#!/bin/bash

err() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2 >> /root/package/scripts/log/capture.log
}

err "Stop capture"
/root/package/scripts/kill_process.sh
