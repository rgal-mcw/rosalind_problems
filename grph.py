#Ryan Gallagher
#Problem 12: GRPH

# Title: A Brief Introduction to Graph Theory

# A graph whopse nodes have all been labeled can be represented by an adjecency list, in which each row of the list contains the two nodes labels corresponding to a unique edge.

# A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge from its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but NOT by (w,v)). A directed loop is a directed edge of the form (v,v).

# For a collection of string and a positive integer k, the overlap graph for the string is a directed graph O_k in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k previx of t, as long as s != t; we demand s!=t to prevent directed loops in the overlap graph (althoug directed cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length at most 10kbp.

# Return: The adjacency list corresponding to O_3. You may return edges in any order. 

#fasta = "./sample_datasets/grph_sample.txt"
fasta = "./datasets/rosalind_grph.txt"

def overlap_graph(fasta, suffix_length):
    with open(fasta) as f:
        fa = f.read().split() 
        #print(fa)
        seq = list()
        read = ""
        for line in fa:
            if line.startswith(">"):
                if len(seq) != 0:
                    seq.append(read)
                seq.append(line)
                read = ""
            else:
                read += line

        if read:
            seq.append(read)
       
        seq_dict = dict(zip(seq[::2],seq[1::2]))
        read_names = seq[::2]
        output = list()
        for name in read_names:
            tail = ''.join((list(seq_dict[name])[-suffix_length:]))
            head = ''.join((list(seq_dict[name])[:suffix_length]))
            clean_name = name.replace(">",'')
            #print(f"The first {suffix_length} of {clean_name}:{seq_dict[name]} is -- {head}")
            #print(f"The last {suffix_length} of {clean_name}:{seq_dict[name]} is -- {tail}")

            for name_2 in read_names:
                clean_name2 = name_2.replace(">",'')
                if name_2 != name:
                    head_2 = ''.join((list(seq_dict[name_2])[:suffix_length])) 
                    if tail == head_2:
                        output.append(f"{clean_name} {clean_name2}")
                        print(f"{clean_name} {clean_name2}")
        #print(output)



def main():
    return overlap_graph(fasta, 3)

main()
