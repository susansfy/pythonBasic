#coding:utf-8

import  tkinter
from tkinter import  ttk
import  os

class TreeFrame:
    def __init__(self,master,path):
        frame = tkinter.Frame(master)
        #frame.pack()
        frame.grid(row=0,column=0)

        self.tree = ttk.Treeview(frame)
        self.tree.pack()

        self.treeinsert(self.tree,path)

        # tree.insert("",0,"tree0",text=os.listdir(path)[0],values=("f0"))
        # tree.insert("", 1, "tree1", text=os.listdir(path)[1], values=("f1"))


    def treeinsert(self,tree,path):
        i = 0
        for dir in os.listdir(path):

            treef1 = self.tree.insert(tree, i, "treef%s" % i, text=dir, values=("F%s" % i))
            path1 = os.path.join(path, dir)
            print("help me:", path1)
            if os.path.isdir(path1):

                self.treeinsert(treef1,path1)
            i = i + 1






