# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats as stats
from scipy.optimize import opt

def f(p):
    x,y = p
    ans = (np.sin(x)+0.05*x**2) + np.sin(y)+0.05*y**2
    return ans

# x和y都是在-10,10区间内，采用步长0.1进行网格搜索求最优解
rranges = (slice(-10, 10, 0.1), slice(-10, 10, 0.1))
res = opt.brute(f.rranges)
print(res)
print(f(res))

