#Sort BAM

import pysam
import argparse
import os

parser = argparse.ArgumentParser(description="Sort BAM")
parser.add_argument('-inputbam', required=True)
args = parser.parse_args()

rows = pysam.sort(args.inputbam, os.path.splitext(args.inputbam)[0] + '.sorted')



