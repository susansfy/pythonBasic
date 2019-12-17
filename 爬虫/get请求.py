
'''

特点：把数据
优点：速度快
缺点：承载的数据小，不安全
'''

import  urllib.request

url = ""
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)  #字符串类型

#但实际上响应数据大多数是json格式的字符串
#json viwer软件，查看json的层次


