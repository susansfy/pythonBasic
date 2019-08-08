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
#从外面进入控件时触发
label1.bind("<Enter>",func)
#从控件离开时触发
label1.bind("<Leave>",func)

win.mainloop()