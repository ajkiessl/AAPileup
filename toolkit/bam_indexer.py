#BAM index writer

import pysam
import argparse
import os

parser = argparse.ArgumentParser(description="SAM to BAM converter")
parser.add_argument('-inputbam', required=True)
args = parser.parse_args()

index = pysam.index(args.inputbam)

