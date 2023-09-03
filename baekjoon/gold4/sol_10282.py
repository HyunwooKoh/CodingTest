import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(start, dep, mat):
    heap = []
    heapq.heappush(heap, (0, start))
    dep[start] = 0
    while heap:
        w, n = heapq.heappop(heap)
        for n_n, wei in mat[n]:
            n_w = wei + w
            if n_w < dep[n_n]:
                dep[n_n] = n_w
                heapq.heappush(heap, (n_w, n_n))

if __name__ == "__main__":
    for _ in range(int(input())):
        n, d, c = map(int, input().split())
        mat = [[] for _ in range(n+1)]
        dep = [INF] * (n+1)

        for _ in range(d):
            a, b, s = map(int, input().split())
            mat[b].append((a,s))
        
        dijkstra(c, dep, mat)
        
        cnt, res = 0, 0
        for dp in dep:
            if dp != INF:
                cnt += 1
                res = max(res, dp)
        
        print(f"{cnt} {res}")