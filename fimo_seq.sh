a=1
export PATH=$HOME/meme/bin:$PATH

mkdir output_fimo
mkdir output_fimo/up_regulated_fimo
mkdir output_fimo/down_regulated_fimo
mkdir output_fimo/notdiff_regulated_fimo

for i in ~/Desktop/BE_Project/up_top_tags_out/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o output_fimo/up_regulated_fimo/"fimo$fname" JASPAR2018_insects_redundant_removed.txt $i
	#a=$((a+1))
	#echo $a
done

for i in ~/Desktop/BE_Project/down_top_tags_out/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o output_fimo/down_regulated_fimo/"fimo$fname" JASPAR2018_insects_redundant_removed.txt $i
	#a=$((a+1))
	#echo $a
done

for i in ~/Desktop/BE_Project/notdiff_top_tags_out/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o output_fimo/notdiff_regulated_fimo/"fimo$fname" JASPAR2018_insects_redundant_removed.txt $i
	#a=$((a+1))
	#echo $a
done


for i in ~/Desktop/BE_Project/output_fimo/up_regulated_fimo/*
do	
	python ~/Desktop/BE_Project/temp.py $i/*.tsv $i
	#echo $i
	#filename=$(basename "$i")
	#fname="${filename%.*}"
	#echo $filename
done

for i in ~/Desktop/BE_Project/output_fimo/down_regulated_fimo/*
do	
	python ~/Desktop/BE_Project/temp.py $i/*.tsv $i
	#echo $i
	#filename=$(basename "$i")
	#fname="${filename%.*}"
	#echo $filename
done

for i in ~/Desktop/BE_Project/output_fimo/notdiff_regulated_fimo/*
do	
	python ~/Desktop/BE_Project/temp.py $i/*.tsv $i
	#echo $i
	#filename=$(basename "$i")
	#fname="${filename%.*}"
	#echo $filename
done
		
