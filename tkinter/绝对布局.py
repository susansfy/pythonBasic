#coding:utf-8
import tkinter
from tkinter import  ttk

win = tkinter.Tk()
win.title("title")
win.geometry("600x400+200+20")

label1=tkinter.Label(win,text="good",bg="blue")
label2=tkinter.Label(win,text="nice",bg="red")
label3=tkinter.Label(win,text="cool",bg="pink")

#绝对布局
#特点：窗口的变化对位置没有影响，即窗口缩小、扩大，对位置还是不变
label1.place(x=10,y=10)
label2.place(x=100,y=10)
label3.place(x=10,y=100)

win.mainloop()