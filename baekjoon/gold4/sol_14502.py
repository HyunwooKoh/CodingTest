import sys
import itertools
import copy
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def spread(i,j):
    queue = deque()
    queue.append((i,j))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and temp[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                temp[ny][nx] = 2
                queue.append((ny,nx))


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    empty = []
    for i in range(n):
        line = list(map(int, input().split()))
        graph.append(line)
        for j in range(m):
            if line[j] == 0:
                empty.append((i,j))
    
    res = 0
    for it in itertools.combinations(empty,3):
        temp = copy.deepcopy(graph)
        for x in list(it):
            temp[x[0]][x[1]] = 1
        
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2 and not visited[i][j]:
                    visited[i][j] = True
                    spread(i,j)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    count += 1
        res = max(res, count)
    print(res)