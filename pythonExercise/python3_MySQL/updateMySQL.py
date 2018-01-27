#!/usr/bin/env python3

# host = localhost
# database: example1
# user: root
# password: 123456
# table: students
# 向 students 表更新记录

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
		sql = "SELECT * FROM students WHERE score > 70"
		cursor.execute(sql)
		result = cursor.fetchall()
		for row in result:
			print(row)

	# 更新操作
	with connection.cursor() as cursor:
		sql = "UPDATE students SET score = score + 1 WHERE name = 'steve'"
		cursor.execute(sql)
		connection.commit()
		print('Update success')

except Exception as e:	
	print("Error to update:", e)
finally:
	connection.close()
