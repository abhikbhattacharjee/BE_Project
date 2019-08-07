# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:26:28 2019

@author: badhe
"""
import pandas as pd
import numpy as np
import re
import os
from io import StringIO

filename = "mast_filtered.txt"
#mat = pd.read_csv(filename, sep = "  ",skiprows = 2, usecols = range[1:135])

outfile = open('mast_gr_0.6.txt',"w")

with open(filename) as f:
    content = [x.strip().split()[1:] for x in f]

for k in content:
    for p in k:
        if(float(p)>=0.6 and float(p)<1):
            out = "\n" + str(content.index(k)+2) + "\t" + str(k.index(p)+1) + "\t" + str(float(p))
            outfile.write(out)

record = "mast_gr_0.6.txt" 


"""
with open(record) as r:
    new_content = [x.strip().split()[0:] for x in r]

length=len(new_content)
motif = set()
for i in range(length):
    motif.add(new_content[i][0])
print(motif)


matrix = []
i = 0
for k in content[1:]:
    matrix.append(np.array(k), dtype = float)
    i+=1

matrix1 = np.loadtxt(StringIO("mast_filtered.txt"), delimiter = "  ", skiprows = 2, dtype = float)[1:,2:]
matt = np.genfromtxt(StringIO("mast_filtered.txt")"""
