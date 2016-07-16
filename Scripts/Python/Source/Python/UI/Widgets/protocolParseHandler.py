#!/usr/bin/python
# -*- coding: UTF-8 -*-

import protocolCommonData

def parseMessageHead(str):
    print("Handle message head")
    #print("#####################BEGIN HRAD##########################")
    print("消息头")
    print("消息类型："+protocolCommonData.getMessageType(str[2:6]))
    #print("消息体属性："+str[6:8])
    #print("终端手机号："+str[8:14])
    #print("#####################END HEAD##########################")

def parseMessageBody(str):
    print("####################BEGIN BODY###########################")
    print("消息体")
    print("####################END BODY##################################")





