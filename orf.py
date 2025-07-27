#Ryan Gallagher
#Problem 18 - ORF

# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA could be translatd into amino acids: three reading frames result from reading the string  itself, whereas three more result from reading its reverse compliment. 

# An open reading frame (ORF) is one which starts from the start codon and ends by the stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

with open("./sample_datasets/orf_sample.fasta") as f:
    f.read
