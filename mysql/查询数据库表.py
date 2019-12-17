'''
fetchone()
功能:获取下一个查询结果集，结果集是一个对象

fetchall()
加收全部的返回的行

rowcount:是一个只读属性，返回execute()方法影响的行数

'''

import pymysql

db = pymysql.connect("localhost","root","","foran")
#创建一个cursor对象
cursor = db.cursor()

sql = "select * from cource"

#执行sql语句
try:
    cursor.execute(sql)
    reslist = cursor.fetchall()
    print(reslist) #((1002, '英语'), (1001, '计算机'), (1003, '语文'))
    for row in reslist:
        print("%s--%s"%(row[0],row[1])) #1002--英语....
except:
    #失败的话回滚
    db.rollback()



#断开
cursor.close()
db.close()