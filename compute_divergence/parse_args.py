def parse_args():
    """
    Parse command-line arguments
    :return: 
    """

    parser = argparse.ArgumentParser(description="This script computes the number of sites that are different between"
                                                 "two species in each line of the BED file. "
                                                 "NOTE: this is NOT the non-overlapping window approach.")

    parser.add_argument("--BED", required=TRUE,
                        help="REQUIRED. Path to the BED file that represents the regions to compute divergence."
                             "For example, this BED file specifies putatively neutral regions.")

    parser.add_argument("--summary_lines", required=TRUE,
                        help="REQUIRED. Path to the summary line of the AXT file.")

    parser.add_argument("--species_1_DNA", required=TRUE,
                        help="REQUIRED. Path to the DNA sequence of species 1 (this file is extracted from the AXT file.")

    parser.add_argument("--species_2_DNA", required=TRUE,
                        help="REQUIRED. Path to the DNA sequence of species 2 (this file is extracted from the AXT file.")

    parser.add_argument("--outfile", required=TRUE,
                        help="REQUIRED. Path to the output file.")

    args = parser.parse_args()
    return args