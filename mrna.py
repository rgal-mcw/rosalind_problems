#Ryan Gallagher
#Problem 17 - MRNA

# For positive integers a and n, a modulo n is the remainder when a is divided by n. Ex: 29 %% 11 = 7 because 29 = 11 * 2 + 7

# MODULO ARITHMETIC: Is the study of +, -, /, * with respect to the modulo operation. We say that a and b are congruent modulo n if a %% n = b %% n; in this case, we say that a and b are congruent %% n.

# Useful identities:
#   if a is congruent to b %% n AND c is congruent to d %% n -> then (a + c is congruent to b + d, %% n), -- and a * c is congruent to b * d, %% n.


# Given: A protein string of length at most 1000 aa
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't negleect the importance of the stop codon in protein translation)

from resources.rna_codons import rna_codon_table

aa_string = "MA" # output is 12 because M = 1, A = 4, STOP = 3. The numbers are the amount of possible codons for that letter. All strings need to end with a STOP codon which there are 3 possibilities for. So 1 x 4 x 3.

with open("./datasets/rosalind_mrna.txt") as f:
    initial_read = f.read()
    test_string = initial_read.replace('\n','')
    print(test_string)

def possible_rna_string(aa_string):
    codon_dict = rna_codon_table()
    aa_list = list(aa_string)
    aa_list.append("STOP")
    codons = [codon_dict[key] for key in aa_list]
    out=1
    for grp in codons:
        out *= len(grp)
    return print(out % 1000000)



def main():
    return possible_rna_string(test_string)

if __name__ == "__main__":
    main()

