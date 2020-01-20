# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:07:09 2020

@author: Abhik
"""

import pylab as plt
import numpy as np

fn = "heatmap.txt"
with open(fn, "r") as f:
    labels = f.readline().rstrip("\n").split()[1:]
data = np.loadtxt(fn, skiprows=1, converters={0:lambda x: 0})
plot_data = np.ma.masked_equal(data[:,1:], 0)

plt.subplots_adjust(left=0.1, bottom=0.15, right=0.99, top=0.95)
plt.imshow(plot_data, cmap=plt.cm.get_cmap("Reds"), interpolation="nearest", aspect = "auto")
plt.xticks(range(len(labels)), labels, rotation=90, va="top", ha="center")
plt.colorbar()

plt.rcParams["figure.figsize"] = (20,10)
plt.show()