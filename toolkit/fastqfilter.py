"""
Filter fastq by phred score and length.  
This program also converts to any fastq format (defaulted fastq-sanger)
"""

from Bio import SeqIO
import argparse
import random

parser = argparse.ArgumentParser(description="Filter fastq by length and phred score.")
parser.add_argument('-fastqinput', required=True)
parser.add_argument('-lengthfilter', type=int, default=0)
parser.add_argument('-phredmin', type=int, default=10)
parser.add_argument('-allowance', type=int, default=3)
parser.add_argument('-outputtype',type=str, default='fastq-sanger')
parser.add_argument('-outputid', required=True)
args = parser.parse_args()

fastqfile = open(args.fastqinput,'rU')

#filter seqs by length
filter1_fastq = []
for record in SeqIO.parse(fastqfile, "fastq"):
    if int(args.lengthfilter) == len(record.seq):
        filter1_fastq.append(record)
    if int(args.lengthfilter) == 0:
        filter1_fastq.append(record)

#filter again by phred quality
filter2_fastq=[]
for record in filter1_fastq:
    bad_quality_count=0
    for phred in record.letter_annotations["phred_quality"]:
        if phred <= int(args.phredmin):
            bad_quality_count+=1
    if bad_quality_count < int(args.allowance):
        filter2_fastq.append(record)

#write to new file
file = open((args.outputid),'w')

for record in filter2_fastq:
    file.write(str(record.format(args.outputtype)))

file.close()
fastqfile.close()
