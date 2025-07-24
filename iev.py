#Ryan Gallagher
#Problem 13: IEV

# Calculating Expected Offspring

# The description of this problem outlines calculating expected value for a random variable X.

# Can read at rosalind.info/problems/iev

# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possesing each genotype pairing for a given factor. In order, the six given integers represent the numbers of couples having the following genotypes:

# 1. AA-AA
# 2. AA-Aa
# 3. AA-aa
# 4. Aa-Aa
# 5. Aa-aa
# 6. aa-aa

# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring. 

sample = "1 0 0 1 0 1"
test = "17928 18294 19999 16408 19316 16133"

def iev(sample):
    int_list = [17928*2, 18294*2, 19999*2, 16408*2, 19316*2, 16133*2]
    int_probs = [1, 1, 1, 0.75, 0.50, 0]

    print(int_list)
    Exp_dom = []
    for i in range(len(int_list)):
        #print(sum(range(1, int_list[i]+1)))
        Exp_dom.append(int_list[i] * int_probs[i])
    print(sum(Exp_dom))

def main():
    return iev(test)

if __name__ == "__main__":
    main()
