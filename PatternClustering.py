# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import numpy as np
from scipy.cluster import vq
import matplotlib.pyplot as plt

class1 = np.random.randn(30,2)+10  # 产生第一个正态分布类，基础抬高10
class2 = np.random.randn(40,2)-10  # 产生第二个正态分布类，基础降低10
class3 = np.random.randn(50,2)     # 产生第三个正态分布类
data = np.vstack([class1,class2,class3]) #将数据叠合到一起，形成一个矩阵

centroid, var = vq.kmeans(data,3)   
# 用k均值聚类法聚类，指定按3个类别聚类，获取类中心和方差
key,distance = vq.vq(data,centroid)  # 根据聚类中心，将不同的样本分类
vqclass1 = data[key==0]  # 取出类别0
vqclass2 = data[key==1]
vqclass3 = data[key==2]
plt.scatter(vqclass1[:,0],vqclass1[:,1],marker='o', color="r",label='c1')  # 为类0制图
plt.scatter(vqclass2[:,0],vqclass2[:,1],marker='1', color="g" ,label='c2')
plt.scatter(vqclass3[:,0],vqclass3[:,1],marker='2', color="b",label='c3')
plt.legend(loc='upper left')
plt.show()
