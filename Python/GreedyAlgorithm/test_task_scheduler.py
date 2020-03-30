# coding: utf-8

import collections

def least_interval(tasks, n):
    """
    621. Task Scheduler

    Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different 
    letters represent different tasks. Tasks could be done without original order. Each task could be done 
    in one interval. For each interval, CPU could finish one task or just be idle.
    However, there is a non-negative cooling interval n that means between two same tasks, there must be at 
    least n intervals that CPU are doing different tasks or just be idle.
    You need to return the least number of intervals the CPU will take to finish all the given tasks.

    Example:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

    https://leetcode.com/problems/task-scheduler/
    """
    if len(tasks) == 0: return 0

    cnts = collections.Counter(tasks)
    sorted_tasks = sorted(cnts, key=cnts.get, reverse=True)
    max_cnt = cnts[sorted_tasks[0]] - 1
    idle_slots = max_cnt * n

    for i in range(1, len(sorted_tasks)):
        task = sorted_tasks[i]
        idle_slots -= min(cnts[task], max_cnt)

    return len(tasks) + idle_slots if idle_slots > 0 else len(tasks)

print least_interval(tasks = ["A","A","A","B","B","B"], n = 2)

def test_least_interval_1():
    assert 8 == least_interval(tasks = ["A","A","A","B","B","B"], n = 2)

def test_least_interval_2():
    assert 5 == least_interval(tasks = ["A","B","C","A","B"], n = 2)