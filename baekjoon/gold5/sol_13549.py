import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    hide = [-1] * 100001
    queue = deque([n])

    hide[n] = 0
    while queue:
        p = queue.popleft()

        if p == k:
            print(hide[p])
            break

        if 0 <= p*2 <= 100000 and hide[p*2] == -1:
            queue.appendleft(p*2)
            hide[p*2] = hide[p]
        
        if 0 <= p+1 <= 100000 and hide[p+1] == -1:
            queue.append(p+1)
            hide[p+1] = hide[p] + 1
        
        if 0<= p-1 <= 100000 and hide[p-1] == -1:
            queue.append(p-1)
            hide[p-1] = hide[p] + 1