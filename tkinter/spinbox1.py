#coding:utf-8
import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

'''
数值范围控件
'''
#increment 步长，默认是1，
sp = Tkinter.Spinbox(win,from_=0,to=100,increment=1)
#values  取值，一般不与from_,to,increment同时使用
#sp = Tkinter.Spinbox(win,values=(0,2,4,6,8))
sp.pack()

win.mainloop()