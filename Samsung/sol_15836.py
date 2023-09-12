import sys
from copy import deepcopy

sys.setrecursionlimit(1e9)
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]
mode = [
    [],
    [[0],[1],[2],[3]], # CCTV 1번
    [[0,2], [1,3]], # CCTV 2번
    [[0,1], [1,2], [2,3], [0,3]], # CCTV 3번
    [[0,1,2], [0,1,3], [1,2,3], [0,2,3]], # CCTV 4번
    [[0,1,2,3]] # CCTV 5번
]
minRes = 1e9

def printMat(tempMat):
    for i in range(n):
        print(tempMat[i])
    print()

def checkRange(tempMat, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                break
            elif tempMat[ny][nx] == 6:
                break
            elif tempMat[ny][nx] == 0:
                tempMat[ny][nx] = -1


def dfs(depth, mat):
    if depth == len(cctv):
        #printMat(mat)
        global minRes
        res = 0
        for i in range(n):
            res += mat[i].count(0)
        minRes = min(minRes, res)
    else:
        tempMat = deepcopy(mat)
        target, x, y  = cctv[depth]
        for i in mode[target]:
            checkRange(tempMat, i , x, y)
            dfs(depth+1, tempMat)
            tempMat = deepcopy(mat)


if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = []
    cctv = []
    for i in range(n):
        line = list(map(int, input().split()))
        mat.append(line)
        for j in range(m):
            if 1 <= line[j] <= 5:
                cctv.append((line[j], j, i))
    
    dfs(0, mat)    
    print(minRes)