# ref https://www.codetree.ai/training-field/frequent-problems/problems/debugging
import sys
input = sys.stdin.readline

def check():
    for i in range(n):
        p = i
        for j in range(h):
            if mat[j][p] != -1:
                p = mat[j][p]
        if p != i:
            return False
    return True

def dfs(cnt, x, y):
    if cnt == 3:
        return
    else:
        for i in range(y,h):
            for j in range(0 if i != y else x, n-1):
                if mat[i][j] == -1 and mat[i][j+1] == -1:
                    mat[i][j] = j+1
                    mat[i][j+1] = j
                    if check():
                        global res
                        res = min(res, cnt+1)
                    else:
                        dfs(cnt+1, j, i)
                    mat[i][j] = -1
                    mat[i][j+1] = -1


if __name__ == "__main__":
    n, m, h = map(int, input().split())
    mat = [[-1]*n for _ in range(h)]
    res = 1e9
    for _ in range(m):
        a, b = map(int, input().split())
        mat[a-1][b-1] = b
        mat[a-1][b] = b-1
    if m == 0 or check():
        res = 0
    else:
        dfs(0,0,0)
    print(res if res != 1e9 else -1)