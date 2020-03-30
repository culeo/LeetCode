# coding: utf-8

def num_rescue_boats(people, limit):
    """
    881. Boats to Save People
    
    The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
    Each boat carries at most 2 people at the same time, provided the sum of the weight of those people 
    is at most limit.
    Return the minimum number of boats to carry every given person.  
    (It is guaranteed each person can be carried by a boat.)

    Example:
        Input: people = [1,2], limit = 3
        Output: 1
        Explanation: 1 boat (1, 2)

    https://leetcode.com/problems/boats-to-save-people/
    """
    people.sort()
    
    i, j = 0, len(people)-1
    ans = 0
    
    while i <= j:    
        if people[i] + people[j] <= limit: i += 1
        
        j -= 1
        ans += 1
        
    return ans

print num_rescue_boats(people = [1,2], limit = 3)

def test_num_rescue_boats_1():
    assert 1 == num_rescue_boats(people = [1,2], limit = 3)

def test_num_rescue_boats_2():
    assert 3 == num_rescue_boats(people = [3,2,2,1], limit = 3)

def test_num_rescue_boats_3():
    assert 4 == num_rescue_boats(people = [3,5,3,4], limit = 5)
