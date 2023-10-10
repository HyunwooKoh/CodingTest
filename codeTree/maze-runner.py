# ref https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner
import sys
from collections import deque
input = sys.stdin.readline

# M명의 참가자
# N*N 격자
# K초 동안 수행 (모두 탈출 시 종료)
# y : r, x : c -> (r-1, c-1)

### 미로 종류
# 미로 칸 종류
# : 빈칸, : 벽 (이동 X, 1~9 값, 회전시 -= 1, 0되면 빈칸)
# 출구 도착시 종료

### 미로 회전
# 한명 이상의 참가자 및 출구를 포함한 가장 작은 정사각형 
# -> 1초마다 최단거리가 바뀜 (갱신?)
# -> 사람의 좌표를 리스트로 관리하고, 이 리스트 순회로 정사각형 특정
# 여러개 -> 좌상단의 y좌표가 작은 것이 우선, 이것이 같으면 x 좌표가 작은 것이 우선
# 시계방향 90도 회전 및 내구도가 1씩 깍임

### 출력
# 모든 참가자들의 이동 거리 합 및 출구 좌표

dx = [0,0,-1,1]
dy = [-1,1,0,0]

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    people = []
    for _ in range(m):
        y, x = map(int, input().split())
        people.append((x-1, y-1))
    exitX, exitY = map(int, input().split())
    time, move = 0, 0

    while time < k:
        
        # 이동
        i = 0
        while i < len(people):
            minDist = int(1e9) + 1
            px, py = people[i]
            dist = abs(px - exitX) + abs(py - exitY)
            minPos = []
            
            for d in range(4):
                nx = px + dx[d]
                ny = py + dy[d]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                
                nDist = abs(nx - exitX) + abs(ny - exitY)
                # 최단거리가 감소하는 곳으로만 이동
                if  dist <= nDist:
                    continue

                # 상/하가 우선되므로, 같은 값은 무시
                if nDist < minDist:
                    minDist = nDist
                    minPos = [nx,ny]
            
            if not minPos: # 움직일 수 없는 경우
                continue
            else:
                move += 1
                if minPos[0] == exitX and minPos[1] == exitY:
                    # 출구로 나가는 경우 해당 탐험가 제거
                    people.pop(i)
                else:
                    i += 1
                    people[i] = (nx, ny)
    
        # 정사각형 집기
        # 크기가 같을 경우를 대비해서, (1)y좌표 (2)x좌표로 정렬
        people.sort(key = lambda x : (x[1], x[0]))
        minLen = n
        squares = [] # tx, ty, bx, by
        for px, py in people:
            pLen = max(abs(px - exitX), abs(py - exitY))

            if pLen < minLen:
                squares = [min(px, exitX), min(py, exitY), min(px, exitX)+pLen, min(py, exitY)+pLen]
        
        # 정사각형 돌리기
        

        