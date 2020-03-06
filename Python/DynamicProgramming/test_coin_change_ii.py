# coding: utf-8

def coin_change(amount, coins):
    """
    518. Coin Change 2

    You are given coins of different denominations and a total amount of money. Write a function to compute the number 
    of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

    Example 1:
        Input: amount = 5, coins = [1, 2, 5]
        Output: 4
        Explanation: there are four ways to make up the amount:
                     5=5
                     5=2+2+1
                     5=2+1+1+1
                     5=1+1+1+1+1

    https://leetcode.com/problems/coin-change-2/
    """
    if amount < 1: return 1

    f = [0] * (amount + 1)
    f[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            f[i] += f[i-coin]

    return f[amount]

print coin_change(5, [1, 2, 5])

def test_coin_change_1():
    assert 4 == coin_change(5, [1, 2, 5])

def test_coin_change_2():
    assert 1 == coin_change(0, [])