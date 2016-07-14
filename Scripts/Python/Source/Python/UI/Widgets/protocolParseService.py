#!/usr/bin/python
# -*- coding: UTF-8 -*-

def parserInitial(str):
    messageType=str[2:6]

def handleDifferentMessage(str):
    messageType=str[3:2]
    #print(messageType)
    handlers[2]()

def parseLocationUpload():
    print("地理位置上报信息")    

def parseAuthoration(str):
    print("授权信息")

handlers = {
    2:parseLocationUpload,
    1:parseAuthoration
}

