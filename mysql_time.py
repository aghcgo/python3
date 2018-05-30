import pymysql
import datetime
import time
 
# 打开数据库连接
db = pymysql.connect("localhost","root","zhg721019","TESTDB" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 

try:
	for i in range(10000):
		# SQL 插入语句
		dt=datetime.datetime.now()
		print(dt)
		sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME,TIME) VALUES ('%s', '%s', '%d', '%c', '%d','%s' )" %  ('Mac', 'Mohan', 20, 'M', 2000,dt)
		print(sql)
		# 执行sql语句
		cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
		print(i)
		time.sleep(1)
except:
	# 如果发生错误则回滚
	db.rollback()
	print(sql)
	print(i)
# 关闭数据库连接
db.close()
