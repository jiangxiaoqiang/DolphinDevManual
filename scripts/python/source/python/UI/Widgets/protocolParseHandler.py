#!/usr/bin/python
# -*- coding: UTF-8 -*-

import protocolCommonData
import protocolParser
#import sys
#sys.path.append("./Location")
import LocationParserService

def parseMessageHead(str):
    headerParseResult="#####################BEGIN HRAD##########################"
    headerParseResult=headerParseResult+"\n消息类型："+protocolCommonData.getMessageType(str[2:6])
    headerParseResult=headerParseResult+"\n消息体属性:"+str[6:10]
    headerParseResult=headerParseResult+"\n终端手机号:"+str[10:22]
    headerParseResult=headerParseResult+"\n消息流水号："+str[22:26]
    headerParseResult=headerParseResult+"\n#####################END HEAD##########################"
    protocolParser.showParseResult(headerParseResult)

def parseMessageBody(str):
    bodyParseResult="####################BEGIN BODY###########################"    
    bodyParseResult=bodyParseResult+"####################END BODY##################################"
    protocolParser.showParseResult(bodyParseResult)





