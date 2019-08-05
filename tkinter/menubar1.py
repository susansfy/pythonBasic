#coding:utf-8
import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#菜单条
menubar = Tkinter.Menu(win)
win.config(menu=menubar)

def func():
    print("hello")

#创建一个菜单选项
menu1 = Tkinter.Menu(menubar,tearoff=False)
#菜单选项添加内容
#command一般是触发该控件的操作
for item in ["python","c","java","c++","退出"]:
    if item == "退出":
        #添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)

    else:
        menu1.add_command(label=item,command=func)

#向菜单条上添加一个菜单选项
menubar.add_cascade(label="语言",menu=menu1)

win.mainloop()