#coding:utf-8
import tkinter
from tkinter import  ttk

win = tkinter.Tk()
win.title("title")
win.geometry("600x400+200+20")

label1=tkinter.Label(win,text="good",bg="blue")
label2=tkinter.Label(win,text="nice",bg="red")
label3=tkinter.Label(win,text="cool",bg="pink")

#设置焦点，小控件绑定key事件时，要有焦点才能响应key事件；win绑定的话就不需要
label1.focus_set()
label1.pack()

def func(event):
    print("event.char =",event.char)
    print("event.keycode =", event.keycode)
#Key 响应所有的按键；
label1.bind("<Key>",func)

win.mainloop()