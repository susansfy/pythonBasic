#coding:utf-8
import tkinter
from tkinter import  ttk

win = tkinter.Tk()
win.title("title")
win.geometry("600x400+200+20")

#返回鼠标点击的坐标
def func(event):
    print(event.x,event.y)
button1 = tkinter.Button(win,text="leftmouse button")
#<Button-1>  鼠标左键
#<Button-3> 鼠标右键
#<Button-2> 鼠标中键
#具体看笔记截图
#bind 给控件绑定事件
button1.bind("<Button-1>",func)
button1.pack()

win.mainloop()