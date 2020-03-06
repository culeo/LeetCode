# coding: utf-8

def find_max_form(strs, m, n):
    """
    474. Ones and Zeroes(一和零)

    In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
    For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, 
    there is an array with strings consisting of only 0s and 1s.
    Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. 
    Each 0 and 1 can be used at most once.

    Note:
        The given numbers of 0s and 1s will both not exceed 100
        The size of given string array won't exceed 600.

    Example 1:
        Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
        Output: 4
        Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

    https://leetcode.com/problems/ones-and-zeroes/
    """
    f = [[0] * (n+1) for i in range(m+1)]
    for s in strs:
        zeroes, ones = 0, 0
        for c in s:
            if c == '0':
                zeroes += 1
            else:
                ones += 1
        
        for i in range(m, zeroes-1, -1):
            for j in range(n, ones-1, -1):
                f[i][j] = max(f[i][j], f[i-zeroes][j-ones] + 1)

    return f[m][n]

print find_max_form(["10","0001","111001","1","0"], 5, 3)

def test_find_max_form_1():
    assert 4 == find_max_form(["10","0001","111001","1","0"], 5, 3)

def test_find_max_form_2():
    assert 2 == find_max_form(["10","0","1"],1,1)
