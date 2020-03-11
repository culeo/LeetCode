# coding: utf-8

def max_profit(prices):
    """
    122. Best Time to Buy and Sell Stock II

    Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
    (i.e., buy one and sell one share of the stock multiple times).
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

    Example :
        Input: [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                     Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    """
    
    if len(prices) < 2: return 0
    
    profit = 0
    
    for i in range(0, len(prices) - 1):
        profit += max(prices[i+1]-prices[i], 0)
        
    return profit

print max_profit([7,1,5,3,6,4])

def test_max_profit_1():
    assert 7 == max_profit([7,1,5,3,6,4])

def test_max_profit_2():
    assert 4 == max_profit([1,2,3,4,5])