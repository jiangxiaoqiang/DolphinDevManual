#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import protocolParseService

root = Tk()
text = Text(root,width=100)

def protocolParserinstance():
    print("aaaaa")    
    var = StringVar()
    label = Label( root, textvariable=var, relief=RAISED,text="报文数据：" )
    var.set("Hey!? How are you doing?")    
    button = Button(root,width=10,text="解析",command=buttonClick)
    text.insert(INSERT, "hj0200kk.....")
    button.pack()    
    text.pack()
    label.pack()
    root.mainloop()

def buttonClick():
    textcontent = text.get('1.0','end')
    print(textcontent)
    protocolParseService.handleDifferentMessage(textcontent)
    
