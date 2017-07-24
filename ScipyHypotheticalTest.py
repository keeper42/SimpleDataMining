# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as stats

# 假定数据服从正太分布
normDist = stats.norm(loc = 2.5, scale = 0.5)
z = normDist.rvs(size = 400)
mean = np.mean(z)
med = np.median(z)
dev = np.std(z)
print("mean = ", mean, " med = ", med, " dev = ", dev)
statVal, pVal = stats.kstest(z,'norm',(mean,dev))
print('计算得到,服从某个正太分布的pValue值：')
print('pVal = ',pVal)
print('结论：我们接受假设，既z数据是服从正态分布的')

