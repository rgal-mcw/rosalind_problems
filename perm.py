# Ryan Gallagher
# Problem 19 - PERM

# A permutation of length n is an ordering of the positive integers {1,2,...,n}. For exampple, pi = (5,3,2,1,4) is a permutation of the length 5.

# GIVEN: A positive integer n <= 7

# RETURN: The total number of permutations of length n, followed by a list of all such permutations ()

import math
from itertools import permutations

k = 7

def PERM(k):

    if k < 0:
        return "Factorial is not defined for negative numbers"

    print(math.factorial(k))
    nums = []
    for i in range(1, k+1):
        nums.append(i)

    for p in permutations(nums):
        out = ""
        for i in range(0, len(p)):
            out += f"{str(p[i])} "
        print(out)

def main():
    return PERM(k)

if __name__ == "__main__":
    main()
