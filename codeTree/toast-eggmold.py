# ref https://www.codetree.ai/training-field/frequent-problems/problems/toast-eggmold
import sys
from collections import deque
input = sys.stdin.readline

# 완전 탐색 -> boarder를 지움
# bfs -> 각 칸별 작업
# 오른쪽, 아래, 왼쪽, 위
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x, y, visited):
    total = mat[y][x]
    target = [(x,y)]
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[ny][nx]:
                continue

            if L <= abs(mat[y][x] - mat[ny][nx]) <= R:
                total += mat[ny][nx]
                visited[ny][nx] = True
                target.append((nx,ny))
                queue.append((nx,ny))
    
    newVal = total // len(target)
    for x,y in target:
        mat[y][x] = newVal

    return True if len(target) > 1 else False

if __name__ == "__main__":
    n, L, R = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    res = 0
    while True:
        change = False
        visited = [[False]*n for _ in range(n)]
            
        for y in range(n):
            for x in range(n):
                if not visited[y][x]:
                    visited[y][x] = True
                    change = bfs(x,y,visited) or change
        
        if change:
            res += 1
        else:
            break
    print(res)