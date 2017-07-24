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
from scipy.optimize import fmin


def myfunc(p):
	x,y = p
	return x**2 + y**2 + 8
p = (1, 1)
print(fmin(myfunc, p))
