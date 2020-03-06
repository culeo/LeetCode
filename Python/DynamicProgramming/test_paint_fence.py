# coding: utf-8

def num_ways(n, k):
    """
	276	Paint Fence(栅栏染色)

    There is a fence with n posts, each post can be painted with one of the k colors.
    You have to paint all the posts such that no more than two adjacent fence posts have the same color.
    Return the total number of ways you can paint the fence.

    Example:
        Input: n=3, k=2  
        Output: 6
        Explanation:
                    post 1,   post 2, post 3
            way1    0         0       1 
            way2    0         1       0
            way3    0         1       1
            way4    1         0       0
            way5    1         0       1
            way6    1         1       0

    https://leetcode.com/problems/paint-fence
    https://www.lintcode.com/problem/paint-fence/description
    """
    if n == 0: return 0
    if n == 1: return k

    f_d = [0] * n
    f_s = [0] * n
    f_d[0] = k
    f_s[0] = 0

    for i in range(1, n):
        f_d[i] = (f_d[i-1] + f_s[i-1]) * (k-1)
        f_s[i] = f_d[i-1]

    return f_d[n-1] + f_s[n-1]

print num_ways(2, 3)

def test_num_ways_1():
    assert 6 == num_ways(3, 2)

def test_num_ways_2():
    assert 4 == num_ways(2, 2)
