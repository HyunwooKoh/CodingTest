# ref https://www.codetree.ai/training-field/frequent-problems/problems/odd-chess
import sys
from copy import deepcopy
input = sys.stdin.readline

# 남 북 동 서
dx = [0,0,1,-1]
dy = [1,-1,0,0]
horsesType = [[], # 빈 말
    [[0],[1],[2],[3]], # 1번말
    [[0,1],[2,3]], # 2번말
    [[1,2],[0,2],[0,3],[1,3]], # 3번말
    [[1,2,3],[0,1,2],[0,2,3],[0,1,3]]] # 4번말

def paddingDir(x,y,dir,tmpMat):
    while True:
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= m or y < 0 or y >= n:
            break
        elif tmpMat[y][x] == 6:
            break
        elif tmpMat[y][x] == 0:
            tmpMat[y][x] = -1

def dfs(idx, tmpMat):
    if idx == len(horses):
        global res
        tmpRes = 0
        for i in range(n):
            tmpRes += tmpMat[i].count(0)
        res = min(res, tmpRes)
    else:
        x, y, type = horses[idx][0], horses[idx][1], horses[idx][2]
        for ways in horsesType[type]:
            newMat = deepcopy(tmpMat)
            for way in ways:
                paddingDir(x,y,way,newMat)
            dfs(idx+1, newMat)

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = []
    horses = []
    defaultHorse = []
    for i in range(n):
        line = list(map(int ,input().split()))
        for j in range(m):
            if line[j] in (1,2,3,4):
                horses.append([j,i, line[j]])
            elif line[j] == 5:
                defaultHorse.append([j,i,5])
        mat.append(line)
    
    for horse in defaultHorse:
        x, y, type = horse[0], horse[1], horse[2]
        for i in range(4):
            paddingDir(x,y,i, mat)
    
    res = n*m
    dfs(0,mat)
    print(res)