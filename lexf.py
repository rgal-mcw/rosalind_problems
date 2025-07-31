# Ryan Gallagher
# Problem 23 - LEXF

# Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation of A = (a1, a2, ..., ak) where a1 < a2 < ... < ak. For instance, the English alphabet is organized as (A, B, ..., Z).

# Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s <Lex t) if the first symbol s[j] that does not match t[j] satisfies sj < tj in A. 

# GIVEN: A collection of at most 10 symbols defining an ordered alphabet, and positive integer n (n<=10)

# RETURN: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symvols in the English alphabet)

import itertools
sample_file = "./sample_datasets/lexf_sample.txt"
test_file = "./datasets/rosalind_lexf.txt"

def lexf(file):
    with open(file) as f:
        read_in = f.read().splitlines()
        letters = read_in[0].split()
        n = int(read_in[1])

        all_perms = list(itertools.product(letters, repeat = n))
        
        for lett in all_perms:
            out = ''
            for let in lett:
                out += let
            print(out)


        return

def main():
    return lexf(test_file)

if __name__ == "__main__":
    main()

