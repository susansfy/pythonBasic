#from 封装 import

s = myOwnsql("localhost","root","","grade")
res = s.get_all("select * from pk")
for row in res:
    print(row[0],row[1])