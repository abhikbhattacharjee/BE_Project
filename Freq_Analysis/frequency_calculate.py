#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:09:25 2019

@author: yash
"""

import pandas as pd

peak_calling=pd.read_excel("/home/yash/BE_PROJECT/peak_calling_length.xlsx", 'not_diff')
peak_calling1=pd.read_excel("/home/yash/BE_PROJECT/peak_calling_length.xlsx", 'down_toptags')
peak_calling2=pd.read_excel("/home/yash/BE_PROJECT/peak_calling_length.xlsx", 'up_toptags')

mean_notdiff = peak_calling['Length'].mean() 
count1 = peak_calling['Length'].count() 
mean_downtags = peak_calling1['Length'].mean()
count2 = peak_calling1['Length'].count()
mean_uptags = peak_calling2['Length'].mean()
count3 = peak_calling2['Length'].count()

frequency_data=pd.read_excel("/home/yash/BE_PROJECT/overall_ana.xlsx")

frequency_data['notdiff_frequency']=(frequency_data['not_diff']*1000)/((round(mean_notdiff)+400)*count1)
frequency_data['down_frequency']=(frequency_data['down']*1000)/((round(mean_downtags)+  400)*count2)
frequency_data['up_frequency']=(frequency_data['up']*1000)/((round(mean_uptags)+400)*count3)


frequency_data['up/down'] = frequency_data['up']/frequency_data['down']
frequency_data['down/up'] = frequency_data['down']/frequency_data['up']

frequency_data['up/not_diff'] = frequency_data['up']/frequency_data['not_diff']
frequency_data['not_diff/up'] = frequency_data['not_diff']/frequency_data['up']

frequency_data['down/not_diff'] = frequency_data['down']/frequency_data['not_diff']
frequency_data['not_diff/down'] = frequency_data['not_diff']/frequency_data['down']

frequency_data = frequency_data.to_excel("/home/yash/BE_PROJECT/frequency_analysis.xlsx")

