# Ryan Gallagher
# Problem 11: cons

# Matrix: M rows x N columns. Matrix A_mn has m rows and n columns

# Say we have a collection of DNA strings, all having the same length n. Their profile matrix is 4 x n matrix P in which P_1_j represents the number of times that 'A' occurs in the jth position of one of the strings. P_2_j represents the number of times that C occurs in the jth positon, and so on.

# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position. If there are mroe than one common symbolm we might have more than one consensus string.

# Given: A collection of at most 10 DNA strings of equal length in FASTA format

# Return: A consensus string and profile matrix for the collection (If several possible consensus strings exist, then you may return any one of them)

# This will be loaded from .fasta format. See ./sample_datasets/

import numpy as np

sample_fasta = "./sample_datasets/cons_sample.fasta"
test_fasta = "./datasets/rosalind_cons.txt"

def get_fasta_matrix(fasta):
    with open(fasta) as f:
        fa = f.read().split() 
        seq = list()
        read = ""
        for line in fa:
            if line.startswith(">"):
                if read:
                    seq.append(read)
                read = ""
            else:
                read += line

        if read:
            seq.append(read)

        fa_filtered_list = list(''.join(seq))
        return np.array(fa_filtered_list).reshape(len(seq), len(seq[1]))
         

def get_profile(matrix):
    profile = np.empty([4, matrix.shape[1]], dtype=int)
    max_string=""
    #print(f"matrix.shape[0]:{matrix.shape[0]}, matrix.shape[1]:{matrix.shape[1]}")
    #print(matrix.shape)
    for i in range(0, matrix.shape[1]):
        A=G=C=T=0
        
        for j in range(0, matrix.shape[0]):
            if matrix[j,i] == 'A':
                A += 1
            if matrix[j,i] == 'G':
                G += 1
            if matrix[j,i] == 'C':
                C += 1
            if matrix[j,i] == "T":
                T += 1
        
        #print(f"A:{A}, C:{C}, G:{G} T:{T}")

        max_dict = {A:'A', G:'G', C:'C', T:'T'}
        maxx = max(A,C,G,T)
        max_string += max_dict[maxx]


        profile[0,i] = A
        profile[1,i] = C
        profile[2,i] = G
        profile[3,i] = T

    
    A_str = ""
    for i in range(0,profile.shape[1]):
        A_str += f"{str(profile[0,i])} "

    C_str = ""
    for i in range(0,profile.shape[1]):
        C_str += f"{str(profile[1,i])} "

    G_str = ""
    for i in range(0, profile.shape[1]):
        G_str += f"{str(profile[2,i])} "

    T_str = ""
    for i in range(0, profile.shape[1]):
        T_str += f"{str(profile[3,i])} "
    
    print(max_string)
    print(f"A: {A_str}")
    print(f"C: {C_str}")
    print(f"G: {G_str}")
    print(f"T: {T_str}")
    return


def main():
    return get_profile(get_fasta_matrix(test_fasta))

main()
