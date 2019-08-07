#coding:utf-8
import tkinter

'''
框架控件
在屏幕上显示一个矩形区域，多作为容器控件
'''

win = tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

frm = tkinter.Frame(win)
frm.pack()

#left;
## tkinter.Frame(frm)的参数是frm时，表示在这个frm的左边
#tkinter.Frame(frm)的参数是win时，表示在这个窗口的左边
frm1 = tkinter.Frame(frm)
tkinter.Label(frm1,text="左上",bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm1,text="左下",bg="yellow").pack(side=tkinter.TOP)

frm1.pack(side=tkinter.LEFT)


win.mainloop()