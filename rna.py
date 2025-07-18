#Ryan Gallagher
#Problem 2: RNA

# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

#Given a DNA string t
# corresponding to a coding strand, its transcribed RNA string u
# is formed by replacing all occurrences of 'T' in t with 'U' in u


#Given: A DNA string t
# having length at most 1000 nt.

#Return: The transcribed RNA string of t.

RNA_EX = "GATGGAACTTGACTACGTAAATT"
RNA_file = "./datasets/rosalind_rna.txt"

def T_to_U(rna):
    with open(RNA_file) as f:
        rna_file = f.read()
        return print(rna_file.replace('T', 'U'))

def main():
    return T_to_U(RNA_file)

main()

