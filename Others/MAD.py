# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import numpy as np

def MSE(target, predictions):
	squared_deviation = np.power(target - predictions, 2)
	return np.mean(squared_deviation)

if __name__ == '__main__':
	# print ("MSE: ", MSE(boston.target, predictions))