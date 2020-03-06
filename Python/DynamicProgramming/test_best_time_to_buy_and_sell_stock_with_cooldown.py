# coding: utf-8

def max_profit(prices):
    """
    309. Best Time to Buy and Sell Stock with Cooldown(最佳买卖股票时机含冷冻期)

    Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
    (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
        •You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
        •After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
    
    Example:
        Input: [1,2,3,0,2]
        Output: 3 
        Explanation: transactions = [buy, sell, cooldown, buy, sell]

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
    """

    n = len(prices)
    if n < 2: return 0

    fb = list()
    fs = list()

    fb.append(-prices[0])
    fs.append(0)

    for i in range(1, n):
        fs.append(max(fb[i-1] + prices[i], fs[i-1]))
        if i > 2:
            fb.append(max(fs[i-2] - prices[i], fb[i-1]))
        else:
            fb.append(max(-prices[i], fb[i-1]))
            
    return max(fs)

print max_profit([1,2,3,0,2])

def test_max_profit_1():
    assert 3 == max_profit([1,2,3,0,2])

def test_max_profit_2():
    assert 3 == max_profit([1,4,2])

def test_max_profit_3():
    assert 6 == max_profit([6,1,3,2,4,7])

def test_max_profit_4():
    assert 7 == max_profit([6,1,6,4,3,0,2])