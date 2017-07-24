# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df = pd.DataFrame(np.random.rand(50, 4), columns = ["a", "b", "c", "d"])
df.plot.scatter(x = "a", y = "b", color = "DarkBlue", s = 80)

plt.show()