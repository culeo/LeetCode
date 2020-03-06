# coding: utf-8

def encode(s):

    N = len(s)
    f = [[0] * N for i in range(N)]
    
    for l in range(N):
        for i in range(N - l):
            j = i + l
            f[i][j] = s[i:j+1]
            for k in range(i, j):
                left, right = f[i][k], f[k+1][j]
                if len(left) + len(right) < len(f[i][j]):
                    f[i][j] = left + right
            
            tmp = s[i: j+1]
            idx = (tmp + tmp).find(tmp, 1)

            if idx > 0 and idx < len(tmp):
                tmp = str(int(len(tmp) / idx)) + '[' + f[i][i+idx-1] + ']'
            
            if len(tmp) < len(f[i][j]):
                f[i][j] = tmp

    return f[0][N-1]

print encode('abbbabbbcabbbabbbc')

def test_encode_1():
    assert '2[2[abbb]c]' == encode('abbbabbbcabbbabbbc')

def test_encode_2():
    assert 'aaa' == encode('aaa')

def test_encode_3():
    assert '2[aabc]d' == encode('aabcaabcd')
