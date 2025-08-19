'''
Ryan Gallagher
Problem 41 - PDST

For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the proportion of corresponding symbolds that differ between s1 and s2. 

For a general distance function d on n taxa s1, s2, ..., sn (taxa are often represented by genetic strings), we may encode the distances between pairs of taxa via a distance matrix D in which Dij = d(si, sj). 

GIVEN: A collection of n (n <= 10) DNA strings s1, ..., sn of equal length (at most 1kbp), Strings are given in fasta format. 

RETURN: The matrix D corresponding to the p-distance d_p on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
'''

from resources.open_fasta import open_fasta
import numpy as np

sample_file = "./sample_datasets/pdst_sample.txt"
test_file = "./datasets/rosalind_pdst.txt"

def p_distance(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)

    prop = 0
    for i in range(0, len(s1_list)):
        if s1_list[i] == s2_list[i]:
            prop += 1

    return round((1 - (prop / len(s1_list))), 5)

def pdst(fasta):
    D = np.zeros((len(fasta), len(fasta)))

    for i in range(0, len(fasta)):
        out = ""
        for j in range(0, len(fasta)):
            D[i,j] = p_distance(fasta[i], fasta[j])
            out += f"{D[i,j]} "
        print(out)


def main():
    fa = open_fasta(test_file)
    return pdst(fa)

if __name__ == "__main__":
    main()
