# ref https://www.codetree.ai/training-field/frequent-problems/problems/heros-of-storm
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def getPulledPos(x,y):
    nx, ny = x, y
    if 0 <= y <= windTop:
        if y == windTop and x != m-1: # 오른쪽으로 밀리는 라인 (끝 칸 제외)
            nx += 1
        elif x == m-1 and y != 0: # 위쪽으로 밀리는 라인
            ny -= 1
        elif y == 0 and 0 < x: # 왼쪽으로 밀리는 라인
            nx -= 1
        elif x == 0: # 아래쪽으로 밀리는 라인
            ny += 1
    else:
        if y == windBottom and x != m-1: # 오른쪽으로 밀리는 라인 (끝 칸 제외)
            nx += 1
        elif x == m-1 and y != n-1: # 아래쪽으로 밀리는 라인
            ny += 1
        elif y == n-1 and 0 < x: # 왼쪽으로 밀리는 라인
            nx -= 1
        elif x == 0: # 위쪽으로 밀리는 라인
            ny -= 1
    #print("x : " + str(x) + ", y : " + str(y) + ", nx : " + str(nx) + ", ny : " + str(ny))
    return nx, ny


if __name__ == "__main__":
    n, m, t  = map(int, input().split())
    windTop, windBottom = -1, -1
    mat = []
    for i in range(n):
        line = list(map(int, input().split()))
        if windTop == -1 and line[0] == -1:
            windTop = i
            windBottom = i+1
        mat.append(line)
    
    for _ in range(t):
        # 나눠주고 남은 양 + 나눔 받은 양의 갱신을 위한 새로운 mattrix
        newMat = [[0]*m for _ in range(n)]
        
        # 먼지 확산 및 바람 미는 로직
        for y in range(n):
            for x in range(m):
                
                # 해당 칸이 돌풍인 경우 Skip
                if x == 0 and y in (windTop, windBottom):
                    continue

                spreadCnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or mat[ny][nx] == -1:
                        continue
                    
                    pullednx, pulledny = getPulledPos(nx, ny)
                    
                    spreadCnt += 1
                    newMat[pulledny][pullednx] += mat[y][x] // 5 # 갱신용 mat에 확산을 ADD
                
                if spreadCnt != 0:
                    pulledx, pulledy = getPulledPos(x, y)
                    # 갱신용 mat에 확산하고 남은 것을 ADD
                    newMat[pulledy][pulledx] += mat[y][x] - (mat[y][x] // 5) * spreadCnt
        
        # 돌풍 위치에 들어간 값 지우기 및 바로 옆에 깨끗한 칸 삽입
        newMat[windTop][0] = -1
        newMat[windBottom][0] = -1
        newMat[windTop][1] = 0
        newMat[windBottom][1] = 0
        mat = newMat
    
    res = 0
    for i in range(n):
        res += sum(mat[i])
    res += 2
    print(res)