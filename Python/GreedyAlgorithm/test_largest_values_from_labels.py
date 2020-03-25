# coding: utf-8

import collections

def largest_vals_from_labels(values, labels, num_wanted, use_limit):
    """
    1090. Largest Values From Labels

    We have a set of items: the i-th item has value values[i] and label labels[i].
    Then, we choose a subset S of these items, such that:
        |S| <= num_wanted
        For every label L, the number of items in S with label L is <= use_limit.
    Return the largest possible sum of the subset S.

    Example:
        Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
        Output: 9
        Explanation: The subset chosen is the first, third, and fifth item.
 
    https://leetcode.com/problems/largest-values-from-labels/
    """
    
    vls = sorted(zip(values, labels), reverse=True)
    cnts = collections.defaultdict(int)
    ans = 0

    for v, l in vls:
        if num_wanted == 0: break
        if cnts[l] < use_limit:
            ans += v
            num_wanted -= 1
            cnts[l] += 1

    return ans

print largest_vals_from_labels(values = [2,6,3,6,5], labels = [1,1,2,1,1], num_wanted = 3, use_limit = 1)

def test_largest_vals_from_labels_1():
    assert 9 == largest_vals_from_labels(values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1)

def test_largest_vals_from_labels_2():
    assert 12 == largest_vals_from_labels(values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2)

def test_largest_vals_from_labels_3():
    assert 16 == largest_vals_from_labels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1)

def test_largest_vals_from_labels_4():
    assert 24 == largest_vals_from_labels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2)

def test_largest_vals_from_labels_5():
    assert 9 == largest_vals_from_labels(values = [2,6,3,6,5], labels = [1,1,2,1,1], num_wanted = 3, use_limit = 1)



