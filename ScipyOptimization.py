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

def f(x):
	return x**2 - 4*x + 8
x = np.linspace(-4, 4, 1000)
y = f(x)
fig1 = plt.figure()
fig1.add_subplot(Series(y, index = x).plot(kind = "line"))
fig1.show()

# scipy.optimize包提供了求极值的函数fmin
from scipy.optimize import fmin
print(fmin(f, 0))

plt.show()
