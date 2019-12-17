import  urllib.request

#向指定的URL发送请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen("http://www.baidu.com")


#读取响应的内容，会把读取到的数据赋值给一个字符串变量
#data = response.read()
#print(data)
#print(type(data))  #<class 'bytes'>

#把内容写入文件中
#with open(r"f:\workspace\Python\PythonTest\blibli2\爬虫\urllibtest.html","wb") as f:
#    f.write(data)


#读取一行
#data2 = response.readline()


#读取全部内容，会把读取到的数据赋值给一个列表变量；跟response.read()有差别
data3 = response.readlines()
print(data3)
print(type(data3)) #<class 'list'>
print(type(data3[2])) #<class 'bytes'>


#response 属性
#返回当前环境的有关信息
print(response.info())

#返回状态码
print(response.getcode())
if response.getcode() == 200 or response.getcode() == 304 :
    #处理网页信息
    pass

#返回当前正在爬取的URL地址
print(response.geturl())

#当url存在中文编码时
url = r""

#解码
newUrl = urllib.request.unquote(url)
print(newUrl)

#编码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)
