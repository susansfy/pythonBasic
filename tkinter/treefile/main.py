#coding:utf-8
import  tkinter
import  treeframe
import fileframe
import  os

win = tkinter.Tk()
win.title("title")
win.geometry("600x400+200+20")

path = r'D:\learn\Python\codetest\onetest'
print("path:",os.path.basename(path))
print("listdir:",os.listdir(path))


treefrm = treeframe.TreeFrame(win,path)
#treefrm.grid(row=0,column=0)
filefrm = fileframe.FileFrame(win)
#filefrm.grid(row=0,column=1)

win.mainloop()