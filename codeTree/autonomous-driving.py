# ref https://www.codetree.ai/training-field/frequent-problems/problems/autonomous-driving
import sys
from collections import deque
input = sys.stdin.readline

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


if __name__ == "__main__":
    n, m = map(int, input().split())
    y, x, d = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    cnt = 1
    visited[y][x] = True
    while True:
        # 회전
        move = False
        for _ in range(4): # 마지막에 다시 보던 방향으로 돌리기 위해 +4까지
            d = (d-1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if x < 0 or x > m or y < 0 or y > n:
                continue
            if mat[ny][nx] == 0 and not visited[ny][nx]:
                x = nx
                y = ny
                visited[ny][nx] = True
                move = True
                cnt += 1
                break
        
        if not move:
            nx = x - dx[d]
            ny = y - dy[d]
            if x < 0 or x > m or y < 0 or y > n or mat[ny][nx] == 1:
                break # 지도 밖으로 벗어나거나, 뒤에가 인도
            else: # 후진
                x = nx
                y = ny
    print(cnt)