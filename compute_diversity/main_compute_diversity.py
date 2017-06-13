import sys
import os
import argparse
import csv
from make_neutral_loci import *
from compute_AF import *
from compute_diversity import *

def parse_args():
	"""
	Parse command-line arguments
	"""
	parser = argparse.ArgumentParser(description="This script computes pairwise diversity.")

	parser.add_argument(
            "--windows_bed", required=True,
            help="REQUIRED. BED file for Xkb window.")
	parser.add_argument(
    		"--targets_bed", required=True,
            help="REQUIRED. BED file specifying the regions to be partitioned into Xkb window. For example, give the path for the bed file where regions represent neutral region")
	parser.add_argument(
            "--variants", required=True,
            help="REQUIRED. Variant file. The format should be CHROM POS ind1 ind2 etc. Should be tab delimit. Because of VCF format, it is 1-based")
	parser.add_argument(
			"--numAllele", required=True,
			help="REQUIRED. Indicate the number of alleles, which is equal to the number of individuals in your sample times 2.")
	parser.add_argument("--outfile", required=True, 
			help="REQUIRED. Name of output file.")
	args = parser.parse_args()
	return args

def main():
	args = parse_args()
	windows = []
	with open(args.windows_bed,"r") as windowsFile:
		for line in windowsFile:
			line = line.split("\t")
			windows.append((int(line[1]), int(line[2])))

	targets = []
	with open(args.targets_bed,"r") as targetsFile:
		for line in targetsFile:
			line = line.split("\t")
			targets.append((int(line[1]), int(line[2])))
	
	numAlleles = 0
	variants = [] # this is a list. Each item in this list is a list where the first item is the genomic position (0-based).
	with open(args.variants, "r") as variants_file:
		header = next(variants_file).split("\t")
		numAlleles = int(len(header) - 2)*2
		if numAlleles != int(args.numAllele):
			print "The number of alleles computed is not equal to the number of alleles you think you have. Something is not consistent here. Please check!"
			exit(1)
		else:
			for line in variants_file:
				line = line.rstrip("\n")
				line = line.split("\t")
				to_append = [int(line[1])-1] # minus 1 because I want to save the position in 0-based format
				if all(x!='./.' for x in line[2:]): # remove variants because of missing data
					for i in range(2, len(line)):
						to_append.append(line[i])
				variants.append(to_append)

	# Do stuff:
	windows_with_targets = make_neutral_loci_predefined_windows(windows, targets)

	windows_with_total_callable_sites = tabulate_total_sites_each_window(windows_with_targets)

	## compute allele frequency
	variants_AF_dict = computeAF(variants, numAlleles)

	variantsSet = set()
	for key in variants_AF_dict:
		variantsSet.add(key)

	winsPi = {}
	for each_window, intervals in windows_with_targets.iteritems():
		if len(intervals) != 0:
			each_window_AF = []
			for each_interval in intervals:
				for each_site in range(each_interval[0], each_interval[1] + 1):
					if each_site in variantsSet:
						each_window_AF.append(variants_AF_dict[each_site])
			pi = computePi(each_window_AF, numAlleles)
			if pi != 'NA':
				piPerSite = float(pi)/windows_with_total_callable_sites[each_window]
			else:
				piPerSite = 'NA'
			winsPi[each_window] = (pi, windows_with_total_callable_sites[each_window], piPerSite)
		else:
			pi = 'NA'
			piPerSite = 'NA'
			winsPi[each_window] = (pi, windows_with_total_callable_sites[each_window], piPerSite)

	with open(args.outfile,"w") as f:
		output_list = []
		for key in sorted(winsPi):
			output_list.append([key[0], key[1], winsPi[key][0], winsPi[key][1], winsPi[key][2]])

		w = csv.writer(f, delimiter = "\t")
		w.writerows(output_list)
main()


