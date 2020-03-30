# coding: utf-8

def advantage_count(A, B):
    """
    870. Advantage Shuffle
    
    Given two arrays A and B of equal size, the advantage of A with respect to B is the number 
    of indices i for which A[i] > B[i].
    Return any permutation of A that maximizes its advantage with respect to B.

    Example:
        Input: A = [2,7,11,15], B = [1,10,4,11]
        Output: [2,11,7,15]

    https://leetcode.com/problems/advantage-shuffle/
    """

    B = [(x, i) for i, x in enumerate(B)]
    B.sort()
    A.sort()

    C = [0] * len(A)
    i, j = 0, len(B) - 1

    for x in A:
        if x >= B[i][0]:
            C[B[i][1]] = x
            i += 1
        else:
            C[B[j][1]] = x
            j -= 1

    return C

print advantage_count(A = [12,24,8,32], B = [13,25,32,11])

def test_advantage_count_1():
    assert [2,11,7,15] == advantage_count(A = [2,7,11,15], B = [1,10,4,11])

def test_advantage_count_2():
    assert [24, 32, 8, 12] == advantage_count(A = [12,24,8,32], B = [13,25,32,11])