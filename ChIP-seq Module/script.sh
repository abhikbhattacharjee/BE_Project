bwa mem genome.fa sra_data1.fastq > bwa_test
samtools view -S -b bwa_test > bwa_test.bam
samtools view -F 0x200 -F 0x4 -b bwa_test.bam > bwa_test_filtered.bam


