'''
Ryan Gallagher
Problem 37: KMP

Knuth-Morris-Pratt Algorithm

A prefix of length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n]

The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k] that is equal to some prefix s:[1:k-j+1], where j cannot equal 1 (otherwise P[k] would always equal k). By convention P[k]=0.


GIVEN: A DNA string s (length of 100kbp at most) in FASTA format.

RETURN: The failure array of s.
'''

from resources.open_fasta import open_fasta

sample_file = "./sample_datasets/kmp_sample.txt"
test_file = "./datasets/rosalind_kmp.txt"

def kmp(s):
    string = list(s)
    fail = [0] * len(s)
   
    for i in range(1, len(string)):
        if string[i] == string[0]:
            substr = string[i:]
            count = 0
            for k in range(0, len(substr)):
                if substr[k] == string[k]:
                    count += 1

                    if fail[i+k] < count:
                        fail[i+k] = count
                else:
                    break

    out_string = ''
    for f in fail:
        out_string += f'{f} '
    print(out_string)





def main():
    fa = open_fasta(test_file)
    return kmp(fa[0])

if __name__ == "__main__":
    main()
