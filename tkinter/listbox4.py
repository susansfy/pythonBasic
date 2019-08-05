#coding:utf-8
import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#MULTIPLE 支持多选
lb = Tkinter.Listbox(win,selectmode=Tkinter.MULTIPLE)
lb.pack()

for item in ["good","nice","list2"]:
    #按顺序添加
    lb.insert(Tkinter.END,item)

win.mainloop()