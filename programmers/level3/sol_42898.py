def solution(m, n, puddles):
    mat = [[0] * (m+1) for _ in range(n+1)]
    mat[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j,i] in puddles:
                mat[i][j] = 0
            else:
                mat[i][j] = (mat[i-1][j] + mat[i][j-1]) % 1000000007
    return mat[n][m]