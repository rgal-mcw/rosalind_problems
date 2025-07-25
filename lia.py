#Ryan Gallagher
#Problem 15 - LIA

# Given: Two positive integers k (k<=7) and N (N <= 2^k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's Second Law hold for the factors


# BIG! - No matter what the specific genotype of the descendant parent is, since the outsider mate is always AaBb, then the change of their offspring being heterozygous Aa/Bb is 50%. So, P(AaBb) is always 25%.

# This is just the binomial formula

from scipy.stats import binom

k = 7
N = 32
prob = 0.25

def lia(N, k, prob):
    pop = 2 ** k
    print(f"Population: {pop}")
    print(f"We want to know the probability of getting at least {N} AaBb out of {pop}")
    if N == 1:
        return 1 - binom.pmf(0, pop, prob)

    for i in range(1, N):
        if i == 1:
            answer = binom.pmf(0, pop, prob)
        
        answer += binom.pmf(i, pop, prob)
    print(f"Answer is 1 minus the probability of getting {N-1} or less AaBb")
    return 1-answer


def main():
    return print(lia(N, k, prob))

if __name__ == "__main__":
    main()
