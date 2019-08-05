#coding:utf-8
import Tkinter

win = Tkinter.Tk()

win.title("title")
win.geometry("400x400+200+20")

'''
供用户通过拖拽指示器改变变量的值，可以水平，可以竖直4
'''
#HORIZONTAL 水平
#VERTICAL 竖直，默认值是竖直
#length 水平时表示宽度，竖直时表示高度
#tickinterval 选择值将会为该值的倍数
scale1 = Tkinter.Scale(win,from_=0,to=100,orient=Tkinter.HORIZONTAL,tickinterval=10,length=200)
scale1.pack()



win.mainloop()