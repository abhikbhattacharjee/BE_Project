# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:46:33 2019

@author: badhe
"""

filename = "C:\\Users\\badhe\\Downloads\\up_toptags"
infile = open(filename, "r")

base_out = "C:\\Users\\badhe\\Downloads\\up_top_tags_out\\"

lines = infile.readlines()
itr = iter(lines)
count = 0

outfile = None

nextline = next(itr)

while(1):
    if(nextline.startswith('>')):
        try:
            outfile.close()
        except AttributeError:
            pass
        count+=1
        outfile = open(base_out+str(count)+".txt", "w+")
        outfile.write(nextline)
    else:
        outfile.write(nextline)
    
    try:
        nextline = next(itr)
    except StopIteration:
        break

outfile.close()
infile.close()