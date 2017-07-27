# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/26

import pandas as pd
from pandas import Series
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

if __name__ == '__main__':

	#
	# Load data
	# 
	shop_pay_csv = './shop_payNum_new.csv'
	data = pd.read_csv(shop_pay_csv)

	df = pd.DataFrame(np.array(data), columns = ['time_stamp', 'shop_id', 'pay_num', 'cate_2_name'])
	# df = df.cumsum()
	# ax = df.plot(x = ['time_stamp'], y = ['pay_num'], kind = 'line')
	# ax2 = df.plot(x = ['time_stamp'],  x_compat = True, kind = 'line')
	
	fast_food_pay_num = 0
	convenience_store_pay_num = 0
	hot_pot_pay_num = 0
	barbecue_pay_num = 0
	baking_cakes_pay_num = 0
	dict1 = {}

	for i in range(len(data)):
		if(data['cate_2_name'][i] == 'fast food'):
			fast_food_pay_num = fast_food_pay_num + 1
		elif(data['cate_2_name'][i] == 'convenience store'):
			convenience_store_pay_num = convenience_store_pay_num + 1
		elif(data['cate_2_name'][i] == 'hot pot'):
			hot_pot_pay_num = hot_pot_pay_num + 1
		elif(data['cate_2_name'][i] == 'barbecue'):
			barbecue_pay_num = barbecue_pay_num + 1
		elif(data['cate_2_name'][i] == 'baking cakes'):
			baking_cakes_pay_num = baking_cakes_pay_num + 1

	dict1.update({'fast food': fast_food_pay_num, 
				 'convenience store': convenience_store_pay_num, 
				 'hot pot': hot_pot_pay_num,
				 'barbecue': barbecue_pay_num,
				 'baking cakes': baking_cakes_pay_num,
				})

	dict1_list = list(dict1)
	dict1_list = Series(dict1_list).as_matrix().T
	dict1_data = Series(dict1).as_matrix().T
	food_data = np.vstack((dict1_list, dict1_data)).T
	print(food_data)

	df3 = pd.DataFrame(food_data, columns = ['food_name', 'food_pay_num'])
	print(df3)
	ax3 = df3.plot(x = ['food_name'], y = ['food_pay_num'], kind = 'line', color = 'orange')
	# # ax3 = df3.plot(kind = 'hist')
	plt.show()
