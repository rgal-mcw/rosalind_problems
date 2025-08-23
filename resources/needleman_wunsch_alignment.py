'''
Ryan Gallagher

For problem 46 - EDIT, we're asked to calculate the edit distance between two strings, s and t. 

This problem is much easier if we have an alignment between these two strings. 

This script will code the Needleman-Wunsch Alignment Algorithm for use in this problem specifically, but will likely be useful in the future.

Massive W to Professor Hendrix for an awesome explaintion:
    https://www.youtube.com/watch?v=b6xBvl0yPAY&t=610s


NOTE !!: The traceback could return multiple, equally valid alignments. In my notes, I found that the edit_distance of each option is equal - so I'm not going output all alignments, just one of them.

This could change with further questions.. who knows.


DOUBLE NOTE!!!: Okay this approach was fun and I learned a lot, but the Needleman-Wunsch Algorithm and the Edit Distance are asking two different questions. The N-W Algo MAXIMIZES a score, where the questions asks us to MINIMIZE the cost. These are not the same. My alignment is still good, but not what the questions is asking.

THESE ARE EXTREMELY CLOSE ANSWERS, THOUGH. For one test case, CORRECT = 403 where NW-Algo + HAMM = 405
'''

import numpy as np
import sys

test_s = "PLEASANTLY"
test_t = "MEANLY"


def recursion_relation(left: int, diag: int, top: int, match: bool, gap_penalty: int):
    if match:
        diag += 1

        return max(left+gap_penalty, diag, top+gap_penalty)

    if not match:
        diag -= 1
        return max(left+gap_penalty, diag, top+gap_penalty)


def traceback(scoring_matrix: np.ndarray, s_list, t_list, gap_penalty: int):
    m,n = scoring_matrix.shape

    m = m-1
    n = n-1

    align_0 = []
    align_1 = []
    align_2 = []

    while m != 0 or n != 0:

        # If hitting top row - move left
        if m == 0:
            align_0.append('-')
            align_1.append(' ')
            align_2.append(t_list[n-1])
            n = n-1
            continue

        if n == 0:
            align_0.append(s_list[m-1])
            align_1.append(' ')
            align_2.append('-')
            m = m-1
            continue

        match_score = 1 if s_list[m-1] == t_list[n-1] else -1


        if scoring_matrix[m,n] == scoring_matrix[m-1, n-1] + match_score:
            
            align_0.append(s_list[m-1])
            align_1.append('|' if match_score == 1 else ' ')
            align_2.append(t_list[n-1])

            m = m-1
            n = n-1
            continue

        elif scoring_matrix[m,n] == scoring_matrix[m, n-1] + gap_penalty:

            align_0.append('-')
            align_1.append(' ')
            align_2.append(t_list[n-1])


            n = n-1
            continue

        else:
            
            align_0.append(s_list[m-1])
            align_1.append(' ')
            align_2.append('-')

            m = m-1
            continue

    s_seq = align_0[::-1]
    alignment_mapping = align_1[::-1]
    t_seq = align_2[::-1]

    print("ALIGNMENT:")
    print(" ".join(s_seq))
    print(" ".join(alignment_mapping))
    print(" ".join(t_seq))

    return s_seq, alignment_mapping, t_seq

def needleman_wunsch_alignment(s: str, t: str, gap_penalty=-1):

    if gap_penalty > 0:
        raise Exception("Gap Penalty must be less than 0!")
        sys.exit(1)

    s_list = list(s)
    t_list = list(t)

    # Initialize Scoring Matrix
    # Matrix[Row_index, Column_index]
    scoring_matrix = np.empty((len(s_list)+1, len(t_list)+1), dtype=int)

    # Initialize first row and first column
    scoring_matrix[0,0] = 0
    for i in range(1, len(s_list)+1):
        scoring_matrix[i, 0] = i * gap_penalty
    for j in range(1, len(t_list)+1):
        scoring_matrix[0, j] = j * gap_penalty

    # Begin Filling cells
    match_bool = False
    for i in range(1, len(s_list)+1):
        for j in range(1, len(t_list)+1):

            if s_list[i-1] == t_list[j-1]:
                match_bool = True

            scoring_matrix[i,j] = recursion_relation(left = scoring_matrix[i-1, j],
                                                     diag = scoring_matrix[i-1, j-1],
                                                     top = scoring_matrix[i, j-1],
                                                     match = match_bool,
                                                     gap_penalty = gap_penalty)

            match_bool = False
            
    
    return traceback(scoring_matrix, s_list, t_list, gap_penalty=gap_penalty)
