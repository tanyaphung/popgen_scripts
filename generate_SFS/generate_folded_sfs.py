from parse_args import *
from count_num_snps_in_bin import *
import csv


def main():

	# Parsing command-line arguments
	args = parse_args()

	# Initialize a list.
	# In this this, each item is the count of the number of alternate alleles of each variant.
    # The length of this list is equal to the number of variants you have.
	variants = []
	with open(args.vcf_file, "r") as f:
		for line in f:
			line = line.rstrip("\n")
			if not line.startswith("#"):
				line = line.split("\t")
				to_append = [int(line[1])]
				for i in range(9, len(line)):
					to_append.append(line[i])
				variants.append(to_append)

	results = count_num_snps_in_bin(args.num_alleles, variants)

	with open(args.outfile, "w") as f:
		out_list = []
		for key in sorted(results):
			out_list.append([key, results[key]])
		w = csv.writer(f)
		w.writerows(out_list)

if __name__ == '__main__':
	main()
