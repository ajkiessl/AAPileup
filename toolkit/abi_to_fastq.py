"""
Designed and written by Benjamin Allen
This converts the abi file output from Sanger sequencing to a more useable fastq format
"""

from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputs',nargs='+')
parser.add_argument('-output',required=True)
parser.add_argument('-rc',action='store_true')
parser.add_argument('-clip5prime')
parser.add_argument('-clip3prime')
args = parser.parse_args()

with open(args.output,'wb') as out:
   for inp in args.inputs:
      record = SeqIO.parse(open(inp,'rb'),'abi').next()
      if args.rc:
         record = record.reverse_complement(id=True,name=True,description=True)
      if args.clip5prime:
         start = record.seq.find(args.clip5prime)
         if start > 0:
            record = record[start+len(args.clip5prime):]
      if args.clip3prime:
         stop = record.seq.find(args.clip3prime)
         if stop > 0:
            record = record[:stop]
      SeqIO.write(record,out,'fastq')
