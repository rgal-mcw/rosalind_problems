# Ryan Gallagher
# Problem 22 - SPLC

# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation

# GIVEN: A DNA string (of length at most 1kpb) and a collection of substrings of s acting as introns. All string are given in FASTA format.

# RETURN: A protein string resulting from transcribing and translating the exons of s. 

from resources.dna_codons import dna_codon_table

def read_fasta_to_list(fasta):
    with open(fasta) as f:
        fa = f.read().splitlines()
        fa_list = []
        read = ""
        for i in range(0, len(fa)):
            if fa[i].startswith(">"):
                fa_list.append(read)
                fa_list.append(fa[i])

                read = ""
            else:
                read += fa[i]

            
            if i == len(fa)-1:
                fa_list.append(read)

        return fa_list[1:]

def splc(fa_list):
    dna_codon_dict = dna_codon_table()
    seqs = fa_list[1::2]
    sequence = seqs[0]
    introns = seqs[1:]
    for substring in introns:
        if substring in sequence:
            sequence = sequence.replace(substring, '')

    tri_sequence = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
   
    prot_string = ""
    for i in range(0, len(tri_sequence)):
        prot_string += dna_codon_dict[tri_sequence[i]]

    print(prot_string[:-1])


def main():
    return splc(read_fasta_to_list("./datasets/rosalind_splc.txt"))


if __name__ == "__main__":
    main()
