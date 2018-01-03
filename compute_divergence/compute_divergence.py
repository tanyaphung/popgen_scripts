import os
import sys
from parse_args import *
from get_callable_divergent import *
from compute_divergence_each_BED_line import *


def main():

	args = parse_args()

	# Prepare arguments
	# alignable_intervals is a dict. KEY is the index to look up the sequence. This is the same as the 'Alignment number'
	# from the AXT file. VALUE is a tuple (start, end), 0-based, end is included.
	alignable_intervals = {}
	with open(args.summary_lines, 'r') as f:
		for line in f:
			line = line.rstrip('\n')
			line = line.split(' ')
			alignable_intervals[int(line[0])] = (int(line[2]) - 1, int(line[3]) - 1)

	# species_1_DNA
	with open(args.species_1_DNA, 'r') as f:
		species_1_DNA = [line.rstrip() for line in f]

	# species_2_DNA
	with open(args.species_2_DNA, 'r') as f:
		species_2_DNA = [line.rstrip() for line in f]

	# Identify coordinates (0-based) that are callable and divergent
	all_callable, all_divergent = get_callable_divergent(alignable_intervals = alignable_intervals,
														 species_1_DNA = species_1_DNA, species_2_DNA = species_2_DNA)

	# Set up the output file
	outfile = open(args.outfile, 'w')
	header = ['start', 'end', 'n_sites', 'n_callable', 'n_divergence']
	outfile.write('\t'.join(header) + '\n')

	# Load the BED file. For each line of the BED file, compute divergence and output
	with open(args.BED, 'r') as f:
		for line in f:
			line = line.rstrip('\n')
			line = line.split('\t')

			results = compute_divergence_each_BED_line(start = int(line[1]), end = int(line[2]),
													   all_callable = all_callable, all_divergent = all_divergent)
			outfile.write('\t'.join(results) + '\n')

if __name__ == '__main__':
    main()

