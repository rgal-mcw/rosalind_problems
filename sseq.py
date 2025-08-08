'''
Ryan Gallagher
Problem 29 - SSEQ

A subsequence of a string is a collection of symbols in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indicies of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indicies of ACG in TATGCTAAGATC can be represented by (2,5,9).

As a substring can have multiple locations, a subsequence can have multiple collected of indicies, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subseqeunce of AACCGGTT in 8 different ways.

GIVEN: Two DNA string s and t (each of length at most 1kbp) in FASTA format.

RETURN: One collection of indicies of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
'''

from resources.read_fasta import open_fasta 

sample_file = "./sample_datasets/sseq_sample.fasta"
test_file = "./datasets/rosalind_sseq.txt"
def sseq(fasta):
    s = list(fasta[0])
    t = list(fasta[1])

    indicies = ""
    last_index = 1

    for t_base in t:
        s_onwards = s[(last_index-1):]
        for i in range(0, len(s_onwards)):
            
            if t_base == s_onwards[i]:
                indicies += f"{last_index + i} "
                last_index = i + last_index + 1
                break

    print(indicies)



def main():
    return sseq(open_fasta(test_file))

if __name__ == "__main__":
    main()
