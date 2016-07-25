#!/usr/bin/python
# -*- coding: UTF-8 -*-

def parserLocationBody(str):
    bodyParseResult="省域 ID："+str[26:30]
    bodyParseResult=bodyParseResult+"\n市县域 ID:"+str[30:34]
    bodyParseResult=bodyParseResult+"\n制造商 ID:"+str[34:39]
    bodyParseResult=bodyParseResult+"\n终端型号:"+str[39:59]
    bodyParseResult=bodyParseResult+"\n终端 ID:"+str[59,66]
