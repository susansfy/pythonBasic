#coding:utf-8

import  tkinter
from tkinter import  ttk

class FileFrame:
    def __init__(self,master):
        frame = tkinter.Frame(master)
        #frame.pack()
        frame.grid(row=0,column=1)

        frm1 = tkinter.Frame(frame)
        tkinter.Label(frm1, text="左上", bg="pink").pack(side=tkinter.TOP)
        tkinter.Label(frm1, text="左下", bg="yellow").pack(side=tkinter.TOP)

        frm1.pack(side=tkinter.LEFT)

