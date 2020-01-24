bwa index genome.fa
wait

parallel bash ::: script.sh script1.sh
wait

macs2 callpeak -t bwa_test_filtered.bam -c bwa_test_input_filtered.bam --outdir macs2
annotatePeaks.pl macs2/NA_summits.bed dm6 -noblanks > homer_data
annotatePeaks.pl macs2/NA_summits.bed dm6 -noblanks > homer_data.xls




