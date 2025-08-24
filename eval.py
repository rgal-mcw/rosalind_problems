'''
Ryan Gallagher
Problem 47 - EVAL

Say that you place a number of bets on your favorite sports teams. If their chances of winning are 0.3, 0.8, and 0.6, then you should expect on average to win 0.3 + 0.8 + 0.6 = 1.7 of your bets (of course, you can never win exactly 1.7!).

More generally, if we have a collection of events A1,A2,…,An, then the expected number of events occurring is Pr(A1)+Pr(A2)+⋯+Pr(An). In this problem, we extend the idea of finding an expected number of events to finding the expected number of times that a given string occurs as a substring of a random string.

GIVEN: A positive integer n (n <= 1000000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.

RETURN: An array B having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i].
'''

sample_n = 10
sample_s = 'AG'
sample_A = [0.25, 0.50, 0.75]

test_n = 929282 
test_s = 'ATACCTTT'
test_A = [0.000, 0.072, 0.137, 0.238, 0.296, 0.367, 0.390, 0.441, 0.525, 0.615, 0.645, 0.711, 0.773, 0.825, 0.934, 1.000] 

def eval(n, s, A):
    out = []
    for GC in A:
        base_prob = {
                'A':(1-GC)/2,
                'T':(1-GC)/2,
                'G':(GC)/2,
                'C':(GC)/2
                }
        
        substrings = n - len(s) + 1
        
        prob_s = 1
        for char in list(s):
            prob_s *= base_prob[char]
        
        out.append(round((prob_s * substrings), 4)) # TIMES Substring is the key here. 

    out_str = ''
    for item in out:
        out_str += f"{item} "

    return print(out_str)

def main():
    return eval(test_n, test_s, test_A)

if __name__ == "__main__":
    main()
