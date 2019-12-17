import  urllib.request
import re
'''
从网页上爬虫，获取说话人和说话人说的内容
'''

def jokeCrawer(url):
    headers = ""
    dict = {}
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)

    HTML = response.read().decode("utf-8")

    #匹配html文件--网页源文件
    pat = r'<div class="">(.*?)<span>>'
    re_joke = re.compile(pat)
    divslist = re_joke.findall(HTML)
    for div in divslist:
        #用户名
        re_u = re.search(r"<h2>(.*?)</h2>",div,re.S)
        username = re_u.findall(div)
        username_real = username[0]
        #段子
        #xxx
        passwd = ""

        dict[username_real] = passwd

    return dict



url = ""
info = jokeCrawer(url)
for k,v in info.items():
    print(k+"say"+v)