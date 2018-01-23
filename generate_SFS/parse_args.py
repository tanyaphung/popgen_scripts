import argparse


def parse_args():
    """
    Parsing command-line arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='This script generates the counts for a folded site-'
                                                 'frequency-spectrum from a VCF file.')

    parser.add_argument('--vcf_file', required=True,
                        help='REQUIRED. Input the path to a VCF file.'
                             'Note: one should pass in the VCF file post filtering.')

    parser.add_argument('--num_alleles', required=True,
                        help='REQUIRED. Input the number of alleles in your VCF file.'
                             'The number of alleles is equal to twice the number of individuals.')

    parser.add_argument('--outfile', required=True,
                        help='REQUIRED. Input the path to output file.')

    args = parser.parse_args()
    return args
