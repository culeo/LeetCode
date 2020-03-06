# coding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rob(root):
    """
    337. House Robber III(打家劫舍)

    The thief has found himself a new place for his thievery again. There is only one entrance to this area,
    called the "root." Besides the root, each house has one and only one parent house. 
    After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
    It will automatically contact the police if two directly-linked houses were broken into on the same night.
    Determine the maximum amount of money the thief can rob tonight without alerting the police.

    Example 1:
        Input: [3,2,3,null,3,null,1]
                3
               / \
              2   3
               \   \ 
                3   1
        Output: 7 
        Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

    https://leetcode.com/problems/house-robber-iii/
    """
    f = dfs(root)
    return f[1]

def dfs(root):
    if root is None: return [0, 0]

    fl = dfs(root.left)
    fr = dfs(root.right)

    dp = list()
    dp.append(fl[1] + fr[1])
    dp.append(max(fl[0] + fr[0] + root.val, dp[0]))
    
    return dp

def test_rob_1():

    n1, n2, n3, n4, n5 = TreeNode(3), TreeNode(2), TreeNode(3), TreeNode(3), TreeNode(1)
    n1.left = n2
    n1.right = n3
    n2.right = n4
    n3.right = n5

    assert 7 == rob(n1)

def test_rob_2():

    n1, n2, n3, n4, n5, n6 = TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(1), TreeNode(3), TreeNode(3)
    n1.left = n2
    n1.right = n3
    n2.right = n4
    n2.right = n5
    n3.right = n6
    
    assert 9 == rob(n1)