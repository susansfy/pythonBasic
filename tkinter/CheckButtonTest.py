#coding:utf-8
'''
Created on 2019年7月19日
复选框
@author: susan
'''

import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

def updata():
    message=""
    if value1.get() == True:
        message +="money\n"
    if value2.get() == True:
        message +="power\n"
    if value3.get() == True:
        message +="people\n"
    
    #清除text中的所有内容
    text.delete(0.0, Tkinter.END)
    text.insert(Tkinter.INSERT, message)

value1 = Tkinter.BooleanVar()
check1 = Tkinter.Checkbutton(win,text="money",variable=value1,command=updata)
check1.pack()
value2 = Tkinter.BooleanVar()
check2 = Tkinter.Checkbutton(win,text="power",variable=value2,command=updata)
check2.pack()
value3 = Tkinter.BooleanVar()
check3 = Tkinter.Checkbutton(win,text="people",variable=value3,command=updata)
check3.pack()

text = Tkinter.Text(win)
text.pack()

win.mainloop()