import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y, n, m, count, chance):
    if x == m-1 and y == n-1:
        global res
        res = min(res, count)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if mat[ny][nx] == 0:
                    visited[ny][nx] = True
                    dfs(nx, ny, n, m, count+1, chance)
                    visited[ny][nx] = False
                
                if chance:
                    mat[ny][nx] = 0
                    visited[ny][nx] = True
                    dfs(nx, ny, n, m, count+1, False)
                    mat[ny][nx] = 1
                    visited[ny][nx] = False


def bfs(x,y,chance):
    queue = deque([])
    queue.append((x,y,chance))
    
    while queue:
        px, py, pChance = queue.popleft()
        if px == m-1 and py == n-1:
            return visited[py][px][pChance]

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if mat[ny][nx] == 1 and pChance == 0:
                    visited[ny][nx][1] = visited[py][px][0] + 1
                    queue.append((nx,ny,1))
                elif mat[ny][nx] == 0 and visited[ny][nx][pChance] == 0:
                    visited[ny][nx][pChance] = visited[py][px][pChance] + 1
                    queue.append((nx,ny,pChance))
    return -1

if __name__ == "__main__":
    global res
    res = int(1e9)
    
    n,m = map(int, input().split())
    mat = []
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    for _ in range(n):
        mat.append(list(map(int, input().strip())))
    
    visited[0][0][0] = 1
    print(bfs(0,0,0))