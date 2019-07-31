# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:46:33 2019

@author: badhe
"""

filename = "C:\\Users\\badhe\\Downloads\\seq2"
infile = open(filename, "r")

base_out = "C:\\Users\\badhe\\Downloads\\out\\"

lines = infile.readlines()
itr = iter(lines)
count = 0

outfile = open(filename+"1","w+")

nextline = next(itr)

while(nextline!='\0'):
    if(nextline.startswith('>')):
        outfile.close()
        count+=1
        outfile = open(base_out+str(count)+".txt", "w+")
        outfile.write(nextline)
    else:
        outfile.write(nextline)
    nextline = next(itr)

outfile.close()
outfile.close()

infile.close()
