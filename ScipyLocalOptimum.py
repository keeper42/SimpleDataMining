# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25


from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x**2 + 20 * np.sin(x)

# 当起始点设置为0时，它找到了0附近的最小极值点，该解也是全局最优解
ans=optimize.fmin_bfgs(f, 0)
print(ans)

# 全局最优求解一种代替方案
ans = optimize.fminbound(f, -100, 100) 
print(ans)
print(f(ans))