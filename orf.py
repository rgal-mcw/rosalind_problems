#Ryan Gallagher
#Problem 18 - ORF

# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA could be translatd into amino acids: three reading frames result from reading the string  itself, whereas three more result from reading its reverse compliment. 

# An open reading frame (ORF) is one which starts from the start codon and ends by the stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

# GIVEN: A DNA string s of length at most 1kbp in FASTA format

# RETURN: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order


from resources.dna_codons import dna_codon_table

sample_path = "./sample_datasets/orf_sample.fasta"
test_path = "./datasets/rosalind_orf.txt"

def fasta_to_dict(path):
    motifs = {}
    current_key = ""
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            if line.startswith('>'):
                current_key = line[1:] 
                motifs[current_key] = "" 
            else:
                motifs[current_key] += line 
    return motifs

def get_dna_compliment(dna_string):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement.get(base, base) for base in reversed(dna_string))


def parse_codon_list(codons):
    dna_codons = dna_codon_table()
    out = ''
    out_list = []
    for i in range(0, len(codons)):
        
        if len(codons[i]) < 3: # kill at end of bp list
            return out_list

        if dna_codons[codons[i]] == "M":
            out = "M"
            for j in range(i+1, len(codons)):

                if len(codons[j]) < 3:
                    break

                if dna_codons[codons[j]] != "*":
                    out += dna_codons[codons[j]]
                else:
                    out_list.append(out)
                    break
    return out_list

def get_dna_protein_ORFs(motifs):
    dna_codons = dna_codon_table()
    seq = list(motifs.values())[0]

    # REVERSE COMPLIMENT
    seq_reverse_compliment = get_dna_compliment(seq)
    
    # 3 possible starting positions going forward

    codons_1 = [seq[i:i+3] for i in range(0, len(seq), 3)]
    codons_2 = [seq[i:i+3] for i in range(1, len(seq), 3)]
    codons_3 = [seq[i:i+3] for i in range(2, len(seq), 3)]

    # 3 possible starting positions with reverse compliment

    codons_1_reversed = [seq_reverse_compliment[i:i+3] for i in range(0, len(seq_reverse_compliment), 3)]
    codons_2_reversed = [seq_reverse_compliment[i:i+3] for i in range(1, len(seq_reverse_compliment), 3)]
    codons_3_reversed = [seq_reverse_compliment[i:i+3] for i in range(2, len(seq_reverse_compliment), 3)]

    out = []
    out.append(parse_codon_list(codons_1))
    out.append(parse_codon_list(codons_2))
    out.append(parse_codon_list(codons_3))

    out.append(parse_codon_list(codons_1_reversed))
    out.append(parse_codon_list(codons_2_reversed))
    out.append(parse_codon_list(codons_3_reversed))

    for at_last in set([j for i in out for j in i]):
        print(at_last)


    return
    
def main():
    my_motifs = fasta_to_dict(test_path)
    return get_dna_protein_ORFs(my_motifs)

if __name__ == "__main__":
    main()
