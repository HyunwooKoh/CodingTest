import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    distance = [int(1e9)] * n

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue
                    
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(queue, (cost, node_index))
    return distance


if __name__ == "__main__":
    n, m, x = map(int, input().split())
    x -= 1
    counts = [0] * n
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a-1].append((b-1,t))
    
    res = 0
    back = dijkstra(x)
    for i in range(n):
        if i == x:
            continue
        else:
            go = dijkstra(i)
            res = max(res, go[x] + back[i])
    print(res)