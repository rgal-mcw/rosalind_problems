#Ryan Gallagher
#Problem 7 - IPRB

# This problem is about probability and labeled: Mendel's First Law

#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


sample_k=2
sample_m=2
sample_n=2

test_k = 26
test_m = 16
test_n = 22

def pr_dom(k,m,n):
    population = k+m+n

    prob_Dd_Dd = (m / population) * ((m-1) / (population - 1))
    prob_Dd_dd = ((m) / population) * ((n) / (population - 1))
    prob_dd_Dd = ((n) / population) * ((m) / (population - 1))
    prob_dd_dd = (n / population) * ((n-1) / (population - 1))

    prob_dom = 1 - (prob_Dd_Dd * 0.25) - (prob_Dd_dd * 0.5) - (prob_dd_Dd * 0.5) - (prob_dd_dd)

    return print(prob_dom)
    



def main():
    return pr_dom(test_k, test_m, test_n)

main()
