__author__ = 'James'


def hamming(strand_a, strand_b):
    """
    Takes in two dna strands and returns the Hamming Difference of the strands.
    :param strand_a: First DNA strand.
    :param strand_b: Second DNA strand.
    :return: Hamming Difference as int.
    """

    # Calculates the minimum and maximum lengths of the two strands.
    length_a = len(strand_a)
    length_b = len(strand_b)
    min_length = min(length_a, length_b)
    max_length = max(length_a, length_b)

    ham = 0  # Initializes ham count.

    for i in range(0, min_length):
        if strand_a[i] != strand_b[i]:
            ham += 1

    # If there is a length difference in the strands, add that to the Hamming Difference.
    ham += max_length - min_length

    return ham