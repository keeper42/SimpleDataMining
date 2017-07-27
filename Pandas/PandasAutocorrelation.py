# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import autocorrelation_plot

x = np.linspace(-9 * np.pi, 9 *np.pi, num = 1000)
noise = 0.7 * np.random.rand(1000)
y = noise + 0.3 * np.sin(x)
data = pd.Series(y)
autocorrelation_plot(data)

plt.show()