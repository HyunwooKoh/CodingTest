import sys
input = sys.stdin.readline

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)


if __name__ == "__main__":
    comNum = int(input())
    linkNum = int(input())
    graph = [[] for _ in range(comNum + 1)]
    visited=[0]*(comNum + 1)
    for i in range(linkNum):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)
    print(sum(visited)-1)