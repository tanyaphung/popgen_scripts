import os
import sys
def computeAF (variants_callable, numAllele):
	variants_AF_dict = {}
	for record in variants_callable: #variants_callable is a list. Each item in this list is a list where the first item is the position in 1-based, and the rest of the items is the genotypes.
		altAlleleCount = 0
		for GT in record[1:]:
			if GT == '0/1' or GT == '1/0': #If your file is phased, change to '0|1' and '1|0'
				altAlleleCount += 1
			if GT == '1/1':
				altAlleleCount += 2
		AF = float(altAlleleCount)/numAllele
		variants_AF_dict[record[0]] = AF
	return variants_AF_dict # return a dictionary where key is the POSITION (1-based) and value is the AF.