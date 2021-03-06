# coding: utf-8

def largest_sum_of_averages(A, K):
    """
    813. Largest Sum of Averages(最大平均数之和)

    We partition a row of numbers A into at most K adjacent (non-empty) groups, 
    then our score is the sum of the average of each group. What is the largest score we can achieve?
    Note that our partition must use every number in A, and that scores are not necessarily integers.

    Example:
        Input: 
            A = [9,1,2,3,9]
            K = 3
        Output: 20
        Explanation: 
            The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
            We could have also partitioned A into [9, 1], [2], [3, 9], for example.
            That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

    https://leetcode.com/problems/largest-sum-of-averages/
    """
    N = len(A)
    f = [[0] * (K + 1) for i in range(N+1)]

    sums = list()
    sums.append(0)
    for i in range(N):
        sums.append(sums[-1] + A[i])

    for i in range(1, N+1):
        for j in range(1, min(K, i)+1):
            if j == 1:
                f[i][j] = float(sums[i]) / i
            else:
                f[i][j] = max(f[k][j-1] + float(sums[i]-sums[k]) / (i-k) for k in range(j-1, i))

    return f[N][K]

print largest_sum_of_averages([1,2,3,4,5,6,7], 4)

def test_largest_sum_of_averages_1():
    assert 20.0 == largest_sum_of_averages([9,1,2,3,9], 3)

def test_largest_sum_of_averages_2():
    assert 20.5 == largest_sum_of_averages([1,2,3,4,5,6,7], 4)
