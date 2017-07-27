# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

if __name__ == '__main__':
	
	#
	# Load data
	# 
	# user_pay_csv = './user_pay_new.csv'
	shop_pay_csv = './shop_payNum_new.csv'
	# read_csv
	reader = pd.read_csv(shop_pay_csv, iterator = True, header = None, 
			names = ['time_stamp', 'shop_id', 'pay_num', 'cate_2_name'])

	data = pd.read_csv(shop_pay_csv)
	# sum = 0
	# for i in range(len(data)):
	# 	sum += data['pay_num'][i]	
	# print(sum)

	chunk_size = 100000
	chunks = []
	loop = True	
	while loop:
		try:
			# get_chunk
			chunk = reader.get_chunk(chunk_size)
			chunks.append(chunk)
		except StopIteration:
			loop = False
			print("Iteration is stopped")
	full_data = pd.concat(chunks, ignore_index = True)
	print(full_data)
	#
	# Group DataFrame
	#
	size = 100000
	i = 0
	flow = []
	while (i < full_data.shape[0]):
		data_i = full_data[i : i + size]
		if i == 0:
			flow = data_i.groupby(['shop_id', 'time_stamp']).count().reset_index()
		else:
			flow = flow.append(data_i.groupby(['shop_id', 'time_stamp']).count().reset_index(), ignore_index = True)
		i = i + size
	print(flow)


