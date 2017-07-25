# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

if __name__ == '__main__':

	print('创建DataFrame, 通过字典、array或者列表等方式')
	data = {'year':[2000, 2001, 2002, 2001, 2002], \
	        'state':['Ohio', 'Ohio', 'Ohio', \
	                 'Nevada', 'Nevada'], \
	       'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
	frame = pd.DataFrame(data, columns=['year', \
	                    'state', 'pop', 'dept'])
	print(frame)
	print('查看DataFrame中元素的数据类型')
	print(frame.dtypes)
	print('查看前5条数据')
	print(frame.head())
	# 列名方式
	print(frame["pop"])
	# 索引名和列名方式
	print(frame.ix[:, "pop"])
	print("通过bool序列，筛选等于2001年的数据")
	print(frame.ix[frame["year"] == 2001, :])
	print('通过行和列号方式')
	print(frame.iloc[:2, :2])

	# 算术运算
	P1 = pd.DataFrame({"A": [1, 1], "B": [1, 1]}, index = [2, 3])
	P2 = pd.DataFrame({"A": [1, 1, 1], "B": [1, 1, 1], "C": [1, 1, 1]}, index = [1, 3, 5])
	print("P1 + P2", P1 + P2)

	# 保存数据到excel
	frame.to_csv("frame.txt")
	# header设置字段，将第0行作为字段。 index_col设置索引，第0列作为索引。
	pd.read_csv("frame.txt", header = 0, index_col = 0)

	# concat函数
	dates = pd.date_range("20130101", periods = 6)
	df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = list("ABCD"))
	print(df)
	# 行方向堆叠
	pd.concat([df.iloc[:2], df.iloc[2:4], df.iloc[5:7]], axis = 0)

	# merger函数
	adf = pd.DataFrame({'x1': ['A', 'B', 'C'], 'x2': [1, 2, 3]})
	bdf = pd.DataFrame({'x1': ['A', 'B', 'D'], 'x3': ['T', 'F', 'T']})
	pd_merge = pd.merge(adf, bdf, how = "left", on = "x1")
	print(pd_merge)

	# append函数
	df1 = pd.DataFrame(columns=['A', 'B', 'C', 'D'], index=[0,1,2,3])
	df1['A'] = ['A0', 'A1', 'A2', 'A3']
	df1['B'] = ['B0', 'B1', 'B2', 'B3']
	df1['C'] = ['C0', 'C1', 'C2', 'C3']
	df1['D'] = ['D0', 'D1', 'D2', 'D3']

	df2 = pd.DataFrame(columns=['A', 'B', 'C', 'D'], index=[4,5,6,7])
	df2['A'] = ['A4', 'A5', 'A6', 'A7']
	df2['B'] = ['B4', 'B5', 'B6', 'B7']
	df2['C'] = ['C4', 'C5', 'C6', 'C7']
	df2['D'] = ['D4', 'D5', 'D6', 'D7']

	df3 = df1.append(df2)
	print(df3)

	# 统计
	df4 = pd.DataFrame({"A": range(10), "B": range(10)})
	print(df4)
	df4["A"].value_counts()
	df3["A"].unique()
	df4_describe = df4.describe()
	print(df4_describe)
	df4.apply(sum, axis = 0)
	df4.applymap(lambda x : x * x)

	# DataFrame分组统计
	data = {'year':[2000, 2001, 2002, 2001, 2002, 2001, 2002, 2001, 2002], 
			'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
			'pop':[1.5, 1.7, 3.6, 2.4, 2.9, 8, 16, 24, 32]}
	frame = pd.DataFrame(data, columns = ["year", "state", "pop"])
	# 按年份和州分组，对pop字段的值求均值
	frame.groupby(["year", "state"]).mean()

