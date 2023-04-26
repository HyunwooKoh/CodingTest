import sys
import math
input = sys.stdin.readline


def dfs(depth, idx):
    global res
    global n
    if depth == n // 2:
        start = link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += s[i][j]
                elif not visited[i] and not visited[j]:
                    link += s[i][j]
        res = min(res, abs(start - link))
    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(depth + 1, i + 1)
                visited[i] = False

if __name__ == "__main__":
    global res
    global n
    
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n

    res = math.inf
    dfs(0,0)
    print(res)