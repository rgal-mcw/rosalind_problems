'''
Ryan Gallagher
Problem 46 - EDIT

Given two strings s and t (of possibly different lengths), the edit distance d_E(s,t) is the minimum number of edit operations needed to transform s into t, where an edit operation is defined as the substitution, insertion, or deletion of a single symbol.

The latter two operations incorporate the case in which a contiguous interval is insterted into or deleted from a string; such an interval is called a gap. For the purpose of this problem, the insertion or deletion of a gap of length k still counts as k distinct edit operations.

GIVEN: Two protein strings s and t in FASTA format (each of length at most 1000 aa)

RETURN: The edit distance d_E(s,t)
'''

from resources.open_fasta import open_fasta
import numpy as np

sample_file = "./sample_datasets/edit_sample.txt"
test_file = "./datasets/rosalind_edit.txt"

def edit_distance(s:str, t:str) -> int:
    rows = len(s) + 1
    cols = len(t) + 1

    distance_matrix = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        distance_matrix[i, 0] = i
    for j in range(1, cols):
        distance_matrix[0,j] = j

    for j in range(1, cols):
        for i in range(1, rows):
            # If the characters are the same, then sub cost is 0. Else, 1
            substitution_cost = 0 if s[i-1] == t[j-1] else 1

            distance_matrix[i, j] = min(distance_matrix[i-1, j] + 1,        # Deletion
                                        distance_matrix[i, j-1] + 1,        # Insertion
                                        distance_matrix[i-1, j-1] + substitution_cost) # substitution_cost
    return print(distance_matrix[rows-1, cols-1])



def main():
    fa = open_fasta(test_file)
    return edit_distance(fa[0], fa[1])

if __name__ == "__main__":
    main()
