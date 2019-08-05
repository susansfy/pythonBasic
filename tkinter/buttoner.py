#coding:utf-8
'''
Created on 2019年7月18日

@author: susan
'''

import Tkinter

def func():
    print("print this text")

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#创建按钮
#width,height 按钮长宽

button = Tkinter.Button(win,text="按钮",command=func)
button.pack()

button2 = Tkinter.Button(win,text="按钮",command=win.quit)
button2.pack()


win.mainloop()