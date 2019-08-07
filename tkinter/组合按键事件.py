#coding:utf-8
import tkinter
from tkinter import  ttk

win = tkinter.Tk()
win.title("title")
win.geometry("600x400+200+20")



def func(event):
    print("event.char =",event.char)
    print("event.keycode =", event.keycode)
#直接响应
#Control-Alt-a
#shift-up
#control-p
win.bind("<Control-Alt-a>",func)

win.mainloop()