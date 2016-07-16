#!/usr/bin/python
# -*- coding: UTF-8 -*-

import protocolParseHandler

def parserInitial(str):
    messageType=str[2:6]

def handleDifferentMessage(str):
    if(len(str)<12):
        print("没有消息长度小于12的，重填")
        return
    messageType=str[2:6]
    #Convert to int32
    messageTypeToSwitch=int(messageType,16)
    #str(messageTypeToSwitch)
    print("messageType:{0}".format(messageTypeToSwitch))
    handlers[messageTypeToSwitch](str)

def parseLocationUpload(str):
    print("地理位置上报信息")
    print(str)
    protocolParseHandler.parseMessageHead(str)

def parseAuthoration(str):
    print("授权信息")

handlers = {
    512:lambda str: parseLocationUpload(str),
    1:parseAuthoration
}

