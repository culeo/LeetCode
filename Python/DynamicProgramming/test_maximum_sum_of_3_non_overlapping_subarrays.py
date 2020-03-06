# coding: utf-8
def max_sum_of_three_subarrays(nums, k):
    """
    689. Maximum Sum of 3 Non-Overlapping Subarrays(三个非重叠子数组的最大和)

    In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
    Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
    Return the result as a list of indices representing the starting position of each interval (0-indexed). 
    If there are multiple answers, return the lexicographically smallest one.

    Example:
        Input: [1,2,1,2,6,7,5,1], 2
        Output: [0, 3, 5]
        Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
                     We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
                
    https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
    """
    N = len(nums)
    sums = [0]

    for num in nums:
        sums.append(sums[-1] + num)

    left = [0] * N
    right = [N-k] * N

    mx = sums[k]
    for i in range(k, N):
        if sums[i+1] - sums[i-k+1] > mx:
            left[i] = i - k + 1
            mx = sums[i+1] - sums[i-k+1]
        else:
            left[i] = left[i-1]

    mx = sums[N]-sums[N-k]
    for i in range(N-k-1, -1, -1):
        if sums[i+k] - sums[i] >= mx:
            right[i] = i
            mx = sums[i+k] - sums[i]
        else:
            right[i] = right[i+1]
    
    mx = 0
    res = [0,0,0]

    for i in range(k, N - 2*k + 1):
        l, r = left[i-1], right[i+k]
        total = (sums[i+k] - sums[i]) + (sums[l+k] - sums[l]) + (sums[r+k] - sums[r])
        if total > mx:
            mx = total
            res = [l,i,r]

    return res

print max_sum_of_three_subarrays([1,2,1,2,6,7,5,1], 2)

def test_max_sum_of_three_subarrays_1():
    assert [0, 3, 5] == max_sum_of_three_subarrays([1,2,1,2,6,7,5,1], 2)