#coding:utf-8
import tkinter
from tkinter import  ttk

win = tkinter.Tk()

win.title("title")
win.geometry("600x400+200+20")

'''
表格数据
'''
#表格
tree = ttk.Treeview(win)
tree.pack()
#定义列
tree["columns"] = ("姓名","年龄","身高","体重")
#设置列
tree.column("姓名",width=100)
tree.column("年龄",width=100)
tree.column("身高",width=100)
tree.column("体重",width=100)
#设置表头，设置了这个，表格上面才会显示名称text；
#第一个参数要和设置列的第一个参数对应相等
tree.heading("姓名",text="姓名-name")
tree.heading("年龄",text="年龄-name")
tree.heading("身高",text="身高-name")
tree.heading("体重",text="体重-name")

#添加数据
#第二个参数是插入第几行，行数从第0行开始
tree.insert("",0,text="line1",values=("susan","28","160","94"))
tree.insert("",1,text="line1",values=("jane","25","150","95"))

win.mainloop()