"""
This app takes a pileup format BAM file and converts to amino acid sequence
Arguments: path/to/BAMfile.bam, path/to/fastafile.fasta
"""

import pysam
import argparse
import sys
from Bio.Seq import Seq
from pysam import AlignedSegment

# Argument Parser
parser = argparse.ArgumentParser(description="Amino acid pileup for BAM alignments and corresponding reference")
parser.add_argument('-BAMinput',required=True)
parser.add_argument('-fastainput',required=True)
args = parser.parse_args()

# File Inputs
fastafile = pysam.FastaFile(args.fastainput)
samfile = pysam.AlignmentFile(args.BAMinput, "rb")

# codon formation function
def batch_gen(data, batch_size):
    for i in range(0, len(data), batch_size):
            yield data[i:i+batch_size]

# all of the unique reference sequences used by all reads
references = sorted(set(samfile.getrname(read.tid) for read in samfile.fetch()))
referencesLeng = sorted(set(len(fastafile.fetch(reference=str(item)))for item in references))

# loop over all codons in this reference sequence
for reference in references:
    returned_position_lines=[]
    length=0
    refcodonpos=0
    counter=0
    for codon in batch_gen(fastafile.fetch(reference=str(reference)),3):
        length+=3
        markerlist=[]
        referenceid = str(reference)+ ' '
        refnucpos1=0 +(3*refcodonpos)
        refnucpos2=1 +(3*refcodonpos)
        refnucpos3=2 +(3*refcodonpos)
        if 1 <= (refcodonpos+1) <= 9:
            refcodonposid = str(refcodonpos+1)+ " "
        else:
            refcodonposid = str(refcodonpos+1)
        refAAid = str(Seq(codon).translate()[0])
        # loop over all reads to find AAs
        marker_list=[]
        for read in samfile.fetch():
            read_codon=[]
            #loop through base and its pos at the same time
            for seq, pos in zip(read.seq,AlignedSegment.get_reference_positions(read)):
                if pos == refnucpos1:
                    read_codon.append(seq)
                if pos == refnucpos2:
                    read_codon.append(seq)
                if pos == refnucpos3:
                    read_codon.append(seq)
            if any(read_codon) is True:
                if len(read_codon) == 3:
                    counter+=1
                    if ''.join(read_codon) == codon:
                        marker_list.append('.')
                    else:
                        marker_list.append(str(Seq("".join(read_codon)).translate()[0]))
        print (referenceid, refcodonposid, refAAid, counter, ''.join(str(item)for item in marker_list))
        returned_position_lines.append(''.join(str(item)for item in marker_list))

        #Counters
        counter=0
        refcodonpos+=1

    print returned_position_lines
    # forming the substitutions
    AAs = ('A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V','*')
    for AA in AAs:
        position=0
        for line in returned_position_lines:
            position+=1
            count=0
            for readAA in line:
                if readAA==AA:
                    count+=1
            if (count >= 1):
                print count, AA, position

# Wrap up
fastafile.close()
samfile.close()
