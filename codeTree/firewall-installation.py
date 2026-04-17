# ref https://www.codetree.ai/training-field/frequent-problems/problems/firewall-installation
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,cnt):
    if cnt == 3:
        # 이후의 검사를 위한 copy
        fMat = deepcopy(mat)
        cpFire = deepcopy(fire)
        while cpFire:
            fx, fy = cpFire.popleft()
            for i in range(4):
                nfx = fx + dx[i]
                nfy = fy + dy[i]
                if nfx < 0 or nfx >= m or nfy < 0 or nfy >= n:
                    continue
                if fMat[nfy][nfx] == 0:
                    fMat[nfy][nfx] = 2
                    cpFire.append((nfx, nfy))
        
        global maxRes
        res = 0
        for i in range(n):
            res += fMat[i].count(0)
        maxRes = max(maxRes, res)
    else:
        for i in range(y, n):
            for j in range(m):
                # 이미 방화벽을 새웠던 부분 검사 스킵
                if i == y and j < x:
                    continue
                if mat[i][j] == 0:
                    mat[i][j] = 1
                    dfs(j,i,cnt+1)
                    mat[i][j] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    fire = deque([])
    mat = []
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j] == 2:
                fire.append((j,i))
        mat.append(line)
    maxRes = 0
    dfs(0,0,0)
    print(maxRes)