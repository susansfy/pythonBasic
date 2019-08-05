#coding:utf-8
'''
Created on 2019年7月18日
文本控件，用于显示多行文本
@author: susan
'''
import Tkinter



win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")
#创建滚动条
s = Tkinter.Scrollbar()

text = Tkinter.Text(win)
#side放到窗体的哪一侧， fill填充，Y是填充纵轴
s.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)
text.pack(side=Tkinter.LEFT,fill=Tkinter.Y)
#关联
s.config(command=text.yview)
text.config(yscrollcommand=s.set)


#将文本插入到文本框中
str = "hello"

text.insert(Tkinter.INSERT, str)

win.mainloop()