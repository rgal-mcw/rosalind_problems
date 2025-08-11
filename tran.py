'''
Ryan Gallagher
Problem 31 - TRAN

For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols when calculating the Hamming distance.

Point mutations can be divided into two types: transitions and transversions. A transition subsititutes one purine for another (A <-> G) or one pyrmadine for another (C <-> T). A transversion is the change from a purine to a pyrmadine, or vice-versa.


GIVEN: Two DNA strings s1 and s2 of equal length (1kb at most)

RETURN: The transition/transversion ratio R(s1, s2)

'''

from resources.read_fasta import open_fasta
import sys

sample_file = "./sample_datasets/tran_sample.txt"
test_file = "./datasets/rosalind_tran.txt"
fasta = open_fasta(test_file)

def tran(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    purine_pyrmadine_pairs = {
            "C":"T",
            "T":"C",
            "A":"G",
            "G":"A"
            }

    transition_count = 0
    transversion_count = 0

    if len(s1) != len(s2):
        raise Exception("s1 and s2 are not the same length!")
        sys.exit(1)

    for i in range(0, len(s1)):
        if s1[i] == s2[i]:
            continue
        elif purine_pyrmadine_pairs[s1[i]] == s2[i]:
            transition_count += 1
        else:
            transversion_count += 1

    return print(transition_count / transversion_count)


def main():
    return tran(fasta[0], fasta[1])

if __name__ == "__main__":
    main()
