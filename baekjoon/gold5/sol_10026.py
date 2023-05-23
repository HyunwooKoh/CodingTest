import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y, color):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        px, py = queue.popleft()
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=n or visited[nx][ny] == 1:
                continue
            if mat[nx][ny] == color:
                visited[nx][ny] = 1
                queue.append((nx,ny))


def bfs_weakness(x, y, color):
    queue = deque()
    queue.append((x,y))
    
    if color == 'R' or color == 'G':
        color = 'RG'

    while queue:
        px, py = queue.popleft()
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=n or visited_weakness[nx][ny] == 1:
                continue
            if mat[nx][ny] in color:
                visited_weakness[nx][ny] = 1
                queue.append((nx,ny))


if __name__ == "__main__":
    n = int(input())
    mat = [list(map(str, input().strip())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    visited_weakness = [[0]* n for _ in range(n)]
    
    count = 0
    weakness_count = 0    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] == 1
                bfs(i, j, mat[i][j])
                count += 1
            if visited_weakness[i][j] == 0:
                visited_weakness[i][j] == 1
                bfs_weakness(i, j, mat[i][j])
                weakness_count += 1
    print(count)
    print(weakness_count)