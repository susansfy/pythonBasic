#pip install pyexcel,pyexcel-xls,xlrd,future,xlwt-future,pyexcel-io
#有序字典 ordereddict
'''
效果跟“返回整体xlsx数据”的结果一直
'''
from collections import  OrderedDict
#读取数据
from pyexcel_xls import  get_data

def readXlsAndXlsxFile(path):
    #创建有序的字典
    dic = OrderedDict()
    #抓取数据
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]

    return dic


path  = r""
dic = readXlsAndXlsxFile(path)

