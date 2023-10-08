# ref https://www.codetree.ai/training-field/frequent-problems/problems/odd-chess
import sys
input = sys.stdin.readline

# 남 북 동 서
dx = [0,0,1,-1]
dy = [1,-1,0,0]
horsesType = [[], # 빈 말
    [[0],[1],[2],[3]], # 1번말
    [[0,1],[2,3]], # 2번말
    [[1,2],[0,2],[0,3],[1,3]], # 3번말
    [[1,2,3],[0,1,2],[0,2,3],[0,1,3]], # 4번말
    [[0,1,2,3]]] # 5번말

def dfs(idx):
    if idx == len(horses):
        global res
        tmpRes = 0
        for i in range(n):
            tmpRes += mat[i].count(0)
        res = min(res, tmpRes)
    else:
        x, y, type = horses[idx][0], horses[idx][1], horses[idx][2]
        for ways in horsesType[type]:
            changed = []
            for way in ways:
                nx, ny = x, y
                while True:
                    nx += dx[way]
                    ny += dy[way]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        break
                    elif mat[ny][nx] == 6:
                        break
                    elif mat[ny][nx] == 0:
                        mat[ny][nx] = -1
                        changed.append((nx,ny))
            dfs(idx+1)
            # 초기화
            for cx,cy in changed:
                mat[cy][cx] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = []
    horses = []
    for i in range(n):
        line = list(map(int ,input().split()))
        for j in range(m):
            if line[j] in (1,2,3,4,5):
                horses.append([j,i,line[j]])
        mat.append(line)
    
    res = n*m
    dfs(0)
    print(res)