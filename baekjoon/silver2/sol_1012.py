import sys
input = sys.stdin.readline
from collections import deque

## dfs를 쓰면 MaxRecursion을 넘어가 RecursionError 발생
def dfs(vx, vy):
    if kmap[vy][vx] == 1:
        kmap[vy][vx] = 0
        if vx > 0:
            if kmap[vy][vx - 1] == 1:
                dfs(vx - 1, vy)
        if vx < len(kmap[0]) - 1:
            if kmap[vy][vx + 1] == 1:
                dfs(vx + 1, vy)
        if vy > 0:
            if kmap[vy -1][vx] == 1:
                dfs(vx, vy - 1)
        if vy < len(kmap) - 1:
            if kmap[vy + 1][vx] == 1:
                dfs(vx, vy + 1)


def bfs(vx, vy):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append((vx, vy))
    kmap[vy][vx] = 0
    while len(queue) >= 1:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if kmap[ny][nx] == 1:
                kmap[ny][nx] = 0
                queue.append((nx, ny))


if __name__ == "__main__":
    for _ in range(int(input())):
        m, n, kcount = map(int, input().split())
        kmap = [[0]*m for _ in range(n)]
        
        for _ in range (kcount):
            x,y = map(int, input().split())
            kmap[y][x] = 1

        count = 0
        for i in range(len(kmap)):
            for j in range(len(kmap[i])):
                if kmap[i][j] == 1:
                    bfs(j, i)
                    count += 1
        print(count)