#Ryan Gallagher
#Problem 5: GC

#The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

#DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

#In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.



#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

FASTA = "./datasets/rosalind_gc.txt"

def gc_content_fasta(file):
    with open(file) as f:
        fasta = f.readlines()
        fasta_clean = [s.replace('\n', '') for s in fasta] #remove newline character
        
        fasta_dict = {}
        for line in fasta_clean:
            if line.startswith(">"):
                label = line
                fasta_dict[label] = ""
            else:
                line = fasta_dict[label] + line
                fasta_dict[label] = line
        
        max_value = float("-inf")
        for key in fasta_dict:
            count = 0
            seq = list(fasta_dict[key])
            
            for nt in seq:
                if nt == 'G' or nt == 'C':
                    count += 1
            
            GC_content = count / len(seq)
            if GC_content > max_value:
                max_value = GC_content
                top_key = key

        print(top_key)
        print(max_value * 100)
        return    
            

def main():
    return gc_content_fasta(FASTA)

main()
