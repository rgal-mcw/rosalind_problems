'''
Ryan Gallagher
Problem 38 - ID:LCSQ

A string u is a common subsequence of of strings s and t if the symbols of u appear in order as a subsequence of both s and t. For example, "ACTG" is a common subsequence of "AACCTTGG" and "ACACTGTGA".

Analogously to the definition of longest common substring, u is a longest common subsequence of s and t if there does not exist a longer common subsequence of the two strings. Continueing from our above example, "ACCTTG" is a longest common subsequence of "AACCTTGG" and "ACACTGTGA", as is "AACTGG".


GIVEN: Two DNA strings s and t (each having length at most 1kbp) in FASTA format

RETURN: A longest common subsequence of s and t. (If more than one solution exists, you may return one).
'''

from resources.open_fasta import open_fasta
import numpy as np

sample_file = "./sample_datasets/lcsq_sample.txt"
test_file = "./datasets/rosalind_lcsq.txt"

# Solution adapted from: https://en.wikipedia.org/wiki/Longest_common_subsequence 

def get_C_array(s_list,t_list):
    s_list_fun = s_list
    t_list_fun = t_list

    C = np.zeros((len(s_list_fun),len(t_list_fun)))

    for i in range(1, len(s_list_fun)):
        for j in range(1, len(t_list_fun)):
            if s_list_fun[i] == t_list_fun[j]:
                C[i,j] = C[i-1, j-1] + 1
            else:
                C[i,j] = max(C[i,j - 1], C[i-1, j])
    return C

def backtrack(C, s_list, t_list, i, j):
    out = ""
    while i > 0 and j > 0:

        if s_list[i] == t_list[j]:
            out += s_list[i]

            i -= 1
            j -= 1

        elif C[i, j-1] > C[i-1, j]:
            j-= 1

        else:
            i -= 1


    return out[::-1]


def main():
    fa = open_fasta(test_file)
    s_list = [0] + list(fa[0])
    t_list = [0] + list(fa[1])
    C = get_C_array(s_list, t_list)
    return print(backtrack(C, s_list, t_list, len(s_list)-1, len(t_list)-1))

if __name__ == "__main__":
    main()
