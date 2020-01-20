export PATH=$HOME/meme/bin:$PATH

mkdir FASTA
mkdir FASTA/Prediction_source
mkdir Output_fimo
mkdir Output_fimo/Prediction_source_fimo
mkdir Excel

python bcd.py

mv predict.tsv predict.bed

bedtools slop -i predict.bed -g dmel.genome -b 200 > predict_final.bed        
bedtools getfasta -fi genome.fa -bed predict_final.bed -fo predict_toptags
rm predict.bed

python FASTA_splitting.py predict_toptags

for i in FASTA/Prediction_source/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o Output_fimo/Prediction_source_fimo/"fimo$fname" JASPAR2018_insects_redundant_removed.txt $i
done

for i in Output_fimo/Prediction_source_fimo/*
do	
	python Sort_seq.py $i/*.tsv $i
done

python Peak_calling_length_python_code.py
wait
python Tf_analysis.py
wait
python Train_data_generation.py
wait
python final_keras_90acc.py       
 
