import sys
import heapq
input = sys.stdin.readline

def dijkstar(start):
    queue = []
    heapq.heappush(queue, (start,0))
    visited[start] = 0

    while queue:
        direct, fee = heapq.heappop(queue)
        if visited[direct] < fee:
            continue
        elif not direct in bus:
            continue
        
        for d, f in bus[direct]:
            nf = fee + f
            if visited[d] > nf:
                heapq.heappush(queue,(d, nf))
                visited[d] = nf 

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    visited = [int(1e9)] * (n+1)
    bus = {}
    for _ in range(m):
        start, end, fee = map(int, input().split())
        if start in bus:
            bus[start].append((end, fee))
        else:
            bus[start] = [(end,fee)]
    start, end = map(int,input().split())
    
    dijkstar(start)
    print(visited[end])