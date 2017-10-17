#Convert SAM to BAM

import pysam
import argparse
import os

parser = argparse.ArgumentParser(description="SAm to BAM converter")
parser.add_argument('-inputsam', required=True)
args = parser.parse_args()

file1 = open(os.path.splitext(args.inputsam)[0] + '.bam','w')

rows = pysam.view("-Sb", args.inputsam  )

for r in rows:
    file1.write(r)

file1.close()


