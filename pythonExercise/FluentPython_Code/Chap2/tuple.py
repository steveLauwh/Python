#!/usr/bin/env python3
# coding:utf-8

'''Chap 2
元组：不仅是不可变的列表，还可以用于没有字段名的记录。
'''
lax_corrdinates = (33.9425, -118.408056)

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
	print('%s/%s' %passport)

# “_” 占位符
for county, _ in traveler_ids:
	print(county)

