# coding: utf-8

def get_money_amount(n):
    """
    375. Guess Number Higher or Lower II(猜数字大小)

    We are playing the Guess Game. The game is as follows:
    I pick a number from 1 to n. You have to guess which number I picked.
    Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
    However, when you guess a particular number x, and you guess wrong, you pay $x. 
    You win the game when you guess the number I picked.

    Example:
        n = 10, I pick 8.
        First round:  You guess 5, I tell you that it's higher. You pay $5.
        Second round: You guess 7, I tell you that it's higher. You pay $7.
        Third round:  You guess 9, I tell you that it's lower. You pay $9.
        Game over. 8 is the number I picked.
        You end up paying $5 + $7 + $9 = $21.

    https://leetcode.com/problems/guess-number-higher-or-lower-ii/
    """
    f = [[0] * (n+1) for i in range(n+1)]

    for r in range(1, n+1):
        for l in range(r-1, 0, -1):
            f[l][r] = min(k + max(f[l][k-1], f[k+1][r]) for k in range(l, r))

    return f[1][n]

print get_money_amount(10)

def test_get_money_amount_1():
    assert 16 == get_money_amount(10)

def test_get_money_amount_2():
    assert 0 == get_money_amount(1)
