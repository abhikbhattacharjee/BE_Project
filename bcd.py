#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:16:09 2019

@author: chinmay
"""

import pandas as pd

p_c_not=pd.read_excel("/home/chinmay/Automated Module/Peakcalling_1e-4__PePr_peaks_homer.xlsx", 'notdiff_toptags_log2(1.05-0.95)')
p_c_down=pd.read_excel("/home/chinmay/Automated Module/Peakcalling_1e-4__PePr_peaks_homer.xlsx", 'down_toptags_log2_1.5')
p_c_up=pd.read_excel("/home/chinmay/Automated Module/Peakcalling_1e-4__PePr_peaks_homer.xlsx", 'up_toptags_log2_1.5')

cols = [1,2,3]
df = p_c_not[p_c_not.columns[cols]]
df=df.sample(frac=1)
df.to_csv(path_or_buf="/home/chinmay/tsvs/not.tsv",sep='\t',index=False,header=False)

df = p_c_down[p_c_down.columns[cols]]
df=df.sample(frac=1)
df.to_csv(path_or_buf="/home/chinmay/tsvs/down.tsv",sep='\t',index=False,header=False)

df = p_c_up[p_c_up.columns[cols]]
df=df.sample(frac=1)
df.to_csv(path_or_buf="/home/chinmay/tsvs/up.tsv",sep='\t',index=False,header=False)
