#coding:utf-8
'''
Created on 2019年7月18日
点击按钮，显示输入框中的内容
@author: susan
'''

import Tkinter

def func():
    print(entry.get())

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

entry = Tkinter.Entry(win)
entry.pack()

button = Tkinter.Button(win,text="按钮",command=func)
button.pack()

win.mainloop()