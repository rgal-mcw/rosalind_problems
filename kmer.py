'''
Ryan Gallagher
Problem 36 - KMER

For a fixed positive integer k, order all possible k-0mers taken from an underlying alphabet lexicographically. 

Then the k-mer composition of a string s can be represented by an array A for which A[m] denotes the number of time that mth k-mer (with respect to lexicographical order) appears in s.


GIVEN: A DNA string s in FASTA format (having length at most 100kbp)

RETURN: The 4-mer composition of s.

'''

from resources.open_fasta import open_fasta
from itertools import product

sample_file = "./sample_datasets/kmer_sample.txt"
test_file = "./datasets/rosalind_kmer.txt"

def kmer(dna_string, k):
    bases = "ATCG"

    DNA = list(dna_string)
    possible_kmer = []
    for combo in product(bases, repeat=k):
        mer = "".join(combo)
        possible_kmer.append(mer)
    alphabetic_possible_kmer = sorted(possible_kmer)
    possible_kmer_dict = dict.fromkeys(alphabetic_possible_kmer, 0)

    for i in range(0, len(DNA)-k+1):
        k_len_polymer = ''.join(DNA[i:i+k])
        possible_kmer_dict[k_len_polymer] += 1

    out_string = ""
    for count in possible_kmer_dict.values():
        out_string += f"{count} "

    print(out_string)





def main():
    fa = open_fasta(test_file)[0]
    return kmer(fa, 4)


if __name__ == "__main__":
    main()
