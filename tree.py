'''
Ryan Gallagher
Problem 31 - TREE

An undirected graph is connected if there is a path connecting any two nodes. A tree is a connected (undirected) graph containing no cycles; this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart.

In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having degree larger than 1 is called an internal node. 

GIVEN: A positive integer n (n <= 1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

RETURN: The minimum number of edges that can added to the graph to produce a tree.
'''

sample_file = "./sample_datasets/tree_sample.txt"
test_file = "./datasets/rosalind_tree.txt"

with open(test_file) as f:
    dataset = f.read().splitlines()



def edges_to_produce_tree(file):
    n = int(file.pop(0))

    edges = [sorted(list(map(int, s.split()))) for s in file]

    return print(n - len(edges) - 1)
    
    ### WRONG BUT WORK LOL 
    list_of_branches = []
    
    for i in range(1,n+1):
        this_branch = [s for s in edges if i in s]
        flattened_this_branch = list(set([x for xs in this_branch for x in xs]))
        flattened_this_branch.sort()
        list_of_branches.append(flattened_this_branch)

    #print(list_of_branches)
    out = []
    out_tracker = set()
    for branch in list_of_branches:
        other_branches = [x for x in list_of_branches if x != branch]
        current_merged_set = set(branch)
        for other_branch in other_branches:
            if not current_merged_set.isdisjoint(other_branch):
                current_merged_set.update(other_branch)
  
        final_branch = sorted(list(current_merged_set))

        if len(final_branch) > 0 and tuple(final_branch) not in out_tracker:
            out.append(final_branch)
            out_tracker.add(tuple(final_branch))

    return print(len(out_no_sublists)-1)



def main():
    return edges_to_produce_tree(dataset)



if __name__ == "__main__":
    main()


