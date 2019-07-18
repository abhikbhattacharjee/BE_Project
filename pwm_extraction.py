# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:35:58 2019

@author: Abhik
"""
import sys

f = open("mast.txt")
"""print(f.read())"""

s = f.read()
"""print(s)"""

start = s.find("PAIRWISE MOTIF CORRELATIONS")
end = s.find("Correlations")

if start == -1 or end == -1:
    print("Not Found. ERROR!")
    sys.exit(0)
    
end += len("Correlations")

print(s[start:end])