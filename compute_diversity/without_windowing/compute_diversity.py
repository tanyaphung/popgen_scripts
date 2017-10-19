import os
import sys

def computePi(AF, numAlleles):
	""" 
	This script compute pi using allele frequency. 
	Input 1 is a list where each item is the allele frequency of the variant.
	Input 2 is the number of individuals.
	Return 0 if the list is empty. The reason why 0 should be returned here is that if the list is empty, it means that there are no variants in that region. If there is no variant, then pi should be 0.
	NOTE that this is not per site. In order to get per site pi, need to divide by the callable sites.
	"""
	if len(AF) == 0:
		return 0
	else:
		het_all = 0
		for p in AF:
			het_each = 2*p*(1-p)
			het_all += het_each
		het_all_adjusted = (numAlleles/(numAlleles-1))*het_all
		return het_all_adjusted