RNA_codon_table = {
'A': ('GCU', 'GCC', 'GCA', 'GCG'),
'C': ('UGU', 'UGC'),
'D': ('GAU', 'GAC'),
'E': ('GAA', 'GAG'),
'F': ('UUU', 'UUC'),
'G': ('GGU', 'GGC', 'GGA', 'GGG'),
'H': ('CAU', 'CAC'),
'I': ('AUU', 'AUC', 'AUA'),
'K': ('AAA', 'AAG'),
'L': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),
'M': ('AUG',),
'N': ('AAU', 'AAC'),
'P': ('CCU', 'CCC', 'CCA', 'CCG'),
'Q': ('CAA', 'CAG'),
'R': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
'S': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),
'T': ('ACU', 'ACC', 'ACA', 'ACG'),
'V': ('GUU', 'GUC', 'GUA', 'GUG'),
'W': ('UGG',),
'Y': ('UAU', 'UAC'),
'STOP': ('UAA', 'UAG', 'UGA')}

def rna_codon_table():
    return RNA_codon_table
