def make_neutral_loci_by_grouping(intervals, Xkb):
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

def make_neutral_loci_predefined_windows(windows, targets):
    all_loci = {}
    for each_window in windows:
        all_loci[each_window] = []
        for each_target in targets:
            if each_target[0] >= each_window[0] and each_target[0] < each_window[1]:
                if (each_target[1]-1) <= (each_window[1]-1):
                    to_append = (each_target[0], each_target[1] - 1)
                    all_loci[each_window].append(to_append)
                if (each_target[1]-1) > (each_window[1]-1):
                    to_append = (each_target[0], (each_window[1]-1))
                    all_loci[each_window].append(to_append)
            if each_target[0] < each_window[0] and each_target[1] > each_window[0]:
                if (each_target[1]-1) < (each_window[1]-1):
                    to_append = (each_window[0], (each_target[1]-1))
                    all_loci[each_window].append(to_append)
                if (each_target[1]-1) > (each_window[1]-1):
                    to_append = (each_window[0], (each_window[1]-1))
                    all_loci[each_window].append(to_append)
    return all_loci

def tabulate_total_sites_each_window(all_loci):
    loci_with_total_sites = {}
    for key in all_loci:
        total_sites = 0
        for each_region in all_loci[key]:
            sites = each_region[1]-each_region[0] + 1
            total_sites += sites
        loci_with_total_sites[key] = total_sites
    return loci_with_total_sites