import csv
'''
读文件
'''

def readCsv(path):
    infoList = []
    with open(path,"r") as f:
        # 读出来的是个对象
        allFileInfo = csv.reader(f)
        for row in allFileInfo:
            #读取每一行数据，每一行是一个列表
            #print(row)
            infoList.append(row)
    return  infoList


path = r"c\tex.txt"

readCsv(path)