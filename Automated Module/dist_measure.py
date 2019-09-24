#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:09:57 2019n

@author: abhik
"""
import re
import os
import pandas as pd
#import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import seaborn as sns


test_group_final = pd.DataFrame()

for dirpath, dirnames, files in os.walk('Output_fimo/Up_regulated_fimo'): #Output_fimo folder
    for file_name in files:
        if file_name.endswith('ubx.xlsx'):
            test = pd.read_excel(dirpath+"/"+str(file_name))
            #print(test[test.motif_alt_id=='mes2'])
            test = test[test.motif_alt_id=='mes2']
            #test = test.loc[0][test[test[re.search('ubx', test.columns)]]]
            
            """path = os.path.dirname(dirpath+"/"+str(file_name))  
            basename1 = os.path.basename(path)
            print(basename1)"""
            #test['filename'] = basename1
            #test = test.append()
            
            
            #test = test.rename(columns=re.search("Ubx"))
            test_group_final = test_group_final.append(test)#[test.motif_alt_id=='mes2']) 
test_group_final = test_group_final.filter(regex="ubx").dropna(how = 'all')

test_group_final1 = pd.DataFrame()

for dirpath, dirnames, files in os.walk('Output_fimo/Up_regulated_fimo'): #Output_fimo folder
    for file_name in files:
        if file_name.endswith('ubx.xlsx'):
            test = pd.read_excel(dirpath+"/"+str(file_name))
            #print(test[test.motif_alt_id=='mes2'])
            test = test[test.motif_alt_id=='mes2']
            #test = test.loc[0][test[test[re.search('ubx', test.columns)]]]
            
            """path = os.path.dirname(dirpath+"/"+str(file_name))  
            basename1 = os.path.basename(path)
            print(basename1)"""
            #test['filename'] = basename1
            #test = test.append()
            
            
            #test = test.rename(columns=re.search("Ubx"))
            test_group_final1 = test_group_final1.append(test)#[test.motif_alt_id=='mes2']) 
test_group_final1 = test_group_final1.filter(regex="Ubx").dropna(how = 'all')


arr = []
for i in range(0, len(test_group_final)):
    for j in range(0, len(test_group_final.columns)):
        if(test_group_final.iloc[i][j]>=0 or test_group_final.iloc[i][j]<0):
            arr.append(test_group_final.iloc[i][j])
    
arr1 = []
for i in range(0,len(test_group_final1)):
    for j in range(0, len(test_group_final1.columns)):
        if(test_group_final1.iloc[i][j]>=0 or test_group_final1.iloc[i][j]<0):
            arr1.append(test_group_final1.iloc[i][j])

#Plots
sns.distplot(arr,kde=True)
sns.distplot(arr1,kde=True)

plt.hist(arr1, 20)
plt.show()

plt.hist(arr, 20)
plt.show()

#Gaussian Curve
mu = 0
variance = 1
sigma = math.sqrt(variance)

x = np.linspace(mu-3 * sigma, mu+3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()
