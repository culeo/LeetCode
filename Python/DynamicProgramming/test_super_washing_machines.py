# coding: utf-8

def find_min_moves(machines):
    """
    517. Super Washing Machines(超级洗衣机)

    You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.
    For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine 
    to one of its adjacent washing machines at the same time .
    Given an integer array representing the number of dresses in each washing machine from left to right on the line, 
    you should find the minimum number of moves to make all the washing machines have the same number of dresses. 
    If it is not possible to do it, return -1.

    Example
        Input: [1,0,5]
        Output: 3

        Explanation: 
            1st move:    1     0 <-- 5    =>    1     1     4
            2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
            3rd move:    2     1 <-- 3    =>    2     2     2

    https://leetcode.com/problems/super-washing-machines/
    """

    l = len(machines)
    if l < 2: return 0

    sum = reduce(lambda x, y: x+y, machines)
    if sum % l != 0: return -1
    avg = sum / l

    f = [0] * l
    f[0] = machines[0] - avg
    re = 0

    for i in range(l):
        f[i] = (machines[i] - avg) + f[i-1]
        print f
        if f[i-1] < 0 and f[i] > 0:
            re = max(re, (abs(f[i-1]) + abs(f[i])))
        else:
            re = max(re, abs(f[i]))
            
    return re

def test_fin_find_min_moves_1():
    assert 3 == find_min_moves([1,0,5])

def test_fin_find_min_moves_2():
    assert 2 == find_min_moves([0,3,0])

def test_fin_find_min_moves_3():
    assert 4 == find_min_moves([9,1,8,8,9])