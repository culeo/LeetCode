# coding: utf-8

def check_record(n):
    """
    552. Student Attendance Record II(学生签到记录)

    Given a positive integer n, return the number of all possible attendance records with length n, 
    which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.
    A student attendance record is a string that only contains the following three characters:
        'A' : Absent.
        'L' : Late.
        'P' : Present.
        A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

    Example:
        Input: n = 2
        Output: 8 
        Explanation:
            There are 8 records with length 2 will be regarded as rewardable:
            "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
            Only "AA" won't be regarded as rewardable owing to more than one absent times. 
    
    https://leetcode.com/problems/student-attendance-record-ii/
    """
    if n == 0: return 0
    
    f = [[1,1,0], [1,0,0]]
    mod = 10**9 + 7

    for i in range(1, n):
        t = [[0,0,0],[0,0,0]]
        t[0][0] = sum(f[0]) % mod
        t[0][1] = f[0][0]
        t[0][2] = f[0][1]
        t[1][0] = (t[0][0] + sum(f[1])) % mod
        t[1][1] = f[1][0]
        t[1][2] = f[1][1]
        f = t

    return (sum(f[0]) % mod + sum(f[1]) % mod) % mod

print check_record(2)

def test_check_record_1():
    assert 8 == check_record(2)