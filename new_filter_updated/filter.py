
import re

filename = "mast.txt"
infile = open(filename, "r")
outfile = open('mast_filtered.txt',"w")
nextline = ''
matrix_lines = ''
lines = infile.readlines()

flag = 1
itr = iter(lines)

#print (lines)
while(flag):
    nextline = next(itr)
    if re.search("	PAIRWISE MOTIF CORRELATIONS:", nextline) and flag==1:
        nextline = next(itr)
        nextline = next(itr)
        nextline = next(itr)
        
        while(not re.search("Correlations above 0.60",nextline)):
            outfile.write(nextline)
            matrix_lines.join('\n' + nextline)
            nextline = next(itr)
            flag = 0
    next(itr)
