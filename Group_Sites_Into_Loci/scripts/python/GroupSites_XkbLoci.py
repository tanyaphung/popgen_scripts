import sys
import os


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
    for key, value in all_loci.iteritems():
        for each_value in value:
            to_print_list = [key, each_value[0], each_value[1]]
            print('\t'.join([str(x) for x in to_print_list]))


def main():
    """ Usage """
    intervals = []
    with open(sys.argv[1]) as intervalsFile:
        for line in intervalsFile:
            line = line.split("\t")
            intervals.append((int(line[1]), int(line[2]) - 1))
    Xkb = int(sys.argv[2])
    group_sites_XkbLoci(intervals, Xkb)
main()