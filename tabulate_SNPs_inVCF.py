import os
import sys
import argparse
import gzip

def parse_args():
	"""
	Parse command-line arguments
	"""
	parser = argparse.ArgumentParser(description="This script tabulates the number of SNPs in each VCF file. This script takes in (1) a VCF file and returns a number indicating the number of SNPs and (2) a string to indicate whether the VCF is gzipped or not.")

	parser.add_argument(
            "--VCF", required=True,
            help="REQUIRED. Input the path to the VCF file")

	parser.add_argument(
            "--compressed", required=True,
            help="REQUIRED. Please indicate gzip or not_gzip.")

	args = parser.parse_args()
	return args

def main():
	args = parse_args()

	count = 0
	if args.compressed == 'not_gzip':
		with open(args.VCF, "r") as f:
			for line in f:
				if not line.startswith("#"):
					count += 1
	if args.compressed == 'gzip':
		with gzip.open(args.VCF, "r") as f:
			for line in f:
				if not line.startswith("#"):
					count += 1
	print count
main()