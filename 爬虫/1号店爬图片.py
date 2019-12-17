import urllib.request
import re

def imageCrawler(url,topath):
    headers = {}
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    #读取全部内容，用read()
    HtmlStr = response.read()
    #把网页源码存到文件中
    with open(r"htmlpath","wb") as f:
        f.write(HtmlStr)

    pat = r""
    re_image = re.compile(pat,re.S)
    imageList = re_image.findall(HtmlStr)



#146集是例子

url = ""
topath = ""
imageCrawler(url,topath)