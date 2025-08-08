'''
Ryan Gallagher
Problem 27 - PPER

A partial permutation is an order of only j objects taken from a collection containing n object (i.e. k <= n). For example, only partial permutations of three of the first eight positive integers is given by (5,7,2).

The statistics P(n,k) counts the total number of partial permutations of k objects that can be formed from a collection of n objects. Note that P(n,n) is just the number of permutations of n objects, which we found to be equal to n! = n(n - 1)(n - 2) ... (3)(2).

GIVEN: Positive integers n and k such that 100 >= n > 0 and 10 >= k > 0.
RETURN: The total number of partial permutations P(n,k), modulo 1000000
'''
test_n = 90
test_k = 9

import math
def pper(n,k):
    return int((math.factorial(n) / math.factorial(n - k)) % 1000000)

def main():
    return print(pper(test_n, test_k))

if __name__ == "__main__":
    main()
