#Ryan Gallagher
#Problem 11: FIBD


# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which is the reccurent relation Fn = F_n-1 + F_n-2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male and one female) each subsequent month

# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

# Given: Positive integers n <= 100 and m <= 20
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months

# from ./datasets/rosalind_fibd.txt:
test_n = 98
test_m = 16


def rabbits(n, m):
    ages = [0] * m
    ages[0] = 1 #initialize list of zeros of size m w/ first rabbit inside
    for i in range(n-1):
        new_rabbits = sum(ages[1:])
        ages[1:] = ages[:-1]
        ages[0] = new_rabbits
    return sum(ages)


def main():
    return print(rabbits(n=test_n,m=test_m))

main()
