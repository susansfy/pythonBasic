#pip install pyexcel,pyexcel-xls,xlrd,future,xlwt-future,pyexcel-io
#有序字典 ordereddict
from collections import  OrderedDict
#读取数据
from pyexcel_xls import  save_data

def makeExcelFile(path,data):
    dic = OrderedDict()
    for sheetName,sheetValue in data.items():
        d={}
        d[sheetName] = sheetValue
        #字典的update是什么功能？？？
        dic.update(d)

    save_data(path,dic)


path = r""
makeExcelFile(path,{"表1":[[1,2,3],[4,5,6],[7,8,9]],"表2":[[11,21,31],[42,52,62],[73,83,93]]})
