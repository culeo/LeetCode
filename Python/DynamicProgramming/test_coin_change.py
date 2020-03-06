# coding: utf-8

def coin_change(coins, amount):
    """
    322. Coin Change(硬币找零)

    You are given coins of different denominations and a total amount of money amount. 
    Write a function to compute the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.

    Example:
        Input: coins = [1, 2, 5], amount = 11
        Output: 3 
        Explanation: 11 = 5 + 5 + 1

    https://leetcode.com/problems/coin-change/
    """
    if amount < 1: return 0

    f = list()
    f.append(0)
    for i in range(1, amount + 1):
        f.append(0x7FFFFF)
        for c in coins:
            if i >= c:
                f[i] = min(f[i], f[i-c] + 1)
    
    return -1 if f[amount] == 0x7FFFFF else f[amount]

def test_coin_change_1():
    assert 3 == coin_change([1, 2, 5], 11)

def test_coin_change_2():
    assert -1 == coin_change([2], 3)