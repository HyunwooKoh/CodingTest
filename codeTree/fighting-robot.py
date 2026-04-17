# ref https://www.codetree.ai/training-field/frequent-problems/problems/fighting-robot
import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(rx, ry, level):
    visited = [[False]*n for _ in range(n)]
    monsters = []
    queue = deque([(rx,ry,0)])
    visited[ry][rx] = True
    while queue:
        px, py, pDist = queue.popleft()
        if 1 <= mat[py][px] <= 6 and mat[py][px] < level: # 현재 칸이 몬스터인 경우
            monsters.append([px,py,pDist])
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[ny][nx] or level < mat[ny][nx]:
                continue
            queue.append((nx,ny,pDist+1))
            visited[ny][nx] = True

    # 죽일 수 있는 몬스터에 대해 
    monsters.sort(key = lambda x : (x[2], x[1], x[0]))

    # 몬스터의 x좌표, y좌표, 거리 리턴
    if len(monsters) > 0:
        return monsters[0][0], monsters[0][1], monsters[0][2]
    else:
        return -1, -1, -1

if __name__ == "__main__":
    n = int(input())
    mat = []
    rx, ry, rLevel = -1, -1, 2
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j] == 9:
                rx = j
                ry = i
        mat.append(line)
    
    res = 0
    killCnt = 0
    while True:
        nx, ny, dist = bfs(rx, ry, rLevel)
        if dist != -1:
            mat[ry][rx] = 0
            mat[ny][nx] = 9
            rx, ry = nx, ny
            
            killCnt += 1
            if rLevel == killCnt: # 레벨 업
                rLevel += 1
                killCnt = 0
            res += dist # 이동 시간 갱신
        else:
            break # 죽일 것이 없으면 종료
    print(res)