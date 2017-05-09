import os
import sys
import argparse

def parse_args():
	"""
	Parse command-line arguments
	"""
	parser = argparse.ArgumentParser(description="This script tabulates the number of SNPs in each VCF file. This script takes in (1) a VCF file and returns a number indicating the number of SNPs")

	parser.add_argument(
            "--VCF", required=True,
            help="REQUIRED. Input the path to the VCF file")
	args = parser.parse_args()
	return args

def main():
	args = parse_args()

	count = 0
	with open(args.VCF, "r") as f:
		for line in f:
			if not line.startswith("#"):
				count += 1
	print count
main()