#!/usr/bin/env python3

# host = localhost
# database: example1
# user: root
# password: 123456
# 创建 students 表

import pymysql.cursors

# 打开数据库连接
connection = pymysql.connect(host = 'localhost',
					 user = 'root',
					 password = '123456',
					 db = 'example1')

try:
	# 上下文管理器
	with connection.cursor() as cursor:
		# 使用 execute() 方法执行 SQL 语句，如果表存在则删除
		cursor.execute('DROP TABLE IF EXISTS students')

		# 使用预处理语句创建表
		sql = """CREATE TABLE `students` (
				 `id` int(11) NOT NULL AUTO_INCREMENT,
				 `name` varchar(50) NOT NULL,
				 `score` int,
				 PRIMARY KEY (`id`)
				 ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1"""

		cursor.execute(sql)

		print('Create students success')
finally:
	connection.close()


