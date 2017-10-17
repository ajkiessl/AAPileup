# AAPileup
Bioinformatics tool for taking NGS and converting it to amino acid pileup.
NGSsim.py can simulate next-generation sequence output from a Sanger output.
Must download and install samtools and bowtie2.  They must be in $PATH for this pipeline to work.

The tookit directory contains some tools that can be used to manipulate files in the pipeline from within python.
This uses the pysam module.  Check it out at https://github.com/pysam-developers/pysam.
Also uses the SeqIO package from BioPython.
I didn't use these tools in the pipeline.  I used samtools instead.
