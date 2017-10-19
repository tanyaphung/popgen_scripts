import sys
import os
import argparse
import csv
from compute_AF import *
from compute_diversity import *

def parse_args():
	"""
	Parse command-line arguments
	"""
	parser = argparse.ArgumentParser(description="This script computes pairwise diversity for each region (start, end) in a bed without doing any binning to windows first.")
	parser.add_argument(
    		"--targets_bed", required=True,
            help="REQUIRED. BED file specifying the regions to compute diversity. For example, give the path for the bed file where regions represent neutral region. BED file is 0-based.")
	parser.add_argument(
            "--variants", required=True,
            help="REQUIRED. Variant file. The format should be CHROM POS ind1 ind2 etc. Should be tab delimit. Because of VCF format, it is 1-based. NOTE: this file is the output from vcftools. See script obtain_GT_from_VCF.sh for more details. ")
	parser.add_argument(
			"--numAllele", required=True,
			help="REQUIRED. Indicate the number of alleles, which is equal to the number of individuals in your sample times 2.")
	parser.add_argument("--outfile", required=True, 
			help="REQUIRED. Name of output file.")
	args = parser.parse_args()
	return args

def main():
	args = parse_args()

	targets = []
	with open(args.targets_bed,"r") as targetsFile:
		for line in targetsFile:
			line = line.split("\t")
			targets.append((int(line[1]) + 1, int(line[2])+1)) #convert to 1-bsaed because VCF is 1-based. Note that this is end exclusive.
	
	numAlleles = 0

	variants = [] # this is a list. Each item in this list is a list where the first item is the genomic position (1-based).
	with open(args.variants, "r") as variants_file:
		header = next(variants_file).split("\t")
		numAlleles = int(len(header) - 2)*2
		if numAlleles != int(args.numAllele):
			print "The number of alleles computed is not equal to the number of alleles you think you have. Something is not consistent here. Please check!"
			sys.exit()
		else:
			for line in variants_file:
				line = line.rstrip("\n")
				line = line.split("\t")
				to_append = [int(line[1])] #the position should be in 1-based.
				if all(x!='./.' for x in line[2:]): # remove variants because of missing data
					for i in range(2, len(line)):
						to_append.append(line[i])
				variants.append(to_append)

	# Do stuff:
	## compute allele frequency
	variants_AF_dict = computeAF(variants, numAlleles) #This is a dictionary where the key is the POSITION (1-based) and value is the AF.

	## Generate a set that stores all the positions of the variants. This is so that the lookup can be faster. 
	variantsSet = set()
	for key in variants_AF_dict:
		variantsSet.add(key)

	# Compute diversity for each region in the BED file
	each_target_pi = {} # This is what would be return. This is a dictionary where the KEY is the start and end coordinates in the BED file (Here, return the original 0-based exclusive), and the VALUE is a tuple (Number of callable sites, pi).
	for each_target in targets:
		num_callable = each_target[1] - each_target[0] # does not need to add 1 here because the end is exclusive.
		each_target_AF = [] # This is a list with all the AF for all the variants that appear in this region.
		for each_site in range(each_target[0], each_target[1]):
			if each_site in variantsSet:
				each_target_AF.append(variants_AF_dict[each_site])
		# Compute pi
		pi = computePi(each_target_AF, numAlleles)

		# Add to the dictionary
		each_target_pi[each_target] = (num_callable, pi)

	with open(args.outfile,"w") as f:
		output_list = []
		for key in sorted(each_target_pi):
			output_list.append([key[0]-1, key[1]-1, each_target_pi[key][0], each_target_pi[key][1]])

		w = csv.writer(f, delimiter = "\t")
		w.writerows(output_list)
main()


