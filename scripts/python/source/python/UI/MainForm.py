#!/usr/bin/python
# -*- coding: UTF-8 -*-


from Tkinter import *
import sys
#sys.path.append("D:\\OneDrive\\Document\\doc\\DolphinDev\\DolphinDevManual\\scripts\\python\\source\\python\\UI\\Widgets")
sys.path.append("./Widgets")
sys.path.append("./Tools/Protocol")
sys.path.append("./Widgets/Location")
import protocolParser
default_encoding = 'utf-8'
if sys.getdefaultencoding()!=default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def sshdownload():
    donothing()

def newform():
    protocolParser.protocolParserinstance()

def ivokeresolveddata():
    Source.Tools.Protocol.t808protocol.resolvedata()

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

toolmenu = Menu(menubar, tearoff=0)
toolmenu.add_command(label="sshdownload",command=sshdownload)
toolmenu.add_cascade(label="sshupload",command=donothing)
toolmenu.add_command(label="Protocol",command=newform)
menubar.add_cascade(label="Tool",menu=toolmenu)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
