#coding:utf-8
import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#菜单条
menubar = Tkinter.Menu(win)

#菜单
menu1 = Tkinter.Menu(menubar,tearoff=False)
#菜单选项添加内容
#command一般是触发该控件的操作
for item in ["python","c","java","c++","退出"]:
    menu1.add_command(label=item)

#向菜单条上添加一个菜单选项
menubar.add_cascade(label="语言",menu=menu1)

def showMenu(event):
    menubar.post(event.x_root,event.y_root)
win.bind("<Button-3>",showMenu)

win.mainloop()