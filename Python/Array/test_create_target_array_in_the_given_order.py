# coding: utf-8

def create_target_array(nums, index):
    """
    1389. Create Target Array in the Given Order

    Given two arrays of integers nums and index. Your task is to create target array under the following 
    rules:
        Initially target array is empty.
        From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
        Repeat the previous step until there are no elements to read in nums and index.
    Return the target array.
    It is guaranteed that the insertion operations will be valid.

    Example:
        Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
        Output: [0,4,1,3,2]
        Explanation:
            nums       index     target
            0            0        [0]
            1            1        [0,1]
            2            2        [0,1,2]
            3            2        [0,1,3,2]
            4            1        [0,4,1,3,2]
            
    https://leetcode.com/problems/create-target-array-in-the-given-order/
    """
    ans = []
    for i in range(len(nums)):
        ans.insert(index[i], nums[i])
    return ans

print create_target_array(nums = [0,1,2,3,4], index = [0,1,2,2,1])

def test_create_target_array_1():
    assert [0,4,1,3,2] == create_target_array(nums = [0,1,2,3,4], index = [0,1,2,2,1])

def test_create_target_array_2():
    assert [0,1,2,3,4] == create_target_array(nums = [1,2,3,4,0], index = [0,1,2,3,0])

def test_create_target_array_3():
    assert [1] == create_target_array(nums = [1], index = [0])
