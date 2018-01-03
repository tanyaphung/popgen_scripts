def compute_divergence_each_BED_line(start, end, all_callable, all_divergent):
    """
    This script computes divergence for each
    :param start: The start coordinate from the BED line where to compute divergence (0-based)
    :param end: The end coordinate from the BED line where to compute divergence (0-based, end is not inclusive)
    :param all_callable:
    :param all_divergent:
    :return:
    """

    callable = 0
    divergent = 0

    for site in range(start, end):
        if site in all_callable:
            callable += 1
        if site in all_divergent:
            divergent += 1

    toreturn = [str(start), str(end), str(end-start), str(callable), str(divergent)]

    return toreturn
