# ref https://www.codetree.ai/training-field/frequent-problems/problems/vaccine-for-virus
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = []
    hospitals = []
    viruses = []
    res = int(1e9)
    
    for i in range(n):
        line = list(map(int, input().split()))
        mat.append(line)

        for j in range(n):
            if line[j] == 0: #바이러스
                viruses.append((j,i))
            elif line[j] == 2: #병원
                hospitals.append((j,i))
    
    if viruses:
        for comb in combinations(hospitals, m):
            visited = [[n*n]*n for _ in range(n)]
            queue = deque([])
            
            for x, y in comb:
                visited[y][x] = 0
                queue.append((x,y,0))

            while queue:
                x, y, dist = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n or mat[ny][nx] == 1:
                        continue

                    # 한번 방문 했어도, 이후에 최소 거리가 있을 수 있음
                    if dist + 1 >= visited[ny][nx]:
                        continue
                    
                    visited[ny][nx] = dist+1
                    queue.append((nx, ny, dist+1))

            maxDist = 0
            for x, y in viruses:
                # 모든 바이러스를 죽이지 못한 경우
                if visited[y][x] == n*n:
                    maxDist = -1
                    break
                maxDist = max(maxDist, visited[y][x])

            if maxDist != -1:
                res = min(res, maxDist)

    else:
        res = 0
    
    print(res if res != int(1e9) else -1)