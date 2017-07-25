# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/07/25

import trees, treePlotter
from copy import deepcopy

# 加载数据
fr = open('lenses.txt')

# 创建决策树
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']

lensesTree = trees.createTree(lenses, deepcopy(lensesLabels))
treePlotter.createPlot(lensesTree, figsize=(10,10))

# 使用决策树进行分类
asample = ['young', 'myope', 'no', 'normal', 'soft']
# 特征字段名列表
lensesLabels=['age', 'prescript', 'astigmatic', 'tearRate']
print(trees.classify(lensesTree, lensesLabels, asample))
