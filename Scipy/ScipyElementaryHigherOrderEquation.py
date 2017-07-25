# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

from scipy import optimize
import numpy as np
def f(x):
    return x**2 + 20 * np.sin(x)
ans = optimize.fsolve(f, -4)
print(ans)
print(f(ans))