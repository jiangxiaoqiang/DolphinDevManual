#!/usr/bin/python
# -*- coding: UTF-8 -*-

import protocolParseHandler

def parserInitial(messagestr):
    messageType=messagestr[2:6]

def handleDifferentMessage(messagestr):
    filteredMessage=messagestr.replace(':','')    
    if(len(filteredMessage)<12):
        print("没有消息长度小于12的，重填")
        return
    messageType=filteredMessage[2:6]
    #Convert to int32
    messageTypeToSwitch=int(messageType,16)
    handlers[messageTypeToSwitch](filteredMessage)

def parseLocationUpload(messagestr):
    print("地理位置上报信息")    
    protocolParseHandler.parseMessageHead(messagestr)
    protocolParseHandler.parseMessageBody(messagestr)

def parseAuthoration(messagestr):
    print("授权信息")

handlers = {
    512:lambda messagestr: parseLocationUpload(messagestr),
    1:parseAuthoration
}

