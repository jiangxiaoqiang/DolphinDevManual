#!/usr/bin/python
# -*- coding: UTF-8 -*-


from Tkinter import *



def protocolParserinstance():
    print("aaaaa")
    root = Tk()
    var = StringVar()
    label = Label( root, textvariable=var, relief=RAISED,text="报文数据：" )
    var.set("Hey!? How are you doing?")
    text = Text(root,width=100)
    button = Button(root,width=10,text="解析",command=buttonClick)
    button.pack()    
    text.pack()
    label.pack()
    root.mainloop()

def buttonClick():
    print("click")
    textcontent = text.get('1.0','end')
    print(textconent)
    
