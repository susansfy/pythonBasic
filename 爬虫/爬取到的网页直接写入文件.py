import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",
                           filename=r"f:\workspace\Python\PythonTest\blibli2\爬虫\urllibtest2.html")

#urlretrieve在执行的过程中，会生成一些缓存

#清除缓存
urllib.request.urlcleanup()