# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

#
# 曲线拟合
#
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def f(x,a,b):
    return a*x + b

x = np.linspace(-10, 10, 30)
y = f(x,2,1)
ynew= y+ 3*np.random.normal(size=x.size)  # 产生带噪声的数据点
popt, pcov = optimize.curve_fit(f,x,ynew)
print(popt)
print (pcov)
plt.plot(x,y,color='r',label='orig')
plt.plot(x,popt[0]*x+popt[1],color='b',label='fitting')
plt.legend(loc='upper left')
plt.scatter(x,ynew)
plt.show()

