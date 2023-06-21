import sys
from collections import deque

input = sys.stdin.readline

# 오른쪽, 아래, 왼쪽, 위
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    direct = 0
    cnt = 0
    n = int(input())
    mat = [[0]*n for _ in range(n)] # 0 -> 빈칸, 1 -> 사과, 2-> 뱀
    for _ in range(int(input())):
        ay, ax = map(int, input().split())
        mat[ay-1][ax-1] = 1
    change = {}
    for _ in range(int(input())):
        x, c = input().split()
        change[int(x)] = c

    x, y = 0, 0
    mat[y][x] = 2
    queue = deque([(x,y)])
    while(True):
        cnt += 1
        x += dx[direct]
        y += dy[direct]

        if x < 0 or x >= n or y < 0 or y >= n or (x,y) in queue:
            break
        
        if mat[y][x] == 1:
            mat[y][x] = 2
            queue.append((x,y))
        elif mat[y][x] == 0:
            mat[y][x] = 1
            queue.append((x,y))
            tx, ty = queue.popleft()
            mat[ty][tx] = 0
        else:
            break

        if cnt in change:
            if change[cnt] == 'L':
                direct = (direct - 1) % 4
            else:
                direct = (direct + 1) % 4

    print(cnt)
