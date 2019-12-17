import  re

def checkPhone(str):
    #15912120012
    pat = r"^1(([3578]\d)|(47))\d{8}$"
    res = re.match(pat,str)
    print(res)

