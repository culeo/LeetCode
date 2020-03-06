# coding: utf-8

def can_place_flowers(flowerbed, n):
    """
    605. Can Place Flowers

    Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
    However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

    Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), 
    and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
    
    Example:
        Input: flowerbed = [1,0,0,0,1], n = 1
        Output: True

    https://leetcode.com/problems/can-place-flowers/
    """
    if n == 0: return True
    if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1: return True

    for i in range(0, len(flowerbed)):
        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        elif i + 1 == len(flowerbed):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
        else:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        if n == 0:
            return True

    return False

print can_place_flowers([0,1,0], 1)

def test_can_place_flowers_1():
    assert True == can_place_flowers([1,0,0,0,1], 1)

def test_can_place_flowers_2():
    assert False == can_place_flowers([1,0,0,0,1], 2)

def test_can_place_flowers_3():
    assert False == can_place_flowers([1,0,0,0,0,1], 2)

def test_can_place_flowers_4():
    assert False == can_place_flowers([0,1,0], 1)
