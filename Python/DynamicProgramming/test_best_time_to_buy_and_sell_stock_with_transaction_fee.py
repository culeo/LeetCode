# coding: utf-8

def max_profit(prices, fee):
    """
    714. Best Time to Buy and Sell Stock with Transaction Fee(最佳买卖股票时机含手续费)

    Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
    and a non-negative integer fee representing a transaction fee.
    You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. 
    You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
    Return the maximum profit you can make.

    Example 1:
        Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
        Output: 8
        Explanation: The maximum profit can be achieved by:
                    Buying at prices[0] = 1
                    Selling at prices[3] = 8
                    Buying at prices[4] = 4
                    Selling at prices[5] = 9
                    The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
    """
    
    n = len(prices)
    if n < 2: return 0

    fb = list()
    fs = list()

    fb.append(-prices[0])
    fs.append(0)

    for i in range(1, n):
        fb.append(max(fs[i-1]-prices[i], fb[i-1]))
        fs.append(max(fb[i-1]+prices[i]-fee, fs[i-1]))

    return fs[-1]

print max_profit([1,3,2,8,4,9], 2)

def test_max_profit_1():
    assert 8 == max_profit([1,3,2,8,4,9], 2)