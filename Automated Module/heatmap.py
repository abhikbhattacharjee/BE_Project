#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:43:52 2019

@author: abhik
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_excel("Excel/Final_result.xlsx")

df1 = df[['Unnamed: 0.1','up/down','down/up']]

heatmap1_data = pd.pivot_table(df1, values = 'down/up', index = ['Unnamed: 0.1'], columns = 'up/down')
plt.figure(figsize = (16,16))
sns.heatmap(heatmap1_data, cmap="YlGnBu")

fig = plt.figure(figsize = (16,5)).gca(projection='3d')

fig.scatter(df.index, df['up/down'], df['down/up'])
plt.show()