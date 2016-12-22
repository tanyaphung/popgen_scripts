import sys
import os
import argparse
import csv

def parse_args():
    """
    Parse command-line arguments
    """
    parser = argparse.ArgumentParser(description="This script generates a collection of of Xkb loci where Xkb is defined by the user")
        
    parser.add_argument(
            "--target_bed", nargs="*",required=True,
            help="REQUIRED. Bed files (no header) containing the regions to be grouped")
    parser.add_argument(
            "--desired_loci_length", type=int, required=True,
            help="REQUIRED. Length of the loci. Examples are 50000 for 50kb loci, 100000 for 100kb loci")
    parser.add_argument("--outfile", required=True, 
                    help="REQUIRED. Name of output file.")

    args = parser.parse_args()
    return args

def group_sites_XkbLoci(intervals, Xkb):
    all_loci = {}
    count = 1
    while len(intervals) != 0:
        current_loci = []
        current_loci_length = 0
        while current_loci_length < Xkb:
            if len(intervals) == 0:
                break
            else:
                current_interval = intervals[0]
                current_interval_length = current_interval[1] - current_interval[0] + 1
                if current_interval_length <= Xkb - current_loci_length:
                    current_loci.append(current_interval)
                    intervals.pop(0)
                    current_loci_length += current_interval_length
                else:
                    need = Xkb - current_loci_length
                    to_append = (current_interval[0], current_interval[0]+need-1)
                    current_loci.append(to_append)
                    current_loci_length += need
                    left = (current_interval[0]+need, current_interval[1])
                    intervals.pop(0)
                    intervals.insert(0, left)
        all_loci[count] = current_loci
        count += 1
    return all_loci

def main():
    # Grab arguments
    args = parse_args()
    intervals = []
    with open(args.target_bed[0],"r") as intervalsFile:
        for line in intervalsFile:
            line = line.split("\t")
            intervals.append((int(line[1]), int(line[2]) - 1))

    Xkb = args.desired_loci_length
    all_loci = group_sites_XkbLoci(intervals, Xkb)
    with open(args.outfile,"w") as f:
        output_list = []
        for key, value in all_loci.iteritems():
            key_all_values = []
            for each_value in value:
                key_all_values.append(each_value[0])
                key_all_values.append(each_value[1])
            to_print_list = [key, min(key_all_values), max(key_all_values)]
            output_list.append(to_print_list)

        w = csv.writer(f)
        w.writerows(output_list)
main()