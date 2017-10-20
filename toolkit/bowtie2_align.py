"""
app for running bowtie2 alignment on a fastq and indexed fasta file
"""

import subprocess
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-fa', required = True, help='path to fasta file')
parser.add_argument('-fq', required = True, help='path to fastq file')
args = parser.parse_args()

indexBaseName = str(args.fa)[:-6]
baseName = str(args.fq)[:-6]

subprocess.call(['bowtie2-build', args.fa, indexBaseName])
subprocess.call(['bowtie2', '-x', indexBaseName, '-U', args.fq, '-S', baseName + '.sam'])
