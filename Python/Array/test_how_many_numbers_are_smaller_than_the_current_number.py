# coding: utf-8
def smaller_numbers_than_current(nums):
    """
    1365. How Many Numbers Are Smaller Than the Current Number

    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
    That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
    Return the answer in an array.

    Example:
        Input: nums = [8,1,2,2,3]
        Output: [4,0,1,1,3]
        Explanation: 
            For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
            For nums[1]=1 does not exist any smaller number than it.
            For nums[2]=2 there exist one smaller number than it (1). 
            For nums[3]=2 there exist one smaller number than it (1). 
            For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

    https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
    """
    sort_nums = sorted(nums)
    
    return [sort_nums.index(num) for num in nums]

print smaller_numbers_than_current([8,1,2,2,3])

def test_smaller_numbers_than_current_1():
    assert [4,0,1,1,3] == smaller_numbers_than_current([8,1,2,2,3])

def test_smaller_numbers_than_current_2():
    assert [2,1,0,3] == smaller_numbers_than_current([6,5,4,8])

def test_smaller_numbers_than_current_3():
    assert [0,0,0,0] == smaller_numbers_than_current([7,7,7,7])
