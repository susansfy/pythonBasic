import pymysql

db = pymysql.connect("localhost","root","","foran")
#创建一个cursor对象
cursor = db.cursor()

sql = "insert into tablename(xx,xx)"

#执行sql语句
try:
    cursor.execute(sql)
    db.commit()
except:
    #失败的话回滚
    db.rollback()



#断开
cursor.close()
db.close()