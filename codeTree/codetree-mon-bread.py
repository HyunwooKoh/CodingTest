# ref https://www.codetree.ai/training-field/frequent-problems/problems/codetree-mon-bread
import sys
input = sys.stdin.readline

# 상,좌,우,하 순으로 우선순위
dx = [0,-1,1,0]
dy = [-1,0,0,1]

if __name__ == "__main__":
    n, M = map(int, input().split())
    mat = []
    baseCamp = []

    available_baseCamp = [] # 시작할 수 있는 베이스 캠프 (x,y)
    unavailable = [] # 지나갈 수 없는 칸 (x,y)

    people = [] # m번째 사람이 가고 싶은 편의점 위치 (x,y)
    movingPeople = []  # 격자 안에 있는 사람의 정보 (x,y,m)
    arrivedPeople = 0 # 목적지에 도착한 사람 cnt

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j] == 1:
                baseCamp.append((j,i))
                available_baseCamp.append((j,i))
        mat.append(line)

    for i in range(M):
        y, x = map(int, input().split())
        people.append((x-1,y-1))

    time = 0
    while M != arrivedPeople: # 모든 사람이 도착할 때 까지
        # 사람 이동
        arrived = [] # 이번 시간에 도착한 사람
        remainPeople = [] # 아직 도착 못한 사람
        for x,y,m in movingPeople:
            queue = [] # (x좌표, y좌표, history)
            queue.append((x,y,0,[]))
            visited = [[n*n]*n for _ in range(n)]
            visited[y][x] = 0
            minDist = n*n
            priorHis = []

            while queue:
                px, py, dist, history = queue.pop(0)

                if minDist <= dist:
                    continue

                for i in range(4):
                    nx = px + dx[i]
                    ny = py + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    if (nx, ny) in unavailable:
                        continue

                    # 같은 최소 값에 대한 이동 히스토리 비교가 필요하므로, 같은 값일 때에도 진행
                    if visited[ny][nx] < visited[py][px] + 1:
                        continue

                    newHistory = history.copy() + [i]
                    # 해당 사람의 목표 지점에 도달한 경우
                    if nx == people[m][0] and ny == people[m][1]:
                        if  visited[py][px] + 1 < visited[ny][nx]:
                            # 최소 거리가 갱신된 경우
                            minDist = dist+1
                            priorHis = newHistory
                        else:
                            # 최소 거리가 같은 경우 대소비교로 우선순위 셜정
                            priorHis = min(priorHis, newHistory)
                    else:
                        queue.append((nx,ny,dist+1, newHistory))

                    visited[ny][nx] = visited[py][px] + 1

            dir = priorHis[0]
            nx, ny = x + dx[dir], y + dy[dir]
            if nx == people[m][0] and ny == people[m][1]:
                # 움진인 결과가 목표 지점인 경우
                arrived.append(m)
                arrivedPeople += 1
            else:
                remainPeople.append((nx,ny,m))
        movingPeople = remainPeople

        # 사람이 도착한 편의점으로 못 움직이게 반영
        for m in arrived:
            unavailable.append(people[m])
        
        # m == time 인 사람이 격자에 신규 유입 됨
        if time <= M-1:
            x, y = people[time]
            nearestBaseCamp = ()
            minDist = n*n

            queue = []
            queue.append((x,y,0))
            visited = [[n*n]*n for _ in range(n)]
            visited[y][x] = 0

            while queue:
                px, py, dist = queue.pop(0)

                if minDist <= dist:
                    continue

                for i in range(4):
                    nx = px + dx[i]
                    ny = py + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    if (nx, ny) in unavailable:
                        continue

                    # 같은 값에 대한 비교가 필요 없으므로 스킵
                    if visited[ny][nx] <= visited[py][px] + 1:
                        continue
                    visited[ny][nx] = visited[py][px] + 1

                    if (nx,ny) in available_baseCamp:
                        if dist+1 < minDist:
                            minDist = dist+1
                            nearestBaseCamp = (nx,ny)
                        elif dist+1 == minDist:
                            if ny < nearestBaseCamp[1]:
                                nearestBaseCamp = (nx,ny)
                            elif ny == nearestBaseCamp[1]:
                                if nx < nearestBaseCamp[0]:
                                    nearestBaseCamp = (nx, ny)
                    else:
                        queue.append((nx,ny,dist+1))

            available_baseCamp.remove(nearestBaseCamp)
            unavailable.append(nearestBaseCamp)
            movingPeople.append((nearestBaseCamp[0],nearestBaseCamp[1],time))

        time += 1

    print(time)