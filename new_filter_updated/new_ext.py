
import re
import pandas as pd

infile = open("mast.txt", "r")
outfile = open('motif_names.txt',"w")
nextline = ''
matrix_lines = ''
lines = infile.readlines()
#outfile1 = open('motif_ext.txt',"w")
flag = 1
itr = iter(lines)

#print (lines)
while(flag):
    nextline = next(itr)
    if re.search("\tMOTIF ", nextline) and flag==1:
        while(not re.search("PAIRWISE MOTIF CORRELATIONS:",nextline)):
            outfile.write(nextline)
            matrix_lines.join('\n' + nextline)
            nextline = next(itr)
            flag = 0
    
outfile.close()
filename = "motif_names.txt"

#outfile2 = open('out_gr_0.6.txt', "w")


df = pd.read_table(filename, delim_whitespace=True)

#df2 = pandas.read_table("/home/chinmay/be-project/new_filter/out_gr_0.6.txt",header=0)
lineList = list()
with open("out_gr_0.6.txt") as f:           #Reading from out_gr_0.6.txt
  for line in f:
    lineList.append(line)

dataf=pd.DataFrame(lineList)
dataf.columns = ['MOTIF']
dataf = dataf.replace('\n','', regex=True)

cond = df['MOTIF'].isin(dataf['MOTIF']) == True

df.drop(df[cond].index, inplace = True)

filename2 = "jaspar.txt"
infile = open(filename2, "r")
outfile3 = open('jaspar_filtered.txt',"w")

flag=1
#IF "jaspar_prefix.txt" is needed, flag = 1 (Adding denovo and grain to jaspar)
if(flag==1):
    with open("jaspar_prefix.txt") as f:
        for line in f:
            outfile3.write(line)

outfile3.write("MEME version 4\n\nALPHABET= ACGT\n\nstrands: + -\n\nBackground letter frequencies\nA 0.25 C 0.25 G 0.25 T 0.25\n\n")
nextline = ''
matrix_lines = ''
lines = infile.readlines()

itr = iter(lines)

###CODE to be checked for jaspar reducer
"""awk -FS=" " 'NR==FNR {b[$0]; next} {for (x in b) if($0 ~ x) next;print $0}' out_gr_0.6.txt mast_filtered.txt
code for extraction of unique row nos
"""
#print (lines)
for i in df.index[2:,]:        
    ser = "MOTIF "+df['ID'][i]+" "+df['ALT'][i]
    ender="URL http://jaspar.genereg.net/matrix/"+df['ID'][i]
    print(nextline)
    flag = 1
    while(flag):
        if ser in nextline and flag==1:            
            while(not re.search(ender,nextline)):
                out = nextline
                outfile3.write(out)
                print(nextline)
                nextline = next(itr)
                flag = 0
        nextline = next(itr)        
    outfile3.write(ender)
    outfile3.write("\n")
    outfile3.write("\n")
    
#outfile1.close()
#outfile2.close()
outfile3.close()