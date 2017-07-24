# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df3 = pd.DataFrame(np.random.rand(3, 4), columns=['a', 'b', 'c', 'd'])

plt.figure()
df3.plot(kind = "bar")
plt.axhline(0, color = "k")
plt.show()