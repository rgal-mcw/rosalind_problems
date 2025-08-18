'''
Ryan Gallagher
Problem 39 - LEXV

Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n . Consider the substring t′=t[1:m]. 

We have two cases:

If s=t′, then we set s <Lex t because s is shorter than t (e.g., APPLE<APPLET).

Otherwise, s≠t′. We define s <Lex t if s<Lex t′ and define s >Lex t if s >Lex t′

(e.g., APPLET<LexARTS because APPL <Lex ARTS).

GIVEN: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n <= 4)

RETURN: All strings of length at most n formed from A, ordered lexicographically.

NOTE: Alphabet order is defined on the order in which the symbols are given. For DNA, D > N > A.
'''

from itertools import product

sample_string = "D N A"
sample_n = 3

test_string = "O H P S B N M I C D" 
test_n = 4

def lexv(string, n):
    chars = string.split()

    character_dict = {chars[i]:i+1 for i in range(0, len(chars))}
    val_dict = {i+1:chars[i] for i in range(0, len(chars))}
    

    all_perms = []
    for m in range(1,n+1):
        val_perms = [v for v in product(character_dict.values(), repeat = m)]
        all_perms += val_perms

    all_perms = sorted(all_perms) # Using this function might be by-passing the intention of this problem, not sure. 
    for tup in all_perms:
        out=''
        for num in tup:
            out += val_dict[num]
        print(out)


def main():
    return lexv(test_string, test_n)

if __name__ == "__main__":
    main()
