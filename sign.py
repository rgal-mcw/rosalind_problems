'''
Ryan Gallagher
Problem 28 - SIGN

A signed permutation of length n is some ordering of the positive integers {1,2,...,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, pi=(5,-3,-2,1,4) is a signed permutation of length 5.

GIVEN: A positive integer n <= 6

RETURN: The total number of signed permutations of length n, followed by a list of all such permutation (you may list the signed permutations in any order)
'''
from math import factorial
from itertools import permutations
sample_n = 2
test_n = 5

def sign(n):
    both_signed_list = []
    for i in range(1,n+1):
        both_signed_list.append(i)
        both_signed_list.append(-i)

    perms = list(permutations(both_signed_list, n))
    signed_perms = set([s for s in perms if len(set([abs(num) for num in s])) == n]) 
    
    #npr = factorial(len(both_signed_list)) / (factorial(len(both_signed_list) - n))
    
    print(len(signed_perms))
    for perm in signed_perms:
        p_string = ""
        for j in range(0, len(perm)):
            p_string += f"{perm[j]} " 
        print(p_string)

def main():
    return sign(test_n)

if __name__ == "__main__":
    main()
