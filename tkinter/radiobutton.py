#coding:utf-8
import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

#将value打印出来
def updata():
    print(r.get())

#一组单选框都要绑定变量r（variable=r），这样能实现单选；否则会多选
#r是int类型，所以value也应该是int类型，否则会报错
r = Tkinter.IntVar()
radio1 = Tkinter.Radiobutton(win,text="one",value=1,variable=r,command=updata)
radio1.pack()
radio2 = Tkinter.Radiobutton(win,text="two",value=2,variable=r,command=updata)
radio2.pack()


win.mainloop()