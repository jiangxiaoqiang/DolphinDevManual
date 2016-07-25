#!/usr/bin/python
# -*- coding: UTF-8 -*-

import protocolCommonData
import protocolParser
import protocolDefinition
#import sys
#sys.path.append("./Location")
import LocationParserService

def parseMessageHead(messageContent):
    headerParseResult="#####################BEGIN HRAD##########################"
    headerParseResult=headerParseResult+"\n消息类型："+protocolCommonData.getMessageType(messageContent[2:6])
    headerParseResult=headerParseResult+"\n消息体属性:"+messageContent[6:10]
    headerParseResult=headerParseResult+"\n终端手机号:"+messageContent[10:22]
    headerParseResult=headerParseResult+"\n消息流水号："+messageContent[22:26]
    headerParseResult=headerParseResult+"\n#####################END HEAD##########################"
    protocolParser.showParseResult(headerParseResult)

def parseMessageBody(messageContent):
    bodyParseResult="####################BEGIN BODY###########################"
    for singleDefinition in protocolDefinition.locationReport:
        startPosition = protocolDefinition.messagehead_length + singleDefinition[0]
        messagesublength=getMessageLength(singleDefinition[1])
        bodyParseResult=bodyParseResult+"\n"+ singleDefinition[1] +"：" + messageContent[startPosition:messagesublength]
    bodyParseResult=bodyParseResult+"####################END BODY##################################"
    protocolParser.showParseResult(bodyParseResult)





