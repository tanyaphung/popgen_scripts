def get_callable_divergent(alignable_intervals, species_1_DNA, species_2_DNA):
    """
    :param alignable_intervals: a dictionary. KEY is the index to look up where the sequences are. This is the
    "Alignment number" in the AXT summary line. VALUE is a tuple of (start, end) coordinates, 0-based and end inclusive.
    tuple of (start, end). 0-based and end is NOT included.
    :param species_1_DNA: a list where each item is a DNA string.
    :param species_2_DNA: a list where each item is a DNA string.
    :return:
    1. all_callable set: each item in the set is the coordinate (0-based).
    2. all_divergent: each item in the set is the coordinate (0-based).
    """

    nucleotides = ['A', 'T', 'G', 'C']
    all_callable = set()
    all_divergent = set()

    for index, interval in alignable_intervals.items():
        interval_length = interval[1] - interval[0] + 1
        for i in range(0, interval_length):
            if species_1_DNA[index][i] in nucleotides and species_2_DNA[index][i] in nucleotides:
                all_callable.add(interval[0] + i)
                if species_1_DNA[index][i] != species_2_DNA[index][i]:
                    all_divergent.add(interval[0] + i)

    return all_divergent, all_callable