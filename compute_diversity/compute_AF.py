import os
import sys
def computeAF (variants_callable, numAllele):
	variants_AF_dict = {}
	for record in variants_callable:
		altAlleleCount = 0
		for GT in record[1:]:
			if GT == '0/1' or GT == '1/0':
				altAlleleCount += 1
			if GT == '1/1':
				altAlleleCount += 2
		AF = float(altAlleleCount)/numAllele
		variants_AF_dict[record[0]] = AF
	return variants_AF_dict