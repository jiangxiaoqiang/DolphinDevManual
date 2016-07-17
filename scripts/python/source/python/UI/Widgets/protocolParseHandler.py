#!/usr/bin/python
# -*- coding: UTF-8 -*-

import protocolCommonData
import protocolParser

def parseMessageHead(str):
    headerParseResult="#####################BEGIN HRAD##########################"
    headerParseResult=headerParseResult+"\n消息类型："+protocolCommonData.getMessageType(str[2:6])
    #print("消息体属性："+str[6:8])
    #print("终端手机号："+str[8:14])
    headerParseResult=headerParseResult+"\n#####################END HEAD##########################"
    protocolParser.showParseResult(headerParseResult)

def parseMessageBody(str):
    print("####################BEGIN BODY###########################")
    print("消息体")
    print("####################END BODY##################################")





