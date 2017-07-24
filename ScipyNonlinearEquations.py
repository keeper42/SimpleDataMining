# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

from scipy.optimize import fsolve 
from math import *
def f (x):
	x0, x1, x2 = x
	return [2*x1+3, 4*x0*x0 + sin(x1*x2), x1*x2/2 - 3]
ans = fsolve(f, [1.0, 1.0, 1.0])
print(ans)
print(f(ans))

# Scipy中提供了函数odeint，负责微分方程组的求解 是一个参数非常复杂的函数，但通常我们关心的只是该函数的前3项，因此，函数的调用格式可以缩写为：
# odeint(func, y0, t)
# func是有关微分方程组的函数，
# y0是一个元组，记录每个变量的初值，
# t则是一个时间序列。
# 使用时请注意，oedint函数，要求微分方程必须化为标准形式，即dy/dt=f(y,t)。