#!/usr/bin/env python3

# host = localhost
# database: example1
# user: root
# password: 123456
# table: students
# 向 students 表插入数据

import pymysql.cursors

# 打开数据库连接
connection = pymysql.connect(host = 'localhost',
					 user = 'root',
					 password = '123456',
					 db = 'example1',
					 charset = 'utf8mb4')

try:
	with connection.cursor() as cursor:
		# SQL 插入语句
		sql = "INSERT INTO students (name, score) VALUES ('steve', 99)"
		cursor.execute(sql)

	# 提交到数据库执行
	connection.commit()

	with connection.cursor() as cursor:
		sql = "SELECT id, name FROM students WHERE score=99"
		cursor.execute(sql)
		result = cursor.fetchone()  # 获取单条数据
		print(result)

finally:
	connection.close()
