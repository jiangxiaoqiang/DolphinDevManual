#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import protocolParseService

root = Tk()
text = Text(root,width=100,height=10)
parseResultText=Text(root,width=100,height=20)

def protocolParserinstance():    
    var = StringVar()
    label = Label( root, textvariable=var, relief=RAISED,text="报文数据：" )
    var.set("报文的解析结果如下：")    
    button = Button(root,width=10,text="解析",command=buttonClick)
    text.insert(INSERT, "7e:02:00:00:3c:01:41:31:07:17:31:0f:e8:00:20:00:00:00:0c:00:c3:02:1a:04:b0:06:f2:ad:f0:00:2c:02:76:00:b9:16:07:08:00:01:00:01:04:00:00:30:5e:02:02:00:00:03:02:00:00:25:04:00:00:00:00:2b:04:00:00:00:00:30:01:15:31:01:13:f9:7e")
    text.pack()
    button.pack()
    label.pack()
    parseResultText.pack()
    root.mainloop()

def buttonClick():
    textcontent = text.get('1.0','end')
    protocolParseService.handleDifferentMessage(textcontent)
    
def showParseResult(resultMessage):
    parseResultText.insert(INSERT,resultMessage)

