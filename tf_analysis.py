#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:09:57 2019

@author: abhik
"""

import os
import pandas as pd
#import sys

test_group_final = pd.DataFrame()

for dirpath, dirnames, files in os.walk('/home/abhik/Desktop/BE_Project/output_fimo'): #Output_fimo folder
    for file_name in files:
        if file_name.endswith('.xlsx'):
            test = pd.read_excel(dirpath+"/"+str(file_name)) 
            #print(test)
            path = os.path.dirname(dirpath+"/"+str(file_name))
            basename1 = os.path.basename(path)
            columns1 = test['motif_alt_id'].unique()
            
            test_group = test.groupby(['motif_alt_id']).size().reset_index(name=basename1)
            count1 = test_group[basename1]
            
            #df = DataFrame(test_group, columns = test['motif_alt_id'])
            #print(columns1) #should be column name
            #print(basename1)#should be row name
            #print(count1)#should be column values
            
            
            test_group.index = test_group.loc[:,'motif_alt_id']
            test_group = test_group.drop(['motif_alt_id'],axis = 1)
            test_group = test_group.T
            
            test_group_final=test_group_final.append(test_group,sort=False)
test_group_final=test_group_final.sort_index(axis=0)
print(test_group_final)
