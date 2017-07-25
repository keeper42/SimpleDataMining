# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import kMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

if __name__ == '__main__':
	
	datMat = np.mat(kMeans.loadDataSet("./testSet.txt"))
	# datMat[:3, :]

	# 聚类
	myCentroids, clustAssing = kMeans.kMeans(datMat, 4)
	
	# 将聚类中心数据转化为 DataFrame 类型，字段名分别取为 x 和 y
	center = pd.DataFrame(myCentroids, columns=['x', 'y'])
	
	# 将原始的坐标数据转化为 DataFrame 类型，字段名分别为 x 和 y
	frame = pd.DataFrame(datMat, columns=['x', 'y'])
	
	# 将聚类的结果添加到 fame 变量中
	frame["label"] = clustAssing.A[:, 0].astype(pd.np.int)

	# 根据原始数据的坐标绘制散点图，给不同类标的数据绘制不同的颜色
	ax = None 
	color = ['orange', 'blue', 'yellow', 'green', 'red']
	for i, c in enumerate(sorted(frame['label'].unique())):
		ax = frame[frame['label'] == c].plot(x = 'x', y = 'y', kind = 'scatter',
			label = "cluster{0}".format(c), c = color[i % len(color)], ax = ax)
	
	# 绘制聚类中心，用黑色表示 x
	center.plot(x = 'x', y = 'y', kind = 'scatter', marker = 'x', s = 50, c = 'black', ax = ax)
	# plt.show()

	# 聚类及可视化
	kMeans.clusterClubs(numClust = 5)
