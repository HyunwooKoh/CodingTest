import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

if __name__ == "__main__":
    n = int(input())
    mat = []
    x,y = -1,-1
    for i in range(n):
        line = list(map(int, input().split()))
        if x == -1:
            for j in range(n):
                if line[j] == 9:
                    x = j
                    y = i
        mat.append(line)
    res = 0
    state = 2
    count = 0
    mat[y][x] = 0

    while True:
        queue = deque([])
        fishes = [] # [x,y,dist]
        visited = [[0] * n for _ in range(n)]
        queue.append((x,y))
        while queue:
            px, py = queue.popleft()
            for i in range(4):
                nx = px + dx[i]
                ny = py + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[ny][nx] != 0:
                    continue
                
                if mat[ny][nx] <= state:
                    queue.append((nx,ny)) # 지나갈 수 있는 길
                    visited[ny][nx] = visited[py][px] + 1
                    if mat[ny][nx] != 0 and mat[ny][nx] < state:
                        fishes.append([nx,ny,visited[py][px]+1]) # 물고기
        if len(fishes) == 0:
            break
        else:
            # 먹을 물고기 정렬 및 추출
            fishes.sort(key = lambda l : (l[2],l[1],l[0]))
            fish = fishes[0]

            # 시간, (X,Y) 좌표 업데이트
            res += fish[2]
            x = fish[0]
            y = fish[1]
            
            # 먹은 물고기 제거
            mat[y][x] = 0
            
            # 먹은 물고기수 업데이트 및 크기 산정
            count += 1
            if count == state:
                state += 1
                count = 0
    print(res)