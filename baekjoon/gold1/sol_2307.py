import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(n, ban_p1, ban_p2):
    heap = []
    cost = [INF] * (n+1)
    heapq.heappush(heap, (1,0))
    cost[0] = 0
    while heap:
        p, c = heapq.heappop(heap)
        if p == n:
            break
        for n_p, wei in graph[p]:
            if (p == ban_p1 and n_p == ban_p2) or (p == ban_p2 and n_p == ban_p1):
                continue
            n_wei = c + wei
            if n_wei < cost[n_p]:
                cost[n_p] = n_wei
                heapq.heappush(heap, (n_p, n_wei))
                if not ban_p1:
                    preP[n_p] = p
    #print("cost[n] : " + str(cost[n]))
    return cost[n] if cost[n] != INF else -1

if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    preP = {i : 0 for i in range(1, n+1)}
    for _ in range(m):
        a,b,t = map(int, input().split())
        graph[a].append((b,t))
        graph[b].append((a,t))
        
    minRes = dijkstra(n,0,0)
    
    delay = 0
    point = n
    while point != 1:
        res = dijkstra(n, point, preP[point])
        if res == -1:
            delay = -1
            break
        else:
            delay = max(delay, res - minRes)
        point = preP[point]
    print(delay)        