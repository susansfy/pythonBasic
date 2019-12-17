import urllib.request
import re

def movieCrawler(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    #读取全部内容，用read()
    HtmlStr = response.read()
    print(HtmlStr)

    pat = r"<div><strong>(.*?)</div> </div>"
    re_image = re.compile(pat)
    imageList = re_image.findall(HtmlStr)



#146集是例子

url = r"view-source:https://www.ijq.tv/yingshi/juqing/15139295573140_6.html"
url2 = r"https://www.ijq.tv/yingshi/juqing/15139295573140_6.html"
topath = ""
movieCrawler(url2)