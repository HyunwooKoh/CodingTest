import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    degree = [0]*(n+1)
    queue = deque([])

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1
        
    for s in range(1, n+1):
        if degree[s] == 0:
            queue.append(s)

    ans = []
    while queue:
        s = queue.popleft()
        ans.append(s)

        for i in graph[s]:
            degree[i] -= 1
            if degree[i] == 0:
                queue.append(i)

    print(*ans, sep=" ")