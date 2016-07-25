#!/usr/bin/python
# -*- coding: UTF-8 -*-

messageTypeDic={
    '0200':'位置信息上报',
    '8606':'路线信息下发'
}

def getMessageType(messageTypeKey):
    return messageTypeDic[messageTypeKey]

def getMessageLength(contentType):
    messageLengthType[contentType]()

messageLengthType = {
    "DWORD":4,
    "WORD":2    
}