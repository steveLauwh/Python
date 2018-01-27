#!/usr/bin/env python3

# host = localhost
# database: example1
# user: root
# password: 123456
# table: students
# 向 students 表删除记录

import pymysql.cursors

# 打开数据库连接
connection = pymysql.connect(host = 'localhost',
					 user = 'root',
					 password = '123456',
					 db = 'example1',
					 charset = 'utf8mb4')

try:
	# 查询操作
	with connection.cursor() as cursor:
		sql = "DELETE FROM students WHERE name = 'steve'"
		cursor.execute(sql)
		connection.commit()
		print('delete success')
except Exception as e:	
	print("Error to delete:", e)
finally:
	connection.close()
