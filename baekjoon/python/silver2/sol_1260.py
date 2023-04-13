import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)


def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while len(queue) >= 1:
        s = queue.popleft()
        print(s, end=" ")
        for nx in graph[s]:
            if visited[nx] == 0:
                visited[nx] = 1
                queue.append(nx)


if __name__ == "__main__":
    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited= [0] * (n + 1)
    
    for i in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for line in graph:
        line.sort()

    dfs(start)
    print()
    visited= [0] * (n + 1)
    bfs(start)