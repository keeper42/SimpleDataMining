# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

#
# 插值
#
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

#  x,y 现在是假设的采样点
x = np.linspace(0,10*np.pi,20)  #产生20个点
y = np.sin(x)

fl = interp1d(x,y,kind = 'linear')  # 线性插值函数
fq = interp1d(x,y,kind = 'quadratic') # 二次样条插值
fc = interp1d(x,y,kind = 'cubic') # 三次样条插值
xint = np.linspace(x.min(),x.max(),1000) # 产生插值点
yintl = fl(xint) # 由线性插值得到的函数值
yintq = fq(xint) # 由二次样条插值函数计算得到的函数值
yintc = fc(xint) # 由三次样条插值函数计算得到的函数值
plt.plot(xint,yintl,color = 'r', linestyle = '--',label = 'linear')
plt.plot(xint,yintq,color = 'b' ,label = 'quadr')
plt.plot(xint,yintc,color = 'b' ,linestyle = '-.',label = 'cubic')
plt.legend()
plt.show()

