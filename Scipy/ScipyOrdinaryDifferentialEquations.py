# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import numpy as np
from scipy.integrate import odeint

def lorenz(w, t):
	r = 10.0
	p = 28.0
	b = 3.0
	x, y, z = w
	return np.array([r*(y-x), x*(p-z)-y, x*y-b*z])

t = np.arange(0, 30, 0.01) # 创建时间点 
# 调用odeint对lorenz进行求解, 用两个不同的初始值 
track1 = odeint(lorenz, (0.0, 1.00, 0.0), t) 
track2 = odeint(lorenz, (0.0, 1.01, 0.0), t) 
# 绘图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(track1[:,0], track1[:,1], track1[:,2])
ax.plot(track2[:,0], track2[:,1], track2[:,2])
plt.show()
print(track1)