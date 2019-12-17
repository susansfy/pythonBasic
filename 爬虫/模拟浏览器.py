import urllib.request
import  random

url = r"http://www.baidu.com"

#模拟浏览器，带上请求头里的user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

#设置一个请求体
req  = urllib.request.Request(url,headers=headers)
#发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)

agentList = [
    "",
    "",
    ""
]

#从列表中随机取一个值
agentStr = random.choice(agentList)
req = urllib.request.Request(url)
#向请求体里添加了User-Agent
req.add_header("User-Agent",agentStr)

response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
