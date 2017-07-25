# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

print('小圆点表示异常值，上黑色线是上限，下黑线是下限')
print('箱中的一条线是中位数，箱子上边缘是上四分位线')
print('，下边缘是下四分位线')
df = pd.DataFrame(np.random.rand(10, 5), columns = ["A", "B", "C", "D", "E"])
df.ix[2:3, "A"] = [-1, -2]
df.ix[2:3, "D"] = [1.5, 2]
color = dict(boxes = "DarkGreen", whiskers = "DarkOrange", medians = "DarkBlue", caps = "Gray")
df.plot.box(color = color, sym = "r+")

plt.show()