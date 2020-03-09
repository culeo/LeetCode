# coding: utf-8

def min_cost_to_move_chips(chips):
    """
    1217. Play with Chips

    There are some chips, and the i-th chip is at position chips[i].
    You can perform any of the two following types of moves any number of times (possibly zero) on any chip:
        Move the i-th chip by 2 units to the left or to the right with a cost of 0.
        Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
    There can be two or more chips at the same position initially.
    Return the minimum cost needed to move all the chips to the same position (any position).

    Example:
        Input: chips = [2,2,2,3,3]
        Output: 2
        Explanation: Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.
    
    https://leetcode.com/problems/play-with-chips/
    """
    odd = 0
    even = 0
    for c in chips:
        if c % 2 == 0:
            even += 1
        else:
            odd += 1
    
    return min(odd, even)

print min_cost_to_move_chips([2,2,2,3,3])

def test_min_cost_to_move_chips_1():
    assert 1 == min_cost_to_move_chips([1,2,3])

def test_min_cost_to_move_chips_2():
    assert 2 == min_cost_to_move_chips([2,2,2,3,3])