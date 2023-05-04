import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    queue = deque()
    queue.append(start)

    while queue:
        p = queue.popleft()
        if p == end:
            break
        else :
            for np in (p - 1, p + 1, p * 2):
                if 0 <= np <= MAX and t[np] == 0:
                    t[np] = t[p] + 1
                    queue.append(np)
    return t[p]

if __name__ == "__main__" :
    start, end = map(int, input().split())
    MAX = 10 ** 5
    t = [0] * (MAX+1)
    print(bfs(start, end))