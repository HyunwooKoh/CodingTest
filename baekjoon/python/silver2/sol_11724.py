import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for _ in range(m):
        start, end = map(int, input().split())
        graph[start-1].append(end-1)
        graph[end-1].append(start-1)
    
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)
