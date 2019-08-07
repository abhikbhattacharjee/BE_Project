a=1
for i in ~/Desktop/BE_Project/out/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o output_fimo/"fimo$fname" jaspar.txt $i
	#a=$((a+1))
	#echo $a
done
	
