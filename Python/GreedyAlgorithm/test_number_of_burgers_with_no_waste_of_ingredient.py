# coding: utf-8

def num_of_burgers(tomatoSlices, cheeseSlices):
    """
    1276. Number of Burgers with No Waste of Ingredients

    Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:
        Jumbo Burger: 4 tomato slices and 1 cheese slice.
        Small Burger: 2 Tomato slices and 1 cheese slice.
    Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and 
    the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices 
    and cheeseSlices equal to 0 return [].

    Example 1:
        Input: tomatoSlices = 16, cheeseSlices = 7
        Output: [1,6]
        Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 
        tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.

    https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
    """
    if tomatoSlices & 1 == 1: return []
        
    x = tomatoSlices / 2 - cheeseSlices
    y = cheeseSlices - x
    
    if x < 0 or y < 0: return []
    
    return [x, y]

print num_of_burgers(tomatoSlices = 16, cheeseSlices = 7)

def test_num_of_burgers_1():
    assert [1,6] == num_of_burgers(tomatoSlices = 16, cheeseSlices = 7)

def test_num_of_burgers_2():
    assert [] == num_of_burgers(tomatoSlices = 17, cheeseSlices = 4)

def test_num_of_burgers_3():
    assert [] == num_of_burgers(tomatoSlices = 4, cheeseSlices = 17)

def test_num_of_burgers_4():
    assert [0,0] == num_of_burgers(tomatoSlices = 0, cheeseSlices = 0)

def test_num_of_burgers_1():
    assert [0,1] == num_of_burgers(tomatoSlices = 2, cheeseSlices = 1)
