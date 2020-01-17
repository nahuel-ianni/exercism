def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Sequences must be of equal length.")

    zipped_strands = zip(strand_a, strand_b)
    return sum(n1 != n2 for n1, n2 in zipped_strands)
