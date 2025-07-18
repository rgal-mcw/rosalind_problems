# Ryan Gallagher
# Problem 1 - DNA

## PROBLEM:
#A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

#Given: A DNA string s of length at most 1000 nt.

#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
## --------------------

dna_ex = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
dna = "./datasets/rosalind_dna.txt"

def count_nt(dna_file):
    with open(dna_file, 'r') as d:
        nt_dict = {}
        d_string = list(d.read())
        for i in set(d_string):
            nt_dict[i] = d_string.count(i)

        A = nt_dict['A']
        C = nt_dict['C']
        G = nt_dict['G']
        T = nt_dict['T']

        return print(f"{A} {C} {G} {T}")

def main():
    return count_nt(dna)

main()
