import  urllib.request
import ssl
import json

def ajaxCrawler(url):
    headers = {}
    req = urllib.request.Request(url,headers=headers)
    #使用ssl创建未验证的上下文--即访问https请求
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)

    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData


url = ""
info = ajaxCrawler(url)
print(info)