# coding: utf-8

def min_cost(costs):
    """
    265	Paint House II(房屋染色 II)

    There are a row of n houses, each house can be painted with one of the k colors. 
    The cost of painting each house with a certain color is different. 
    You have to paint all the houses such that no two adjacent houses have the same color.
    The cost of painting each house with a certain color is represented by a n x k cost matrix. 
    For example, costs[0][0] is the cost of painting house 0 with color 0; 
    costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

    Example 
        Input:
        costs = [[14,2,11],[11,14,5],[14,3,10]]
        Output: 10
        Explanation:
            The three house use color [1,2,1] for each house. The total cost is 10.
    
    https://leetcode.com/problems/paint-house-ii
    https://www.lintcode.com/problem/paint-house-ii/description
    """

    if len(costs) == 0: return 0
    if len(costs) == 1: return min(costs[0])
    
    n = len(costs)
    k = len(costs[0])

    f = [[0] * k for i in range(n+1)]

    for i in range(1, n+1):
        min1, min2 = 0x7FFFFF, 0x7FFFFF
        idx1, idx2 = 0, 0
        for j in range(k):
            if f[i-1][j] < min1:
                min2 = min1
                idx2 = idx1
                min1 = f[i-1][j]
                idx1 = j
            elif f[i-1][j] < min2:
                min2 = f[i-1][j]
                idx2 = j

        for j in range(k):
            f[i][j] = costs[i-1][j]
            if j == idx1:
                f[i][j] += min2
            else:
                f[i][j] += min1

    return min(f[n])

print min_cost([[14,2,11],[11,14,5],[14,3,10]])

def test_min_cost_1():
    assert 10 == min_cost([[14,2,11],[11,14,5],[14,3,10]])

def test_min_cost_2():
    assert 5 == min_cost([[5]])