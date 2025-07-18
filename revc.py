#Ryan Gallagher
#Problem 3: REVC

#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# (e.g., the reverse complement of "GTCA" is "TGAC").

#Given: A DNA string s of length at most 1000 bp.

#Return: The reverse complement s^c of s

REVC_EX = "AAAACCCGGT"
REVC_FILE = "./datasets/rosalind_revc.txt"


def reverse_and_compliment(revc):
    with open(revc) as f:
        revc_file = f.read()
        
        revc_split = list(revc_file)
        count = 0
        for nt in revc_split:
            if nt == "A":
                revc_split[count] = "T"
            if nt == "T":
                revc_split[count] = "A"
            if nt == "C":
                revc_split[count] = "G"
            if nt == "G":
                revc_split[count] = "C"
            count += 1
        
        out_revc = ''.join(revc_split)

        return print(out_revc[::-1])



def main():
    return reverse_and_compliment(REVC_FILE)

main()


