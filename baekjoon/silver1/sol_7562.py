import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,2,-2,1,-1]
    queue = deque()
    queue.append((x,y))
    while queue:
        px, py = queue.popleft()
        if px == tx and py == ty:
            print(mat[px][py])
            break

        for i in range(8):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx < 0 or nx >= size or ny < 0 or ny >= size or mat[nx][ny] != 0:
                continue
            
            mat[nx][ny] = mat[px][py] + 1
            queue.append((nx,ny))

if __name__ == "__main__":
    for _ in range(int(input())):
        size = int(input())
        x, y = map(int, input().split())
        tx, ty = map(int, input().split())
        mat = [[0] * size for _ in range(size)]
        bfs()