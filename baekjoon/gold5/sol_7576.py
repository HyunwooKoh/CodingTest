import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def dfs(depth):
    change = False
    hasZero = False
    changed = [[0]*x for _ in range(y)]

    for i in range(y):
        for j in range(x):
            if mat[i][j] == 0:
                hasZero = True
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < x and 0 <= ny < y and mat[ny][nx] == 1 and changed[ny][nx] == 0:
                        mat[i][j] = 1
                        changed[i][j] = 1
                        change = True
                        break

    if change:
        dfs(depth + 1)
    elif hasZero:
        print(-1)
    else:
        print(depth)


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < width and 0 <= ny < hight and mat[ny][nx] == 0:
                mat[ny][nx] = mat[y][x] + 1
                queue.append((nx, ny))

if __name__ == "__main__":
    width, hight = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(hight)]
    queue = deque()
    
    for y in range(hight):
        for x in range(width):
            if mat[y][x] == 1:
                queue.append((x,y))
    
    bfs()
    res = 0
    for line in mat:
        for i in line:
            if i == 0:
                print(-1)
                exit(0)
        res = max(res, max(line))
    print(res - 1)