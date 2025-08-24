'''
Ryan Gallagher
Problem 48 - MOTZ

Similarly to our definition of the Catalan numbers, the n-th Motzkin number mn counts the number of ways to form a (not necessarily perfect) noncrossing matching in the complete graph Kn containing n nodes. 

To count all possible secondary structures of a given RNA string that do not contain pseudoknots, we need to modify the Motzkin recurrence so that it counts only matchings of basepair edges in the bonding graph corresponding to the RNA string; see Figure 2.

GIVEN: An RNA string s of length at most 300 bp.

RETURN: The total number of noncrossing matchings of basepair edges in the bonding graph of s, modulo 1,000,000.

'''

from resources.open_fasta import open_fasta
import numpy as np

sample_file = "./sample_datasets/motz_sample.txt"
test_file = "./datasets/rosalind_motz.txt"

def is_pair(b1, b2,base_dict):
    return base_dict.get(b2) == b1

def motz(string):
    n = len(string)
    base_dict = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
    

    dp = np.zeros((n,n), dtype=np.int64)
    
    for L in range(1, n+1):
        for i in range(n-L+1):
            j = i + L - 1

            if L == 1:
                dp[i,j] = 1
                continue

            unmatched_val = dp[i, j-1]

            summation=0
            for k in range(i, j):
                if is_pair(list(string)[k], list(string)[j], base_dict):
                    before_val = dp[i, k-1] if k > i else 1 
                    inside_val = dp[k+1, j-1] if k+1 < j else 1 
                    summation += inside_val * before_val

            dp[i,j] = (unmatched_val + summation) % 1000000
    return print(dp[0, n-1])



def main():
    fa = open_fasta(test_file)
    return motz(fa[0])

if __name__ == "__main__":
    main()
