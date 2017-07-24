# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/24
	 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn import datasets
from sklearn.model_selection import train_test_split

X, y = datasets.make_classification(
	n_samples = 100, n_features = 4, n_redundant = 2,
	n_classes = 2, hypercube = False)
df = pd.DataFrame(X)
df["class"] = y
pd.scatter_matrix(df.iloc[:, :-1], figsize = (9, 9), diagonal = "kde", 
	    		  marker = "o", s = 40, alpha = .4, c = df["class"])

plt.show()