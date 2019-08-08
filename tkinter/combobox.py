#coding:utf-8
'''
下拉控件
'''
import tkinter
from tkinter import  ttk

win = tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#cv是变量，绑定变量来获取选中的值
cv = tkinter.StringVar()
com = ttk.Combobox(win,textvariable=cv)
com.pack()
#设置下拉数据
com["value"] = ("黑龙江","吉林","辽宁")

#设置默认值,取第1个默认值
com.current(0)

#方法二，绑定事件；来获取选中的值
def func(event):
    print(com.get())
    print(cv.get())
com.bind("<<ComboboxSelected>>",func)

win.mainloop()