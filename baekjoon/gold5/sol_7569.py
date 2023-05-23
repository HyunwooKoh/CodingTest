import sys
from collections import deque
input = sys.stdin.readline

def bfs(queue : deque):
    dx = [0,0,0,0,1,-1]
    dy = [0,0,1,-1,0,0]
    dz = [1,-1,0,0,0,0]

    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and mat[nz][ny][nx] == 0:
                mat[nz][ny][nx] = mat[z][y][x] + 1
                queue.append((nx,ny,nz))


if __name__ == "__main__":
    m,n,h = map(int, input().split())

    mat = [ [list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if mat[i][j][k] == 1:
                   queue.append((k,j,i)) 
    
    bfs(queue)
    maxDay = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if mat[i][j][k] == 0:
                    print(-1)
                    exit(0)
            maxDay = max(maxDay, max(mat[i][j]))
    print(maxDay - 1)