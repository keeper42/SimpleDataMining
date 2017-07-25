# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import matplotlib.pyplot as plt
import numpy as np
from numpy import mat
import sys
import time
import svmMLiA

if __name__ == '__main__':
	
	# 读取数据
	dataArr, labelArr = svmMLiA.loadDataSet("./testSet.txt")
	print("following is the data: ")
	print(dataArr)
	print("following is the label of every data: ")
	print(labelArr)

	# 简化的SMO算法
	s = time.clock()
	b, alphas = svmMLiA.smoSimple(dataMatIn = dataArr, classLabels = labelArr, C = 0.6, toler = 0.001, maxIter = 40)
	dual = time.clock() - s

	# 构建支持向量
	suppVector = []
	for i in range(100):
		if alphas[i] > 0.0:
			print(dataArr[i], labelArr[i])
			suppVector.append(dataArr[i])

	# 绘制支持向量
	import plotSupportVectors
	s2 = time.clock()
	b, alphas = svmMLiA.smoP(dataArr, labelArr, 0.6, 0.001, 40)
	dual2 = time.clock() - s2

	# 利用alpha值进行分类
	ws = svmMLiA.calcWs(alphas, dataArr, labelArr)
	# 利用ws进行分类
	dataMat2 = mat([4.6581910000000004, 3.507396])
	value = dataMat2 * mat(ws) + b
	print(u"0号样本的值：", value)
	print(" 预测的类标为：", -1)

	# 测试CBF
	svmMLiA.testRbf()
