import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, idx, total):
    global res
    if res >= total + max_val * (3 - idx):
        return
    if idx == 3:
        res = max(res, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + mat[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + mat[nr][nc])
                visit[nr][nc] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    visit = [([0] * m) for _ in range(n)]
    max_val = max(map(max, mat))

    global res
    res = 0
    for r in range(n):
        for c in range(m):
            visit[r][c] = 1
            dfs(r, c, 0, mat[r][c])
            visit[r][c] = 0
    print(res)