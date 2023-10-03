# ref https://www.codetree.ai/training-field/frequent-problems/problems/2048-game

import sys
from copy import deepcopy
input = sys.stdin.readline

# 아래, 위, 오른쪽, 왼쪽
dx = [0,0,1,-1]
dy = [1,-1,0,0]
maxVal = 0

def move(dir, tempMat):
    if dir == 0:
        # 아래로 밀기
        # 아래방향의 끝(맨위)를 기준으로 Top-Down 탐색
        for i in range(n):
            j = n-1
            while j > 0:
                nextNum = -1
                for k in range(j-1, -1, -1):
                    if tempMat[i][k] != 0:
                        nextNum = k
                        break
                if nextNum != -1:
                    if tempMat[i][j] == 0:
                        tempMat[i][j] = tempMat[i][nextNum]
                        tempMat[i][nextNum] = 0
                    else:
                        if tempMat[i][j] == tempMat[i][nextNum]:
                            tempMat[i][j] *= 2
                            tempMat[i][nextNum] = 0
                        j -= 1
                else:
                    break
    elif dir == 1:
        # 위로 밀기
        for i in range(n):
            j = 0
            while j < n:
                nextNum = -1
                for k in range(j+1, n):
                    if tempMat[i][k] != 0:
                        nextNum = k
                        break
                if nextNum != -1:
                    if tempMat[i][j] == 0:
                        tempMat[i][j] = tempMat[i][nextNum]
                        tempMat[i][nextNum] = 0
                    else:
                        if tempMat[i][j] == tempMat[i][nextNum]:
                            tempMat[i][j] *= 2
                            tempMat[i][nextNum] = 0
                        j += 1
                else:
                    break
    elif dir == 2:
        # 오른쪽으로 밀기
        for i in range(n):
            j = n-1
            while j > 0:
                nextNum = -1
                for k in range(j-1, -1, -1):
                    if tempMat[k][i] != 0:
                        nextNum = k
                        break
                if nextNum != -1:
                    if tempMat[j][i] == 0:
                        tempMat[j][i] = tempMat[nextNum][i]
                        tempMat[nextNum][i] = 0
                    else:
                        if tempMat[j][i] == tempMat[nextNum][i]:
                            tempMat[j][i] *= 2
                            tempMat[nextNum][i] = 0
                        j -= 1
                else:
                    break
    elif dir == 3:
        # 왼쪽으로 밀기
        for i in range(n):
            j = 0
            while j < n:
                nextNum = -1
                for k in range(j+1, n):
                    if tempMat[k][i] != 0:
                        nextNum = k
                        break
                if nextNum != -1:
                    if tempMat[j][i] == 0:
                        tempMat[j][i] = tempMat[nextNum][i]
                        tempMat[nextNum][i] = 0
                    else:
                        if tempMat[j][i] == tempMat[nextNum][i]:
                            tempMat[j][i] *= 2
                            tempMat[nextNum][i] = 0
                        j += 1
                else:
                    break

def dfs(cnt, tempMat):
    if cnt == 5:
        global maxVal
        for i in range(n):
            maxVal = max(maxVal, max(tempMat[i]))
        return
    else:
        for i in range(4):
            nTempMat = deepcopy(tempMat)
            move(i, nTempMat)
            dfs(cnt+1, nTempMat)

if __name__ == "__main__":
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    dfs(0, mat)
    print(maxVal)