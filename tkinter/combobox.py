#coding:utf-8
import Tkinter
from Tkinter import  ttk

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

com = ttk.Combobox(win)
com.pack()

win.mainloop()