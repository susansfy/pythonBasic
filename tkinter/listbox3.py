#coding:utf-8
import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#EXTENDED  可以使listbox支持shift和control
lb = Tkinter.Listbox(win,selectmode=Tkinter.EXTENDED)
lb.pack()

for item in ["good","nice","list2"]:
    #按顺序添加
    lb.insert(Tkinter.END,item)

#按住shift,可以实现连选
#按住control，可以实现多选

#滚动条
sc = Tkinter.Scrollbar(win)
sc.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=Tkinter.LEFT,fill=Tkinter.BOTH)
#额外给属性赋值
sc['command']=lb.yview


win.mainloop()