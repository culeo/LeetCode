# coding: utf-8

def climb_stairs(n):
    """
    70. Climbing Stairs

    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    Note: Given n will be a positive integer.

    Example:
        Input: 2
        Output: 2
        Explanation: There are two ways to climb to the top.
            1. 1 step + 1 step
            2. 2 steps

    https://leetcode.com/problems/climbing-stairs/
    """

    f = list([0, 1, 2])
    for i in range(3, n + 1):
        f.append(f[i-1] + f[i-2])   
    return f[n]

def test_climb_stairs_1():
    assert 2 == climb_stairs(2)

def test_climb_stairs_2():
    assert 3 == climb_stairs(3)