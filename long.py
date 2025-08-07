'''
Ryan Gallagher
Problem 24 - LONG

For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

GIVEN: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

RETURN: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
'''

sample_file = "./sample_datasets/long_sample.fasta"
test_file = "./datasets/rosalind_long.txt"

with open(test_file) as f:
    fa = f.read().splitlines()
    fa_reads = []
    read = ""
    for line in fa:
        if line.startswith(">"):
            fa_reads.append(read)
            read = ""
        else:
            read += line
    fa_reads.append(read)
    fasta = fa_reads[1:]

def long(fasta):
    fasta = list(set(fasta))
    while len(fasta) > 1:
        found = False
        for read in fasta:

            if found:
                break

            for i in range(len(min(fasta, key=len)), 0, -1):
                
                if found:
                    break

                back = [s[0:i] for s in fasta if s != read]
                front = [s[-i:] for s in fasta if s != read]
                
                back_dict = dict(zip(back, [s for s in fasta if s != read]))
                front_dict = dict(zip(front, [s for s in fasta if s != read]))

                match_front = [s for s in front if read.startswith(s)]
                match_back = [s for s in back if read.endswith(s)]


               
                if len(match_front) > 0:
                    match_front.sort(key=len)
                    best_front = match_front[0]
                    cut = len(front_dict[best_front]) - i 
                    merged_front = front_dict[best_front][0:cut] + read
                    merged_fasta = [s for s in fasta if s != read and s != front_dict[best_front]]
                    merged_fasta.append(merged_front)
                    
                    found = True

                    fasta = list(set(merged_fasta))
                    
                    break

                if len(match_back) > 0:
                    match_back.sort(key=len)
                    best_back = match_back[0]
                    merged_back = read + back_dict[best_back][i:len(back_dict[best_back])]
                    merged_fasta = [s for s in fasta if s != read and s != back_dict[best_back]]
                    merged_fasta.append(merged_back)

                    
                    found = True

                    fasta = list(set(merged_fasta))

                    break
    print(fasta[0]) 

def main():
    return long(fasta)

if __name__ == "__main__":
    main()



