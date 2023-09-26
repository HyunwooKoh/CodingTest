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
            last = tempMat[0][i]
            for j in range(1, n):
                if last == 0:
                    last = tempMat[j][i]
        return
    elif dir == 1:
        # 위로 밀기
        return
    elif dir == 2:
        # 오른쪽으로 밀기
        return
    elif dir == 3:
        # 왼쪽으로 밀기
        return

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