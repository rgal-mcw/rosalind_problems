# Ryan Gallagher
# Problem 24 - LGIS

'''
A subsequence of a permutation is a collection of elements of the permutation in the order that they appear.
For example: (5,3,4) is a subsequence of (5,1,3,4,2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease.
For example: Given - (8,2,1,6,5,7,4,3,9), an increasing subsequence is (2,6,7,9),
             and a decreasing subsequence is (8,6,5,4,3). You may verify that these two subsequences are as long as possible.


GIVEN: A positive integer n<= 10000 followed by a permutation pi of lenght n.

RETURN: A longest increasing subsequence of pi, follwed by a longest decreasing subsequence of pi.

'''

sample_file = "./sample_datasets/lgis_sample.txt"
test_file = "./datasets/rosalind_lgis.txt"
with open(test_file) as f:
        file_in = f.read().splitlines()
        n = file_in[0]
        pi = file_in[1].split()
        pi = [int(s) for s in pi]

def lgis(pi):

    m = [None] * len(pi)
    p = [-1] * len(pi)
    l = 0
    for i in range(len(pi)):
        lo = 1
        hi = l
        while lo <= hi:
            mid = (lo + hi) // 2
            if pi[m[mid]] < pi[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        new_l = lo
        p[i] = m[new_l - 1]
        m[new_l] = i

        if new_l > l:
            l = new_l

    s = []
    k = m[l]
    for _ in range(l):
        s.append(pi[k])
        k = p[k]
    return s[::-1]

def lgds(pi):
    neg_pi = [-x for x in pi]
    lis = lgis(neg_pi)
    return [-x for x in lis]



''' 
My Best Try without Resources:
    Thought to take each number in the list and create a pair
    Then, I could look at the last number of one pair and the first of another - if they match, then link.
    I could then have larger and larger groups of numbers to pair. Final product should be one largest linked list.

    NOT EFFICIENT ^^^

def lgis(file):        

        #longest increasing

        # take starting position as pi[i]
        increasing_pairs = []
        for i in range(0, len(pi)):
            # for each starting position, take remaining (pi[i+1:])
            remaining = pi[i:]
            print(f"assembling pairs - starting at {pi[i]} with {len(remaining)} left")
            for j in range(0, len(remaining)):
                if pi[i] < remaining[j]:
                    increasing_pairs.append([pi[i], remaining[j]])
        print("Finished assembling pairs - entering while loop")
        longest = []
        while len(longest) != 1:
            links = 0
            for pair in increasing_pairs:
                for other_pairs in increasing_pairs:
                    if other_pairs != pair:
                        if pair[-1] == other_pairs[0]:
                            print(f"{pair[-1]} matches {other_pairs[0]} - LINKING")
                            new_link = pair + other_pairs[1:]
                            print(f"New link - {new_link}")
                            longest.append(new_link)
                            links = 1
            print(longest) 
            increasing_pairs = longest

            if links == 0:
                longest = [longest[0]]
        longest_inc = ''
        for i in range(0, len(longest[0])):
            longest_inc += f"{longest[0][i]} "
        print(longest_inc)

        #longest decreasing

        # take starting position as pi[i]
        decreasing_pairs = []
        for i in range(0, len(pi)):
            # for each starting position, take remaining (pi[i+1:])
            remaining = pi[i:]
            for j in range(0, len(remaining)):
                if pi[i] > remaining[j]:
                    decreasing_pairs.append([pi[i], remaining[j]])

        longest = []
        while len(longest) != 1:
            links = 0
            for pair in decreasing_pairs:
                for other_pairs in decreasing_pairs:
                    if other_pairs != pair:
                        if pair[-1] == other_pairs[0]:
                            #print(f"{pair[-1]} matches {other_pairs[0]} - LINKING")
                            new_link = pair + other_pairs[1:]
                            #print(f"New link - {new_link}")
                            longest.append(new_link)
                            links = 1
            
            decreasing_pairs = longest

            if links == 0:
                longest = [longest[0]]
        
        longest_dec = ''
        for i in range(0, len(longest[0])):
            longest_dec += f"{longest[0][i]} "
        print(longest_dec)
'''

def main():
    lis = lgis(pi)
    lds = lgds(pi)

    lis_str = ""
    for num in lis:
        lis_str += f"{num} "

    
    lds_str = ""
    for num in lds:
        lds_str += f"{num} "

    print(lis_str)
    print(lds_str)
    return


if __name__ == "__main__":
    main()
