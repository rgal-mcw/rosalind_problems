'''
Ryan Gallagher
Problem 40 - MMCH

If we have an RNA string s that does not have the same number of occurrences of 'C' as 'G' and the same number of occurrences of 'A' as 'U', then the bonding graph of s cannot possibly possess perfect matching among its basepair edges.

In light of this fact, we define a maximum matching in a graph as a matching containing as many edges as possible. 

A maximum matching of basepair edges will correspond to a way of forming as many base pairs as possible in an RNA string.

GIVEN: An RNA string s of length at most 100bp.

RETURN: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
'''

from resources.open_fasta import open_fasta
from math import factorial

test_file = "./datasets/rosalind_mmch.txt"

def permu(n,k):
    return factorial(n) // factorial(n - k)

def mmch(seq):
    # matchings of AU graph * matchings of GC graph
    A_count = seq.count("A")
    U_count = seq.count("U")
    G_count = seq.count("G")
    C_count = seq.count("C")

    return permu(max(A_count, U_count), min(A_count, U_count)) * permu(max(G_count, C_count), min(G_count, C_count))



def main():
    fa = open_fasta(test_file)
    return print(mmch(fa[0]))


if __name__ == "__main__":
    main()
