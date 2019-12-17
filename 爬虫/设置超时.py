
import  urllib.request

#如果超过时间，就不要去爬了
#如果网页长时间没有响应，系统判断超时，无法爬取

for i in range(1,100):
    try:
        #timeout单位是秒
        response = urllib.request.urlopen("url",timeout=0.5)
        print(len(response.read().decode("utf-8")))
    except:
        print("请求超时，继续下一个爬取")

