# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import pandas as pd
import os

test = pd.read_csv(str(sys.argv[1]),delimiter='\t',encoding='utf-8') 
#print(list(test.columns.values))

sorted_values = test.sort_values("motif_alt_id", ascending = True)
#print(str(sys.argv[1]))
print(sorted_values)
out_path = str(sys.argv[2])
print(out_path)
filename = "sorted_values_fimo.xlsx"
sorted_values.to_excel(os.path.join(out_path,filename), index=False)