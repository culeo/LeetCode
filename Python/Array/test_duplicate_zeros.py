# coding: utf-8

def duplicate_zeros(arr):
    """
    1089. Duplicate Zeros 

    Given a fixed length array arr of integers, duplicate each occurrence of zero, 
    shifting the remaining elements to the right.
    Note that elements beyond the length of the original array are not written.
    Do the above modifications to the input array in place, do not return anything from your function.

    Example:
        Input: [1,0,2,3,0,4,5,0]
        Output: null
        Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

    https://leetcode.com/problems/duplicate-zeros/
    """
    length = len(arr)
    dups_cnt = 0
    
    for i in range(length):
        
        if i > length - dups_cnt - 1: break
        
        if arr[i] == 0:
            if i == length - dups_cnt - 1:
                arr[length-1] = 0
                length -= 1
                break
            dups_cnt += 1
            
    for i in range(length - dups_cnt - 1, -1, -1):
        if arr[i] == 0:
            dups_cnt -= 1
            arr[i + dups_cnt] = 0
            arr[i + dups_cnt + 1] = 0
        else:
            arr[i + dups_cnt] = arr[i]
            
    return arr

print duplicate_zeros([1,0,2,3,0,4,5,0])

def test_duplicate_zeros_1():
    assert [1,0,0,2,3,0,0,4] == duplicate_zeros([1,0,2,3,0,4,5,0])

def test_duplicate_zeros_2():
    assert [1,2,3] == duplicate_zeros([1,2,3])