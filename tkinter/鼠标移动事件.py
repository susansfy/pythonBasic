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
#<B1-Motion> 左键移动
#<B3-Motion> 右键移动
label1.bind("<B1-Motion>",func)

win.mainloop()