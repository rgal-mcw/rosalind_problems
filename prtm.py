# Ryan Gallagher
# Problem 20 - PRTM

# In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.

# The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

# GIVEN: A protein string P of length at most 1000 aa.
# RETURN: The total weight of P. Consult the monoisotopic mass table

# NOTE: The standard unit used in mass spectronomy for measuring mass is the atomic mass unit, known as the dalton (Da) and is defined as one twelfth the mass of a neutral atom of carbon-12

from resources.monoisotopic_mass import *


with open("./datasets/rosalind_prtm.txt") as f:
    test_string = f.read().replace("\n", "")

def protein_weight(prot_string):
    monoisotopic_mass_dict = monoisotopic_mass_table()

    str_list = list(prot_string)
    out_sum = 0
    for prot in prot_string:
        out_sum += monoisotopic_mass_dict[prot]

    return print(round(out_sum, 3))

def main():
    return protein_weight(test_string)

if __name__ == "__main__":
    main()
