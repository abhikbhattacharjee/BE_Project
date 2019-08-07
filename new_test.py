#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:35:58 2019

@author: abhik
"""

import os
import pandas as pd
from pandas import DataFrame

test = pd.read_excel("/home/abhik/Desktop/BE_Project/output_fimo/fimo57/sorted_values_fimo.xlsx") 
print(test)
path = os.path.dirname("/home/abhik/Desktop/BE_Project/output_fimo/fimo57/sorted_values_fimo.xlsx")
basename1 = os.path.basename(path)
columns1 = test['motif_alt_id'].unique()

test_group = test.groupby(['motif_alt_id']).size().reset_index(name='Count')
count1 = test_group['Count']

#df = DataFrame(test_group, columns = test['motif_alt_id'])
print(columns1) #should be column name
print(basename1)#should be row name
print(count1)#should be column values

'''
df1 = pd.DataFrame(columns=basename1)
#df2 = pd.concat(df1,count1)
print(df1)
'''

