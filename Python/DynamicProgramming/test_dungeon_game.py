# coding: utf-8

def calculate_minimum_hp(dungeon):
    """
    174. Dungeon Game
    The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
    The dungeon consists of M x N rooms laid out in a 2D grid. 
    Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon 
    to rescue the princess.
    The knight has an initial health point represented by a positive integer. 
    If at any point his health point drops to 0 or below, he dies immediately.
    Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; 
    other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
    In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
    Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
    For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal 
    path RIGHT-> RIGHT -> DOWN -> DOWN.

    -2 (K)	-3	 3
    -5	    -10	 1
    10	    30	-5 (P)

    Note:
        The knight's health has no upper bound.
        Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room 
        where the princess is imprisoned.

    https://leetcode.com/problems/dungeon-game/
    """
    ml = len(dungeon)
    if ml == 0: return 0

    nl = len(dungeon[0])
    print ml, nl

    f = [[0] * nl for i in range(ml)]
    print f

    for i in range(ml - 1, -1, -1):
        for j in range(nl - 1, -1, -1):
            print i, j
            if i == ml - 1 and j == nl - 1:
                f[i][j] = 1 - dungeon[i][j]
            elif i == ml - 1:
                f[i][j] = f[i][j+1] - dungeon[i][j]
            elif j == nl - 1:
                f[i][j] = f[i+1][j] - dungeon[i][j]
            else:
                f[i][j] = min(f[i][j+1] - dungeon[i][j], f[i+1][j] - dungeon[i][j])
            f[i][j] = max(1, f[i][j])

    return f[0][0]

def test_calculate_minimum_hp_1():
    assert 7 == calculate_minimum_hp([[-2,-3,3], [-5,-10,1], [10,30,-5]])

def test_calculate_minimum_hp_2():
    assert 1 == calculate_minimum_hp([[0, 0]])