'''
Ryan Gallagher
Problem 26 - PMCH

A matching in a graph G is a collection of edges of G for which no node belongs to more than one edge in the collection. If G contains an even number of nodes (say 2n) then a matching on G is perfect if it contains n edges, which is clearly the maximum possible.

First, let K_n denote the complete graph on 2n labeled nodes, in which every node is connected to every other nnode with an edge, and let p_n denote the total number of perfect matchings in K_n. For a given node x, there are 2_n - 1 ways to join x to the other nodes in the graph, after which point we must for a perfect matching on the remaining 2_n - 2 nodes. This reasoning provides us with the recurrence relation p_n = (2_n - 1) * p_n-1; using the fact that p_1 is 1, this reccurence relation implies the closed equation p_n = (2_n - 1)(2_n - 3)(2_n - 5) ... (3)(1).,

Given an RNA string s=s_1 ... s_n, on a bonding graph for s is formed as follows. First, assign each symbol of s to a node and arrange these nodes in order around the circle, connecting them with the edges called adjacency edges. Second, form all possible edges {A,U} and {C,G}, called basepair edges. Note that a matching contained in the baispair edges will represent one possibility for base pairing interactions in s. For such a matching to exist, s must have the same number of occurrences of 'A' as 'U' and the same numer of occurrences of 'C' as 'G'.

GIVEN: An RNA string s of length at most 80bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

RETURN: The total possible number of perfect matching of basepair edges in the bonding graph of s. 


'''

import math


sample_file = "./sample_datasets/pmch_sample.txt"
test_file = "./datasets/rosalind_pmch.txt"

with open(test_file) as f:
    fa = f.read().splitlines()
    fa_reads = []
    read = ""
    for line in fa:
        if line.startswith(">"):
            fa_reads.append(read)
            read = ""
        else:
            read += line
    fa_reads.append(read)
    fasta = fa_reads[1:]

RNA_compliments = {
        'A':'U',
        'U':'A',
        'C':'G',
        'G':'C'
        }

def make_basepair_edges(base, base_dict):
    base_list=[]
    for i in range(0, len(base_dict)):
        if base_dict[i].startswith(base):
            for j in range(0, len(base_dict)):
                if base_dict[j].startswith(RNA_compliments[base]):
                    base_list.append((base_dict[i],base_dict[j]))

    return base_list

def reccurence_relation(n):
    p_list = [1]
    for i in range(1, n+1):
        pn = ((2*i) - 1) * p_list[i-1]
        p_list.append(pn)
    return print(p_list)

def pmch(fasta):

    '''
    The instructions were somewhat misleading with how to tackle this problem. There is no need to calculate the defined recurrence relation for this problem. It actually turned out to be a pretty simple combinatorics problem once you realize that you're just looking for the count of unique pairs multiplied across two graphs - which is just the [# of A's]! (or U's) multiplied by the [# of C's]! (or G's). Might be a one liner solution. Coded everything else anyways.
    '''

    bases = list(fasta[0])
    base_dict = {i:f"{bases[i]+str(i)}" for i in range(0, len(bases))}

    adjacency_pairs = {f"{base_dict[i]}":f"{base_dict[i+1]}" for i in range(0, len(base_dict)-1)}
   
    AU_list = make_basepair_edges("A", base_dict)
    AU_unique_list = list(set([x for t in AU_list for x in t]))
    CG_list = make_basepair_edges("C", base_dict)
    CG_unique_list = list(set([x for t in CG_list for x in t]))

    reccurence_relation(len(AU_unique_list))
    reccurence_relation(len(CG_unique_list))

    AU_unique_pairs = math.factorial(len(AU_unique_list)//2)
    CG_unique_pairs = math.factorial(len(CG_unique_list)//2)

    return print(AU_unique_pairs * CG_unique_pairs)





def main():
    return pmch(fasta)

if __name__ == "__main__":
    main()
