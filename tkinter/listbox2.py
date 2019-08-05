#coding:utf-8
import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#绑定变量
lbv = Tkinter.StringVar()
#与BORWSE相似，但是不支持鼠标按下后移动选中位置
lb = Tkinter.Listbox(win,selectmode=Tkinter.SINGLE,listvariable=lbv)
lb.pack()

for item in ["good","nice","list2"]:
    #按顺序添加
    lb.insert(Tkinter.END,item)

#打印当前列表中的选项
print(lbv.get())

#设置选项，重置选项
#lbv.set(("1","2","3"))

#绑定事件,这里需要事件参数event，但是不用传
def myPrint(event):
    print(lb.curselection())

lb.bind("<Double-Button-1>",myPrint)

win.mainloop()