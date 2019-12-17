import  win32com
import  win32com.client
#最稳定的读取文件

def readWordFile(path):
    #调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)
    for par in doc.Paragraphs:
        lin = par.Range.Text
        print(lin)
    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()

path = r"D:\workspace\Python\PythonTest\blibli2\file\test.docx"
readWordFile(path)

