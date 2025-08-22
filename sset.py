'''
Ryan Gallagher
Problem 44 - SSET

This problem introduces sets.

Our first question is to count the total number of possible subsets of a given set.

GIVEN: A positive integer n (n <= 1000). 

RETURN: The total number of subsets {1,2,...,n} modulo 1000000.
'''

test_n = 942

def sset(n):
    return (2 ** n) % 1000000

def main():
    return print(sset(test_n))

if __name__ == "__main__":
    main()
