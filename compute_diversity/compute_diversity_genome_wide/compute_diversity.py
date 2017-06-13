import os
import sys

def computePi(AF, numAlleles):
	""" 
	This script compute pi using allele frequency. 
	Input 1 is a list where each item is the allele frequency of the variant.
	Input 2 is the number of individuals.
	Return NA if the list is empty and het adjusted. 
	NOTE that this is not per site. In order to get per site pi, need to divide by the callable sites.
	"""
	if len(AF) == 0:
		return "NA"
	else:
		het_all = 0
		for p in AF:
			het_each = 2*p*(1-p)
			het_all += het_each
		het_all_adjusted = (numAlleles/(numAlleles-1))*het_all
		return het_all_adjusted