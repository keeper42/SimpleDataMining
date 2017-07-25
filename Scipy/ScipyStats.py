# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as stats

# 产生20个在[0，1]均匀分布的随机数
fig1 = plt.figure()
x = stats.uniform.rvs(size = 10000)
fig1.add_subplot(Series(x).plot(kind = "kde"))
fig1.show()

# 产生20个服从参数a=3，b=4的贝塔分布随机数
fig2 = plt.figure()
y=stats.beta.rvs(size=10000,a=3,b=4)
fig2.add_subplot(Series(y).plot(kind='kde'))
fig2.show()

# 产生了20个服从[0，1]正态分布的随机数
fig3 = plt.figure()
z=stats.norm.rvs(size=10000,loc=0,scale=1)
fig3.add_subplot(Series(z).plot(kind='kde'))
fig3.show()

# 产生poisson分布
fig4 = plt.figure()
p=stats.poisson.rvs(0.6,loc=0,size=10000)
Series(p).plot(kind='kde')
fig4.show()

plt.show()
