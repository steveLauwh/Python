#!/usr/bin/env python3

# host = localhost
# database: example1
# user: root
# password: 123456
# table: students
# 向 students 表查询记录

import pymysql.cursors

# 打开数据库连接
connection = pymysql.connect(host = 'localhost',
					 user = 'root',
					 password = '123456',
					 db = 'example1',
					 charset = 'utf8mb4')

try:
	with connection.cursor() as cursor:
		sql = "SELECT * FROM students WHERE score > 70"
		cursor.execute(sql)
		result = cursor.fetchall()  #获取符合条件的多条数据
		for row in result:
			id = row[0]
			name = row[1]
			score = row[2]
			print('id = %d, name = %s, score = %d' % (id, name, score))
except Exception as e:	
	print("Error to select:", e)
finally:
	connection.close()
