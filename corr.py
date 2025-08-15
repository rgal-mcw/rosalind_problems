'''
Ryan Gallagher
Problem 33 - CORR

As is the case with point mutations, the most common type of sequencing error occurs when a single nucleotide from a read is intepreted incorrectly.

GIVEN: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read in s in the dataset, one of the following applied:
    * s was correctly sequences and appears in the dataset at least twice (possible as a reverse compliment). 
    * s is incorrect, it appears in the dataset exactly once, and its Hamming Distance is 1 with respect to exactly one correct read in the dataset (or its reverse compliment).

RETURN: A list of all corrections in the form '[old read]->[new read]'. (Each correction must be a single symbol subsitution, and you may return the correcitons in any order).
'''

from resources.read_fasta import open_fasta 
pairs = {"A":"T", "T":"A", "C":"G", "G":"C"}


#fasta = "./sample_datasets/corr_sample.fasta"
fasta = "./datasets/rosalind_corr.txt"


def reverse_compliment(string):
    rev_string = list(string[::-1])
    rev_compliment_string = [pairs[s] for s in rev_string]
    return ''.join(rev_compliment_string)

def hamming_distance(first_read, second_read):
    # ASSUMING READS ARE THE SAME LENGTH (given in the problem)
    read1 = list(first_read)
    read2 = list(second_read)

    count = 0
    for i in range(0, len(first_read)):
        if read1[i] != read2[i]:
            count += 1
        
    if count == 1:
        return True

    return False

def corr(list_of_reads):
    reverse_compliment_dict = {x:reverse_compliment(x) for x in list_of_reads}
    
    correct = []
    incorrect = []

    for read in list_of_reads:
        read_count = list_of_reads.count(read)
        rev_read_count = list_of_reads.count(reverse_compliment_dict[read])

        sequence_appearence = read_count + rev_read_count

        if sequence_appearence == 1:
            incorrect.append(read)
        elif sequence_appearence > 1:
            correct.append(read)


    correct_unique = set(correct)
    for bad_read in incorrect:
        hamm_count=0
        correct_read = ""
        for good_read in correct_unique:
            if hamming_distance(bad_read, good_read):
                hamm_count += 1
                correct_read = good_read
            if hamming_distance(bad_read, reverse_compliment_dict[good_read]):
                hamm_count += 1
                correct_read = reverse_compliment_dict[good_read]
        if hamm_count == 1:
            print(f"{bad_read}->{correct_read}")
        
    return


def main():
    
    fa = open_fasta(fasta)
    corr(fa)    


if __name__ == "__main__":
    main()
