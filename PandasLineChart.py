# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

if __name__ == "__main__":
	df3 = pd.DataFrame(np.random.randn(1000, 4), columns=["A", "B", "C", "D"])
	df3 = df3.cumsum()
	ax = df3.plot(secondary_y=['A', 'B'], x_compat=True, mark_right=True)
	ax.set_ylabel('CD scale')
	ax.right_ax.set_ylabel('AB scale')

	plt.show()