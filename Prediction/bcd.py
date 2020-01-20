#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:16:09 2019

@author: chinmay
"""

import pandas as pd

p_c=pd.read_excel("Peakcalling_1e-4__PePr_peaks_homer.xlsx", 'Peakcalling_1e-4__PePr_peaks_ho')

cols = [1,2,3]

df = p_c[p_c.columns[cols]]
#df=df.sample(n=258)
df.to_csv(path_or_buf="predict.tsv",sep='\t',index=False,header=False)

