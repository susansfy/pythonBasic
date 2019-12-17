import  win32com
import  win32com.client

def makeppt(path):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    #增加一文件
    pptFile = ppt.Presentations.Add()
    #创建页，参数1是页数（从1开始），参数2是类型
    pag1 = pptFile.Slides.Add(1,1)
    #pag1.Shapes[0] 是创建第一页的标题
    t1 = pag1.Shapes[0].TextFrame.TextRange
    #在第一页写内容
    t1.Text = "hello，world"

    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()


path = r""
makeppt(path)