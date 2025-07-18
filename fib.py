#Ryan Gallagher
#Problem 4 - FIB

# This problem has to do with dynamic programming and fibonacci sequences
# The the problem posed has to do with the Fibonacci Rabbits Exercise

# rosalind.info/problems/fib/

# Given: Positive integers n <= 40 and k <= 5

# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair
# and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)

# Formula: F_n = F_n-1 + F_n-2 * k

FIB_FILE = "./datasets/rosalind_fib.txt"

def rabbits(n, k):
    Fn_dict = {}
    for i in range(1,n+1):
        if i == 1 or i == 2:
            Fn_dict[i] = 1
        else:
            Fn_dict[i] = Fn_dict[i-1] + (Fn_dict[i-2] * k)
    return print(Fn_dict[n])


def main():
    return rabbits(34,3)

main()
    
