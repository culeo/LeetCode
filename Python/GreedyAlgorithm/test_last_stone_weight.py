# coding: utf-8

def last_stone_weight(stones):
    """
    1046. Last Stone Weight

    We have a collection of rocks, each rock has a positive integer weight.
    Each turn, we choose the two heaviest rocks and smash them together.  
    Suppose the stones have weights x and y with x <= y.  The result of this smash is:
        If x == y, both stones are totally destroyed;
        If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
    At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

    Example:
        Input: [2,7,4,1,8,1]
        Output: 1
        Explanation: 
            We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
            we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
            we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
            we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

    https://leetcode.com/problems/last-stone-weight/
    """
    if len(stones) == 0: return 0
    if len(stones) == 1: return stones[0]
    
    stones.sort(reverse=True)
    
    if stones[0] == stones[1]:
        return last_stone_weight(stones[2:])
    else:
        stones[1] = stones[0] - stones[1]
        return last_stone_weight(stones[1:])

print(last_stone_weight([2,7,4,1,8,1]))

def test_last_stone_weight_1():
    assert 1 == last_stone_weight([2,7,4,1,8,1])