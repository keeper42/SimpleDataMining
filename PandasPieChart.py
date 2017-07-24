# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df = pd.DataFrame([[0.1,4], [0.1,4], [0.1,2], [0.1,4]],
				index = ["a", "b", "c", "d"], columns = ["x", "y"])
df.plot.pie(subplots = True, figsize = (8, 4))

plt.show()
