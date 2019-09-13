a=1
export PATH=$HOME/meme/bin:$PATH

mkdir FASTA
mkdir FASTA/Up_Regulated
mkdir FASTA/Down_Regulated
mkdir FASTA/Notdiff_Regulated
mkdir Output_fimo
mkdir Output_fimo/Up_regulated_fimo
mkdir Output_fimo/Down_regulated_fimo
mkdir Output_fimo/Notdiff_regulated_fimo
mkdir Excel

python FASTA_splitting.py up_toptags down_toptags notdiff_toptags 


for i in FASTA/Up_Regulated/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o Output_fimo/Up_regulated_fimo/"fimo$fname" Latest_JASPAR.txt $i
done

for i in FASTA/Down_Regulated/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o Output_fimo/Down_regulated_fimo/"fimo$fname" Latest_JASPAR.txt $i
done

for i in FASTA/Notdiff_Regulated/*.txt
do	
	
	filename=$(basename "$i")
	fname="${filename%.*}"
	fimo -o Output_fimo/Notdiff_regulated_fimo/"fimo$fname" Latest_JASPAR.txt $i
done


for i in Output_fimo/Up_regulated_fimo/*
do	
	python Sort_seq.py $i/*.tsv $i
done

for i in Output_fimo/Down_regulated_fimo/*
do	
	python Sort_seq.py $i/*.tsv $i
done

for i in Output_fimo/Notdiff_regulated_fimo/*
do	
	python Sort_seq.py $i/*.tsv $i
done
	
python Peak_calling_length_python_code.py
python Tf_analysis.py
python Overall_count_analysis.py	
python Frequency_analysis.py
