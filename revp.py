#Ryan Gallagher
# Problem 21 - REVP

# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse compliment is GCATGC.

# GIVEN: A DNA string of length at most 1 kbp in FASTA format

# RETURN: The position and length of every reverse palindrome in a string having length between 4 and 12. You may return these pairs in any order.

from resources.nucleotide_pairs import get_nucleotide_dict

sample_file = "./sample_datasets/revp_sample.txt"
test_file = "./datasets/rosalind_revp.txt"

def revp(fasta):
    with open(fasta) as f:
        fa = f.readlines()
        seq = list(''.join(fa[1:]).replace("\n", ""))
                
    nucleotide_dict = get_nucleotide_dict()

    for i in range(0, len(seq)):
        out_fin = ""
        for j in range(4+i,13+i):
            if len(seq[i:j]) > 3:
                inst_seq = seq[i:j]
                rev_seq = inst_seq[::-1]
                rev_comp_seq = [nucleotide_dict[elem] for elem in rev_seq]
                
                if inst_seq == rev_comp_seq:
                    out = f"{i+1} {len(inst_seq)}"
                    
                    if out_fin != out:
                        print(out)
                        out_fin = out # No duplicates


def main():
    return revp(test_file)

if __name__ == "__main__":
    main()
