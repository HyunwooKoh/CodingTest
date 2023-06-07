import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstar(start):
    queue = []
    heapq.heappush(queue, (start,0))
    visited[start] = 0

    while queue:
        direct, fee = heapq.heappop(queue)
        if visited[direct] < fee:
            continue
        
        for d,f in graph[direct]:
            nf = fee + f
            if visited[d] > nf:
                heapq.heappush(queue,(d, nf))
                visited[d] = nf 

if __name__ == "__main__":
    v, e = map(int, input().split())
    start = int(input())
    graph  = [[] for _ in range(v+1)]
    visited = [INF] * (v+1)
    
    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    dijkstar(start)

    for i in range(1, v+1):
        if visited[i] == INF:
            print("INF")
        else:
            print(visited[i])