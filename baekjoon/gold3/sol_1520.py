import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if visited[y][x] != -1:
        return visited[y][x]
    
    visited[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
            
        if mat[ny][nx] < mat[y][x]:
            visited[y][x] += dfs(nx,ny)
    return visited[y][x]

if __name__ == "__main__":
    n,m = map(int, input().split())
    visited = [[-1]*m for _ in range(n)]
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))
    
    print(dfs(0,0))