# coding: utf-8

def min_distance(word1, word2):
    """
    583. Delete Operation for Two Strings(两个字符串的删除操作)

    Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, 
    where in each step you can delete one character in either string.

    Example 1:
        Input: "sea", "eat"
        Output: 2
        Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

    https://leetcode.com/problems/delete-operation-for-two-strings/
    """
    N1 = len(word1)
    N2 = len(word2)

    f = [[0] * (N2 + 1) for i in range(N1 + 1)]

    for i in range(N1+1): f[i][0] = i
    for j in range(N2+1): f[0][j] = j

    for i in range(1, N1+1):
        for j in range(1, N2+1):
            f[i][j] = min(f[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 2), f[i-1][j]+1, f[i][j-1]+1)

    return f[N1][N2]
   
print min_distance('sea', 'ate')

def test_min_distance_1():
    assert 2 == min_distance('sea', 'eat')

def test_min_distance_2():
    assert 4 == min_distance('sea', 'ate')
