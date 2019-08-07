
import re
import pandas

filename = "/home/chinmay/be-project/mast.txt"
infile = open(filename, "r")
outfile = open('motif_names.txt',"w")
nextline = ''
matrix_lines = ''
lines = infile.readlines()
outfile1 = open('motif_ext.txt',"w")
flag = 1
itr = iter(lines)

#print (lines)
while(flag):
    nextline = next(itr)
    if re.search("DATABASE AND MOTIFS", nextline) and flag==1:
        nextline = next(itr)
        nextline = next(itr)
        nextline = next(itr)
        nextline = next(itr)
        nextline = next(itr)
        nextline = next(itr)
        nextline = next(itr)
        nextline = next(itr)
        nextline = next(itr)
        
        
        
        while(not re.search("PAIRWISE MOTIF CORRELATIONS:",nextline)):
            outfile.write(nextline)
            matrix_lines.join('\n' + nextline)
            nextline = next(itr)
            flag = 0
    next(itr)
    
filename = "motif_names.txt"

#outfile = open('mast_gr_0.6.txt',"w")

df = pandas.read_table(filename, delim_whitespace=True)

#df2 = pandas.read_table("/home/chinmay/be-project/new_filter/out_gr_0.6.txt",header=0)
lineList = list()
with open("/home/chinmay/be-project/new_filter/out_gr_0.6.txt") as f:
  for line in f:
    lineList.append(line)

dataf=pandas.DataFrame(lineList)
dataf.columns = ['MOTIF']
dataf = dataf.replace('\n','', regex=True)

cond = df['MOTIF'].isin(dataf['MOTIF']) == True

df.drop(df[cond].index, inplace = True)

filename2 = "/home/chinmay/be-project/BE_Project/jaspar.txt"
infile = open(filename2, "r")
outfile3 = open('jaspar_filtered.txt',"w")
nextline = ''
matrix_lines = ''
lines = infile.readlines()

itr = iter(lines)
"""
###CODE to be checked for jaspar reducer
#print (lines)
for i in df.index[2:,]:        
    ser = "MOTIF "+df['ID'][i]+" "+df['ALT'][i]
    ender="URL http://jaspar.genereg.net/matrix/"+df['ID'][i]
    print(nextline)
    flag = 1
    print(ser)
    while(flag):
        nextline = next(itr)
        if re.search(ser, nextline) and flag==1:            
            while(not re.search(ender,nextline)):
                out = nextline
                outfile3.write(out)
                print(nextline)
                nextline = next(itr)
                flag = 0
    next(itr)
    outfile3.write(ender)
"""    