#从word文件读取的内容放到另一个文件中
import  win32com
import  win32com.client
#最稳定的读取文件

def readWordFileToOther(path,toPath):
    #调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)

    #将word的数据保存到另一个文件
    doc.SaveAs(toPath,2) #2表示txt文件
    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()

path = r"D:\workspace\Python\PythonTest\blibli2\file\test.docx"
toPath = r""
readWordFileToOther(path,toPath)

