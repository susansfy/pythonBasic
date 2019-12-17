'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个process类来代表一个进程对象

父子进程的先后顺序：
1、父进程的结束不会影响子进程
2、让父进程等待子进程结束再执行父进程

全局变量在多个进程中不能共享：
1、在子进程中修改全局变量对父进程中的全局变量没有影响
2、在创建子进程时，全局变量做了一个备份，父进程中的与子进程中的变量是完全不同的两个变量

'''

from multiprocessing import Process
from time import sleep
import os

def run(str):
    while True:
        #os.getpid()获取当前进程id号
        #os.getppid()获取当前进程的父进程id号
        print("%s day--%s--%s"%(str,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__=='__main__':
    print("主（父）进程启动")
    #创建子进程
    #target说明进程执行的任务；是把函数名赋值，而不是函数，所以用run---这里要学习下
    #args传参数，如果只有一个参数，则后面要有个逗号

    p = Process(target=run,args=("nice",))
    #启动进程
    p.start()

    #父进程会继续执行到下面，子进程会跳转到run()中执行
    while True:
        print("a good day")
        sleep(2)


