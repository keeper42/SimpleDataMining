# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 
                    'b': np.random.randn(1000), 
                    'c': np.random.randn(1000) - 1},
                     columns=['a', 'b', 'c'])
df4.plot(kind = "hist", orientation = "vertical", cumulative = False,
	    bins = 15, alpha = 0.3, legend = True, logy = True)

plt.show()