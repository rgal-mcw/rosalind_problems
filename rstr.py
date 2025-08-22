'''
Ryan Gallagher
Problem 43 - RSTR

Our aim in this problem is to determine the probability with which a given motif (a known promoter, say) occurs randomly constructed genome. Unfortunately, finding this probability is tricky; instead of forming a long genome, we will form a large collection of smaller random strings having the same length as the motif; there smaller strings represent the genome's substring, which we can then test against our motif. 

Given a probabilistic event A, the complement of A is the collection A^c of outcomes not belonging to A. Because A^c takes place precisely when A does not, we may also call A^c "not A". 

For a simple example, if A is the event that a rolled die is 2 or 4, then Pr(A) = 1/3. A^c is the event that the die is 1,3,5, or 6 and Pr(A^c) = 2/3. In general, for any event we will have to identify that Pr(A) + Pr(A^c) = 1. 


GIVEN: A positive integer N <= 100000, a number x between 0 and 1, and a DNA string s of length at most 10bp. 

RETURN: The porbability that if N random DNA strings having the same length as s are constructed with GC content x, then at least one of the stings equals s. We allow for the same random string to be created more than once.
'''
import math

sample_n = 90000
sample_x = 0.6
sample_DNA = "ATAGCCGA"

test_n = 90057
test_x = 0.530788
test_DNA = "AATGTTAGA"


def rstr(n, x, DNA):
    prob_base = {"G":x/2, "C":x/2, "A":((1-x)/2), "T":((1-x)/2)}

    dna_probs = [prob_base[s] for s in list(DNA)]
    probs_of_dna = math.prod(dna_probs)
    probs_of_not_dna = 1 - probs_of_dna
    
    probs_of_not_dna_over_n_samples = probs_of_not_dna ** n

    return print(round(1 - probs_of_not_dna_over_n_samples, 3))
    



def main():
    return rstr(test_n, test_x, test_DNA)

if __name__ == "__main__":
    main()
