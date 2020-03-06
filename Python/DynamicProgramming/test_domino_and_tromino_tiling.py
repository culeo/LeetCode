# coding: utf-8

def num_tilings(N):
    """
    790. Domino and Tromino Tiling(多米诺和三格骨牌铺瓦问题)

    We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.
        XX  <- domino
        XX  <- "L" tromino
        X
    Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.
    (In a tiling, every square must be covered by a tile. Two tilings are different if and only 
    if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings 
    has both squares occupied by a tile.)

    Example:
        Input: 3
        Output: 5
        Explanation: 
                The five different ways are listed below, different letters indicates different tiles:
                XYZ XXZ XYY XXY XYY
                XYZ YYZ XZZ XYY XXY

    https://leetcode.com/problems/domino-and-tromino-tiling/
    """
    if N == 0: return 0
    if N == 1: return 1
    if N == 2: return 2

    f = [0] * (N+1)
    f[0] = 1
    f[1] = 1
    f[2] = 2

    mod = 10**9 + 7
    for i in range(3, N+1):
        f[i] = (2 * f[i-1] + f[i-3]) % mod

    return int(f[N])

print num_tilings(5)

def test_num_tilings_1():
    assert 24 == num_tilings(5)

def test_num_tilings_2():
    assert 312342182 == num_tilings(30)