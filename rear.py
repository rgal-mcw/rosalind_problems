'''
Ryan Gallagher
Problem 42 - REAR

A reversal of a permutation creates a new permutation by inverting some interval of the permutations; (5,2,3,1,4), (5,3,4,1,2), and (4,1,2,3,5) are all reversals of (5,3,2,1,4). The reversal distance between two permutations pi and sigma, written d_rev(pi, sigma) is the minimum number of reversals required to transform pi into sigma (this assumes that pi and sigma have the same length).


GIVEN: A collection of at most 5 pairs of permutations, all of which have length 10.

RETURN: The reversal distance between each permutation pair.


NOTE: This solution was entirely generated from reviewing code from (https://github.com/zonghui0228/Rosalind-Solutions/blob/master/code/rosalind_rear.py).

I made a hearted attempt to learn the BFS algorithm to implement into this problem, but had a ton of trouble. That code is still at the bottom of this solution.
'''
#sample_file = "./sample_datasets/rear_sample.txt"
sample_file = "./datasets/rosalind_rear.txt"

def _get_reverse_array(s):
    reverse_arrays = []
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            r_list = s[i:j+1]
            r_list.reverse()
            reverse_arrays.append(s[:i] + r_list + s[j+1:])
    return reverse_arrays



def _get_reversal_distance(s1, s2, distance):
    """Recursively finds the reversal distance using a bidirectional search."""
    if s1 & s2:
        return distance

    new_s1 = set()
    for s in s1:
        reverse_arrays = _get_reverse_array(list(s))
        for r in reverse_arrays:
            new_s1.add(tuple(r))
            
    new_s2 = set()
    for s in s2:
        reverse_arrays = _get_reverse_array(list(s))
        for r in reverse_arrays:
            new_s2.add(tuple(r))
            
    distance += 2

    if s1 & new_s2:
        return distance - 1
        
    if s2 & new_s1:
        return distance - 1
        
    if new_s1 & new_s2:
        return distance
    
    distance = _get_reversal_distance(new_s1, new_s2, distance)
    return distance

def reversal_distance(p1, p2):
    s1_tuple = tuple(p1)
    s2_tuple = tuple(p2)

    if s1_tuple == s2_tuple:
        return 0

    s1 = {s1_tuple}
    s2 = {s2_tuple}
    distance = 0
    
    return _get_reversal_distance(s1, s2, distance)

def rear(file):

    with open(file) as f:
        collection = f.read().splitlines()
        filtered_collection = [s for s in collection if s != '']

    out = ""
    for i in range(0, len(filtered_collection), 2):
        out += f"{reversal_distance(filtered_collection[i].split(), filtered_collection[i+1].split())} "
    print(out)


def main():
    return rear(sample_file)


if __name__ == "__main__":
    main()




''' FAILED ATTEMPT
def reversal_distance(pi, sigma):

    sigma_position_map = {int(sigma[i]):i for i in range(len(sigma))}
    pi_relabeled = [sigma_position_map[int(s)] for s in pi]
  
    target = tuple(range(len(sigma)))

    if [(tuple(pi_relabeled),0)] == target:
        return 0

    queue_fwd = [(tuple(pi_relabeled), 0)]
    visited_fwd = {tuple(pi_relabeled):0}

    queue_bwd = [(target, 0)]
    visited_bwd = {target:0}


    while queue_fwd and queue_bwd:
        current_perm_fwd, current_dist_fwd = queue_fwd.pop(0)

        for i in range(0, len(current_perm_fwd)):
            for j in range(i+1, len(current_perm_fwd)):
                new_perm_list = list(current_perm_fwd)

                sub_slice = new_perm_list[i:j+1]
                sub_slice.reverse()

                new_perm_list[i:j+1] = sub_slice
                new_perm = tuple(new_perm_list)


                if new_perm in visited_bwd:
                    return current_dist_fwd + 1 + visited_bwd[new_perm] 


                if new_perm not in visited_fwd:
                    visited_fwd[new_perm] = current_dist_fwd + 1
                    queue_fwd.append((new_perm, current_dist_fwd + 1))


        current_perm_bwd, current_dist_bwd = queue_bwd.pop(0)

        # Generate all possible reversals
        for i in range(len(current_perm_bwd)):
            for j in range(i + 1, len(current_perm_bwd)):
                # Create a new permutation by reversing a slice
                new_perm_list = list(current_perm_bwd)
                sub_slice = new_perm_list[i:j+1]
                sub_slice.reverse()
                new_perm_list[i:j+1] = sub_slice
                new_perm = tuple(new_perm_list)

                # Check if the forward search has already found this permutation
                if new_perm in visited_fwd:
                    # If the searches have met, we're done!
                    return current_dist_bwd + 1 + visited_fwd[new_perm]

                # If this is a new permutation, add it to the backward queue and visited dict
                if new_perm not in visited_bwd:
                    visited_bwd[new_perm] = current_dist_bwd + 1
                    queue_bwd.append((new_perm, current_dist_bwd + 1))

'''
