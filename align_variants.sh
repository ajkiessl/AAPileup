"""
This bash script runs a pipeline to convert a fastq file to BAM pileup format.
It takes a fastq and fasta file as inputs.
Bowtie2 is the aligner used.
"""
#!/bin/bash
fastqfile=$1
fastafile=$2
echo $fastafile, $fastqfile
fastabase=$( basename $fastafile )
fastabaseid=${fastabase%.*}
filteredfastqfile=$( basename $fastqfile )
filteredfastqfilename=${filteredfastqfile%.*}_filtered.fastq
python ./toolkit/fastqfilter.py -fastqinput $fastqfile -outputid $filteredfastqfilename
samoutfile=$( basename $filteredfastqfile )
samoutfilename=${samoutfile%.*}.sam
bowtie2-build $fastafile $fastabaseid
bowtie2 -x $fastabaseid -q $filteredfastqfilename -D 60 -R 6 -N 1 -L 20 -i S,1,0.50 --reorder -S $samoutfilename
samtobamfile=$( basename $samoutfilename )
samtobamfilename=${samtobamfile%.*}.bam
samtools view -bS $samoutfilename > $samtobamfilename
sortedbamfile=$( basename $samtobamfilename )
sortedbamfilename=${sortedbamfile%.*}_sorted
samtools sort $samtobamfilename $sortedbamfilename
indexinput=$( basename $sortedbamfilename ).bam
samtools index $indexinput
