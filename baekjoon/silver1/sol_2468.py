import sys
import copy
from collections import deque

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y, high, gp):
    queue = deque([])
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or gp[nx][ny] <= high:
                continue
            
            queue.append((nx, ny))
            gp[nx][ny] = 0


if __name__ == "__main__":
    n = int(input())
    maxArea = 0
    maxHigh = 0
    graph = []
    for _ in range(n):
        line = list(map(int, input().split()))
        graph.append(line)
        maxHigh = max(maxHigh, max(line))


    for i in range(maxHigh):
        count = 0
        gp = copy.deepcopy(graph)
        for x in range(n):
            for y in range(n):
                if gp[x][y] > i:
                    gp[x][y] = 0
                    count += 1
                    bfs(x, y, i, gp)
        maxArea = max(count, maxArea)
    print(maxArea)