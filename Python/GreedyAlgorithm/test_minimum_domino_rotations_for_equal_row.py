# coding: utf-8

def min_domino_rotations(A, B):
    """
    1007. Minimum Domino Rotations For Equal Row

    In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
    (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
    We may rotate the i-th domino, so that A[i] and B[i] swap values.
    Return the minimum number of rotations so that all the values in A are the same, 
    or all the values in B are the same.
    If it cannot be done, return -1.

    Example:
        Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
        Output: 2
        Explanation: 
            The first figure represents the dominoes as given by A and B: before we do any rotations.
            If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, 
            as indicated by the second figure.

    https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
    """
    
    def check(x):
        a_rotation = 0
        b_rotation = 0

        for i in range(len(A)):
            if A[i] != x and B[i] != x: return - 1
            if A[i] != x: 
                a_rotation += 1
            elif B[i] != x:
                b_rotation += 1

        return min(a_rotation, b_rotation)
   
    rotation = check(A[0])

    if rotation != -1 or A[0] == B[0]:
        return rotation
    
    return check(B[0])
    
print min_domino_rotations(A = [2,1,2,4,2,2], B = [5,2,6,2,3,2])

def test_min_domino_rotations_1():
    assert 2 == min_domino_rotations(A = [2,1,2,4,2,2], B = [5,2,6,2,3,2])

def test_min_domino_rotations_2():
    assert -1 == min_domino_rotations(A = [3,5,1,2,3], B = [3,6,3,3,4])