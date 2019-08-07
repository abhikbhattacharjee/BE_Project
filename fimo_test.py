# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:20:53 2019

@author: Abhik
"""
import pandas as pd

test = pd.read_csv('C:\\Users\\Abhik\\Desktop\\fimo (2).tsv',delimiter='\t',encoding='utf-8') 
print(list(test.columns.values))

sorted_values = test.sort_values("sequence_name", ascending = True)
print(sorted_values)
sorted_values.to_excel("test.xlsx")