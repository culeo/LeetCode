# coding: utf-8

def max_uncrossed_lines(A, B):

    N = len(A)
    M = len(B)

    f = [[0] * (M + 1) for i in range(N + 1)]

    for i in range(1, N+ 1):
        for j in range(1, M + 1):
            if A[i-1] == B[j-1]:
                f[i][j] = f[i-1][j-1] + 1
            else:
                f[i][j] = max(f[i][j-1], f[i-1][j])

    return f[N][M]
 
print max_uncrossed_lines([2,5,1,2,5], [10,5,2,1,5,2])

def test_max_uncrossed_lines_1():
    assert 3 == max_uncrossed_lines([2,5,1,2,5], [10,5,2,1,5,2])

def test_max_uncrossed_lines_2():
    assert 2 == max_uncrossed_lines([1,3,7,1,7,5], [1,9,2,5,1])