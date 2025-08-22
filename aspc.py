'''
Ryan Gallagher
Problem 45 - ASPC

We saw that the total number of subsets of a set S containing n elements is equal to 2^n.

However, if we intend to count the total number of subsets of S having fixed size k, then we use the combination statistic C(n,k), also written (n choose k).

GIVEN: Positive integers n and m with 0 <= n <= n <= 2000

RETURN: The sum of the combinations C(n,k) for all k satisfying m <= k <= n, modulo 1,000,000. Sum from k=m to n of (n choose k)
'''

from math import factorial

n = 1751
m = 1160

def combination(n, k):
    return factorial(n) // (factorial(k)*(factorial(n-k)))

def aspc(n, m):
    out = 0
    for k in range(m, n+1):
        out += combination(n, k)

    return print(out % 1000000)

def main():
    return aspc(n, m)

if __name__ == "__main__":
    main()
