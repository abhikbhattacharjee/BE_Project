bwa mem genome.fa sra_data.fastq > bwa_test_input
samtools view -S -b bwa_test_input > bwa_test_input.bam
samtools view -F 0x200 -F 0x4 -b bwa_test_input.bam > bwa_test_input_filtered.bam

