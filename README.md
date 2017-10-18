# AAPileup

Bioinformatics tool for taking next-generation sequencing or Sanger sequencing outputs and converting them to amino acid pileup.
ngs_sim.py can simulate next-generation sequencing outputs from a Sanger output.
You must download and install samtools and bowtie2 and they must be in $PATH for this pipeline to work.  
alignvariants.sh is the bash script that contains the pipeline.

The tookit directory contains some tools that can be used to manipulate files in the pipeline from within python.
This uses the pysam module.  Check it out at https://github.com/pysam-developers/pysam.
Also uses the SeqIO package from BioPython.
The only tool I used in the pipeline is fastq_filter.py.  I used samtools instead of the other tools.
