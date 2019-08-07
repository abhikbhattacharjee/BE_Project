a=1
for i in ~/Desktop/BE_Project/output_fimo/*
do	
	python ~/Desktop/BE_Project/temp.py $i/*.tsv $i
	#echo $i
	#filename=$(basename "$i")
	#fname="${filename%.*}"
	#echo $filename
done
	
