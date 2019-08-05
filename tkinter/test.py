#coding:utf-8
'''
Created on 2019年7月18日

@author: susan
'''

import Tkinter

#创建主窗口
win = Tkinter.Tk()

#设置标题
win.title("title")

#设置大小和位置
win.geometry("400x400+200+20")

#label :标签控件可以显示文本
#win 父窗体  
#text 显示的文本内容
#bg 背景色
#fg 字体颜色
#font 字体大小和格式 font("黑色",20)
#width,height label的长、宽
#wraplength 指定text文本中多宽进行换行
#justify 设置换行后的对齐方式 "left"
#anchor 位置n e s w center、ne等等(北、东、南、西、居中)
label = Tkinter.Label(win,text = "this is the label",bg="pink",fg="red")
#显示出来
label.pack()

win.mainloop()