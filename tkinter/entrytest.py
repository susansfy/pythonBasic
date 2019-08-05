#coding:utf-8
'''
Created on 2019年7月18日

@author: susan
'''
import Tkinter



win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#绑定变量
e = Tkinter.Variable()

#输入控件
#用于显示简单的文本内容
#show 密文显示 show="*"
entry = Tkinter.Entry(win,textvariable=e)
entry.pack()

#e就代表输入框这个对象
#设置值
e.set("this is the value")
#取值
#赋值的时候不能用entry，取值的时候可以
print(e.get())
print(entry.get())

win.mainloop()