'''
Ryan Gallagher
Problem 27 - PROB

An array is a structure containing an ordered collection of objects. We let A[k] denote the k-th value in the array A. You may like to think of an array as simply a matrix having only one row. 

A random string is constructed so that the probability of choosing subsequence symbol is based on a fixed underlying symbol frequency.

GC-content offers us natural symbol frequencies for constructing random DNA strings. If the GC-content is x, then we set the symbol frequencies of C and G equal to x/2 and the symbol frequences of A and T equal to (1-x)/2. For example, if the GC-content is 40%, then as we construct the string, the next symbol is 'G'/'C' with probability 0.2, and the next symbol is 'A'/'T' with probability 0.3. 

In practice, many probabilities wind uo being very small. In order to work with small probabilities, we may plug them into a function that 'blows them up' for the sake of comparison. Specifically, the common logarithm of x (defined for x > 0 and denoted log_10(x)) is the exponent to which we must raise 10 to obtain x. 

See figure 1 for a graph of the common logarithm function y = log_10(x). In this graph, we can see the the logarithm of x-values between 0 and 1 always wind up mapping to y-values between -inf and 0: x-values near 0 have logarithms close to -inf, and x-values close to one have logarithms close to 0. Thus, we will select the common logarithm as our function to 'blow up' small probability values for comparison.


GIVEN: A DNA string s of length at most 100bp and an array A containing at most 20 numbers between 0 and1. 

RETURN: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
'''

from math import log10

sample_file = "./sample_datasets/prob_sample.txt"
test_file = "./datasets/rosalind_prob.txt"

with open(test_file) as f:
    file = f.read().splitlines()
    string = file[0]
    probs = [float(s) for s in file[1].split()]

def prob(string, probs):
    split_string = list(string)
    out_string = ""
    for gc_content in probs: 
        base_probs = {
                "A":(1-gc_content)/2,
                "T":(1-gc_content)/2,
                "G":(gc_content)/2,
                "C":(gc_content)/2
                }

        common_log_probability = 0
        for base in split_string:
           common_log_probability += log10(base_probs[base])

        out_string += f"{str(round(common_log_probability,3))} "
    
    print(out_string)

def main():
    return prob(string, probs)

if __name__ == "__main__":
    main()
