#coding:utf-8
import tkinter
from tkinter import  ttk

win = tkinter.Tk()
win.title("title")
win.geometry("600x400+200+20")

label1=tkinter.Label(win,text="good",bg="blue")
label2=tkinter.Label(win,text="nice",bg="red")
label3=tkinter.Label(win,text="cool",bg="pink")

label1.pack()

def func(event):
    print(event.x,event.y)
#ButtonRelease-1  释放鼠标左键
#ButtonRelease-3 释放鼠标右键
label1.bind("<ButtonRelease-1>",func)

win.mainloop()