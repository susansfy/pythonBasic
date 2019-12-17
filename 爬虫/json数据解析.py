'''
概念：一种保存数据的个数
作用：可以保存本地的json文件，也可以将json串进行传输，通常将json称为轻量级的传输方式

json文件组成
{} 代表对象（字典）
[] 代表列表
: 代表键值对
, 代表分隔两个部分
'''

import  json

jsonStr = '{"name":"susan","hobby":["num1","power"],"params":{"a":1,"b":2}}'

#将json格式的字符串转为python数据类型的对象
#loads(s,)
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData)) #dict
print(jsonData["hobby"])

#将python数据类型的对象转为json格式的字符串
jsonData2 = {"name":"susan","hobby":["num1","power"],"params":{"a":1,"b":2}}
jsonStr2 = json.dumps(jsonData2)
print(jsonStr2) #string

#读取本地的json文件
path1 = r""
with open(path1,"rb") as f:
    #load(fp,）,跟loads有区别
    data = json.load(f)
    print(data)

#写本地json
