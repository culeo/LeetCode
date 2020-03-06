# coding: utf-8

def can_cross(stones):
    """
    403. Frog Jump(青蛙跳)

    A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. 
    The frog can jump on a stone, but it must not jump into the water.
    Given a list of stones' positions (in units) in sorted ascending order, 
    determine if the frog is able to cross the river by landing on the last stone. Initially, 
    the frog is on the first stone and assume the first jump must be 1 unit.
    If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. 

    Example:
        [0,1,3,5,6,8,12,17]

        There are a total of 8 stones.
        The first stone at the 0th unit, second stone at the 1st unit,
        third stone at the 3rd unit, and so on...
        The last stone at the 17th unit.

        Return true. The frog can jump to the last stone by jumping 
        1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
        2 units to the 4th stone, then 3 units to the 6th stone, 
        4 units to the 7th stone, and 5 units to the 8th stone.

    https://leetcode.com/problems/frog-jump/
    """
    N = len(stones)

    f = dict()
    f[0] = set([1])
    target = stones[-1]

    for stone in stones:
        if f.get(stone) == None: continue
        for sp in f[stone]:
            nt = stone + sp
            if nt == target: 
                return True

            if f.get(nt) == None: 
                f[nt] = set()

            f[nt].add(sp)
            f[nt].add(sp+1)
            
            if sp > 1: 
                f[nt].add(sp-1)

    return False


print can_cross([0,2])

def test_can_cross_1():
    assert True == can_cross([0,1,3,5,6,8,12,17])

def test_can_cross_2():
    assert False == can_cross([0,1,2,3,4,8,9,11])

def test_can_cross_3():
    assert False == can_cross([0,2])