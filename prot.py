#Ryan Gallagher
#Problem 8: PROT

# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

# The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

# Return: The protein string encoded by s.

# I've added the codon table as a dictionary in a python script in the `resources` directory
from resources.rna_codons import rna_codon_table

sample_rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
prot_file = "./datasets/rosalind_prot.txt"

def get_proteins(rna_string):
    with open(rna_string) as f:
        rna = f.read()
        codon_table = rna_codon_table()
        n = 3
        codon_string = ''
        three_seq = [rna[i:i+n] for i in range(0, len(rna), n)]
        for seq in three_seq:
            for key, val in codon_table.items():
                if seq in val:
                    codon_string += key
        return print(codon_string)

def main():
    return get_proteins(prot_file)

main()
