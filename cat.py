'''
Ryan Gallagher
Problem 33 - CAT


A matching in a graph is noncrossing if none of its edges cross eachother. If we assume that the n nodes fo this graph are arranged around a circle, and if we label these nodes with positive integers between 1 and n, then a matching is noncrossing as long as there are not edges {i,j} and {k,l} such that i < k < j < l.

A noncrossing matching of basepair edges in the bonding graph corresponding to an RNA string will correspond to a possible secondary structure of the underlying RNA strand that lacks pseudoknots.

In this problem, we will consider counting noncrossing perfect matchings of basepair edges. As a motivating example of how to count noncrossing perfect matchings, let c_n denote the number of noncrossing perfect matching in the complete graph K_2n. After setting c_0 = 1, we can see that c_1 should equal 1 as well. As for the case of a general n, say that the nodes of K_2n are labeled with the positive integers from 1 to 2n. We can join node 1 to any of the reminaing 2n-1 nodes; yet once we have chosen this node (say m), we cannot add another edge to the matching that corsses the edge {1,m}. As a result, we must match all the edges on one side of {1,m} to each other. This requirement forces m to be even, so that we can write m=2k for some positive integer k.

There are 2k - 2 nodes on one side of {1,m} and 2n-2k nodes on the other side of {1,m}, so that in turn there will be c_k-1 * c_n-k different ways of forming perfect matching on the remaining nodes K_2_n. If we let m vary over all possible n-1 choices of even numbers between 1 and 2n, then we obtain the reccurence relation c_n = sum_k=1^n of c_k-1 * c_n-k. The resulting numbers c_n counting noncrossing perfect matchings in K_2_n are called the Catalan numbers, and they appear in a huge number of other setting. 


GIVEN: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300bp

RETURN: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000
'''


def catalan_count(n):
    n = n//2
    catalan_list = {}

    for m in range(0, n+1):
        if m == 0:
            catalan_list[0]=1
            continue
        c_n = 0
        for k in range(1, len(catalan_list)+1):
            c_k_1 = catalan_list[k-1]
            c_n_k = catalan_list[m-k]
            c_n += (c_k_1 * c_n_k)

        catalan_list[m] = c_n
    
    out_catalan_list = {}
    for key, value in catalan_list.items():
        out_catalan_list[key*2] = value
    
    return out_catalan_list

memo={}
pairs = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}

def count_matchings(s):
    # Base case: empty
    if len(s) == 0:
        return 1

    # Check if substring is solved
    if s in memo:
        return memo[s]

    # If not, calc the substring noncrossing pairs
    total = 0
    for j in range(1, len(s), 2): # must be an odd number to pair
        if pairs[s[0]] == s[j]:
            inner_string = s[1:j]
            outer_string = s[j+1:]
           
            ## KEY IDEA: RECURSION & MEMOIZATION
            inner_count = count_matchings(inner_string)
            outer_count = count_matchings(outer_string)

            total += (inner_count * outer_count)

    # store result for later
    memo[s] = total
    return total


def main():
    with open("./datasets/rosalind_cat.txt") as f:
        f.readline()
        rna_string = ''.join(line.strip() for line in f)

    result = count_matchings(rna_string)

    print(result % 1000000)


if __name__ == "__main__":
    main()


