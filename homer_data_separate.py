# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:41:22 2020

@author: badhe
"""

#HOMER DATA Sheet separation

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("homer_data.xlsx")

writer = pd.ExcelWriter('homer_data_separated.xlsx', engine='xlsxwriter')

df1 = df.sort_values("Annotation")
df3 = df1["Annotation"].str.split(" ", n=1, expand =True)
df1['0'] = df3[0]

list1 = df3[0].unique()
sheet_counts = pd.DataFrame(columns=["Counts"])
sheet_counts["Annotation"] = df3[0].unique()

for i in range(len(list1)):
    df_temp = df[df1['0']==list1[i]]
    df_temp.to_excel(writer, sheet_name=list1[i])
    sheet_counts.loc[sheet_counts["Annotation"]==list1[i], "Counts"] = len(df_temp)
    
writer.save()

def counts(val):
    percent = np.round(val/100.*sheet_counts["Counts"].sum(),0)
    return str(percent)+'\n'+str(np.round(val,1))+'%'  

plt.pie(sheet_counts["Counts"], autopct=counts, labels=sheet_counts["Annotation"])
plt.rcParams["figure.figsize"] = (10,10)
plt.show()
