# coding: utf-8

def fib(N):
    """
    509. Fibonacci Number
    
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
    such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
        F(0) = 0,   F(1) = 1
        F(N) = F(N - 1) + F(N - 2), for N > 1.
        Given N, calculate F(N).

    Example:
        Input: 2
        Output: 1
        Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    https://leetcode.com/problems/fibonacci-number/
    """
    fibs = [0, 1]
    
    for i in range(2, N + 1):
        fibs.append(fibs[i-1]+fibs[i-2])
    
    return fibs[N]

print fib(2)

def test_fib_1():
    assert 1 == fib(2)

def test_fib_2():
    assert 2 == fib(3)

def test_fib_3():
    assert 3 == fib(4)