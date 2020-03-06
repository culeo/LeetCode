# coding: utf-8
 
def min_distance(word1, word2):
    """
    72. Edit Distance(最小编辑距离)

    Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
    You have the following 3 operations permitted on a word:
        1.Insert a character
        2.Delete a character
        3.Replace a character

    Example 1:
        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation: 
            horse -> rorse (replace 'h' with 'r')
            rorse -> rose (remove 'r')
            rose -> ros (remove 'e')

    https://leetcode.com/problems/edit-distance/
    """
    len1 = len(word1)
    len2 = len(word2)
    if len1 == 0: return len2
    if len2 == 0: return len1

    f = [ [0] * (len2 + 1) for i in range(len1 + 1)]
    for i in range(len1 + 1): f[i][0] = i
    for i in range(len2 + 1): f[0][i] = i

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i-1] == word2[j-1]:
                f[i][j] = f[i-1][j-1]
            else: 
                f[i][j] = min(min(f[i-1][j-1], f[i-1][j]), f[i][j-1]) + 1
    return f[len1][len2]

def test_min_distance_1():
    assert 3 == min_distance("horse", "ros")

def test_min_distance_2():
    assert 5 == min_distance("intention", "execution")
