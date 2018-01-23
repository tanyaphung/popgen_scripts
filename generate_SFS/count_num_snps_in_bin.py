from collections import Counter


def count_num_snps_in_bin(num_alleles, variants):
    """
    This script counts the number of SNPs in each bin of the site frequency spectrum, following equation 1.2 from
    John Wakeley book.
    :param num_alleles: the number of alleles in the VCF file, which is equal to twice the number of individuals
    :param variants: a list. Each item in this list is a list where the first item is the position of the variant
    in 1-based coordinate and the rest is the genotypes. The length of this list should be equal to (1 + numAlleles/2)
    :return:
    """

    # Initialize a list. In this this, each item is the count of the number of alternate alleles of each variant.
    # The length of this list is equal to the number of variants you have.
    alt_alleles = []

    for record in variants:
        count = 0
        for genotype in record[1:]:
            if genotype == '0|1' or genotype == '1|0':
                count += 1
            if genotype == '1|1':
                count += 2
        alt_alleles.append(count)

    # zeta: tabulates how many variants appear with frequency 1, 2, 3, etc.
    zeta = Counter(alt_alleles)

    # Initialize eta: a dictionary where
    eta = {}
    for i in range(1, (num_alleles / 2) + 1):
        if i != (num_alleles - i):
            frequency = float(zeta[i] + zeta[num_alleles - i])
            eta[i] = frequency
        if i == (num_alleles - i):
            frequency = float(zeta[i] + zeta[num_alleles - i]) / 2
            eta[i] = frequency

    return eta


