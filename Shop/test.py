# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

#
# read_csv
# 
user_pay = pd.read_csv("user_pay_new.csv", header = None, names = ["time_stamp", "shop_id", "pay_num"])

# 分组
grouped = user_pay.groupby([[user_pay("shop_id")], user_pay["time_stamp"]])

# 得到每个商家历史日期每天的客流量
groupcnt = grouped.count()

# 
# To be continued ...
# 