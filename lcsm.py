# Ryan Gallagher
# Problem 14: LCSM 

# A common substring of a collection of strings is a substring of every member of the collection.

# We say that a common substring is a longest common substring if there does not exist a longer common substring.

# Note that the longest common substring is not necessarily unique; for example "AA" and "CC" are both the longest common substring of "AACC" and "CCAA"


# Given: A collection of k (k <= 100) DNA strings of length at most 1kbp each in FASTA format

# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution)

sample_fasta = "./sample_datasets/lcsm_sample.txt"
test_fasta = "./datasets/rosalind_lcsm.txt"

def lcsm(fasta):
    with open(fasta) as f:
        fa = f.read().split()
        seq = list()
        read = ""
        for line in fa:
            if line.startswith(">"):
                if read:
                    seq.append(read)
                read = ""
            else:
                read += line

        if read:
            seq.append(read)

        shortest_seq = min(seq, key=len)
        seq_except_shortest = [s for s in seq if s != shortest_seq]
        # Substrings of size n
        for n in range(len(shortest_seq), 0, -1):
            substr = [shortest_seq[i:i+n] for i in range(len(shortest_seq) - n + 1)]
            #print(n)
            
            for sub in substr:
                for sequence in seq_except_shortest:
                    found = False
                    if sub in sequence:
                        found = True
                        #print(f"{sub} found in {sequence}. Continuing")
                    if not found:
                        #print(f"{sub} not found in {sequence}. Breaking.")
                        break
                if found:
                    #print(f"{sub} found in all sequences!")
                    return(print(sub))
                


        return print(f"No longest common string found.") 
 
def main():
    return lcsm(test_fasta)


if __name__ == "__main__":
    main()
