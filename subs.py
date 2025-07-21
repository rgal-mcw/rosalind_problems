#Ryan Gallagher
#Problem 10:

# Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s.

# The position of a symbol in a string is the total number of symbols found to its left, including itself. The symbol at position i of s is denoted by s[i].

# A substring of s can be represented as s[j:k], where j and k represent the starting and ending position of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU"

# The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than one as a substring of s.

sample_string = "GATATATGCATATACTT"
sample_substring = "ATAT"

test_string = "GCACGCATCGGAGATGCATCGGTAGCATCGGGCGCATCGGCCGCATCGGCGCATCGGACATGCATCGGATCTGGCATCGGGCATCGGCTAGCTGCGAGCATCGGGCATCGGCCCGCATCGGCGCTTCGCATCGGAGCATCGGGACCCTGCATCGGTACGCATCGGGCATCGGACAGGTGCATCGGCGCATCGGGCATCGGGATGCATCGGGCATCGGATGGCATCGGGCATCGGCGAATTTAGTGCATCGGAAATGCATCGGGCATCGGGCATCGGGCATCGGTTTCGCATCGGGCATCGGCGCATCGGGGATGCATCGGAGCATCGGCTTGCATCGGACGCATCGGCGCCGCATCGGGTGACCGCATCGGGCATCGGGCATCGGTCGCATCGGCAGGCATCGGAACGCATCGGGAACGAGCATCGGAGATATGCATCGGGCATCGGCAGCATCGGCTGCATCGGGAGGAGCATCGGTGCATCGGGCATCGGGCATCGGATAGCATCGGCCGCATCGGGCGCATCGGGGCGCATCGGGGGACCTGCATCGGGCATCGGCGCATCGGGCATCGGGCATCGGGGCATCGGCCAGGGCATCGGCAGCATCGGGCATCGGGAGGCATCGGAATCGTGCATCGGGCATCGGGAGCATCGGCGGCGCATCGGGCATCGGACGCATCGGTGGGTGGCATCGGATGGACGCATCGGGCATCGGCACTTCATCCGGCATCGGATGCATCGGTAATGCATCGGAGCATCGGGGCATCGGACGCATCGGAGAGCATCGGGCATCGGCGTGCATCGGAAACGCATCGGAGCATCGGCGACAGCATCGGAGCATCGGTAGTTGCATCGGGCGCCGCATCGGCGCATCGGTAACGCATCGGGCATCGGTGCATCGGGCATCGG" 

test_substring = "GCATCGGGC"


def motif(substring, string):
    string_list = list(string)
    substring_list = list(substring)
    
    res_list = list()
    first_char = substring_list[0]
    for i in range(0, len(string_list)):
        if string_list[i] == first_char:
            #print(f"{string_list[i]} matched {first_char} at {i+1}")
            #print(string_list[i:i+len(substring_list)])
            if string_list[i:i+len(substring_list)] == substring_list:
                res_list.append(i+1)
    return print(res_list)
        



def main():
    return motif(test_substring, test_string)

main()
    
