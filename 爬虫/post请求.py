'''
把参数进行打包，单独传输
'''

import urllib.request
#对参数进行打包，需要引用下面的包
import urllib.parse

url = r""
#将要发送的数据合成一个字典
#
data = {
    "usrname":"susan",
    "passwd":"555"
}

#对要发送的数据进行打包,data支持的格式是bytes,所以要转换为str
postData = urllib.parse.urlencode(data).encode("utf-8")

#请求体
req = urllib.request.Request(url,data=postData)
#请求
req.add_header("user-agent","")

responst = urllib.request.urlopen(req)
#print(responst.data().decode("utf-8"))