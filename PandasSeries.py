# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

from pandas import Series, DataFrame
import pandas as pd

if __name__ == '__main__':
	
	sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
	obj3 = Series(sdata)
	print(obj3)

	states = ['California', 'Ohio', 'Oregon', 'Texas']
	obj4 = Series(sdata, index = states)
	print(obj4)

	obj = Series({'A': 5, 'B': 3, 'C': 2})
	print(obj.values)
	print(obj.index)
	print(obj["A"])
	print(obj[[False, True, False]])
	print(obj[obj > 2])
	obj[obj > 2] = 100
	print(obj)
	obj["C"] = -100
	print(obj)

