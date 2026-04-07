## https://school.programmers.co.kr/learn/courses/30/lessons/468379?language=python3

import sys
from collections import deque
input = sys.stdin.readline

def printMat(mat):
    for i in range(len(mat)):
        print(mat[i])

def solution2(m, n, h, w, drops):
    total = m * n
    INF = 999
    
    rain = [INF] * total

    # 2차원 배열을 1차원 배열로 변환
    for i in range(len(drops)):
        r, c = drops[i]
        rain[r * n + c] = i + 1
    print(rain)

    new_n = n - w + 1
    row_min = [0] * (m * new_n)

    # 가로 슬라이딩 윈도우 (row 기준)
    for r in range(m):
        dq = deque()

        for c in range(n):
            while dq and rain[r*n + dq[-1]] >= rain[r*n + c]:
                dq.pop()

            dq.append(c)

            if dq[0] <= c - w:
                dq.popleft()

            if c >= w - 1:
                row_min[r * new_n + (c - w + 1)] = rain[r*n + dq[0]]

    new_m = m - h + 1

    best_time = -1
    best_r = 0
    best_c = 0

    # 세로 슬라이딩 윈도우 (column 기준)
    for c in range(new_n):
        dq = deque()

        for r in range(m):
            val = row_min[r * new_n + c]

            while dq and row_min[dq[-1] * new_n + c] >= val:
                dq.pop()

            dq.append(r)

            if dq[0] <= r - h:
                dq.popleft()

            if r >= h - 1:
                cur = row_min[dq[0] * new_n + c]
                sr = r - h + 1

                if (cur > best_time or
                   (cur == best_time and (sr < best_r or (sr == best_r and c < best_c)))):
                    
                    best_time = cur
                    best_r = sr
                    best_c = c

    return [best_r, best_c]

def solution(m,n,h,w,drops):
    mat = [[0]*n for _ in range(m)]

    #printMat(mat)

    time = 0
    for drop in drops:
        time +=1 
        mat[drop[0]][drop[1]] = time

    #print()
    #printMat(mat)
    
    maxX = -1
    maxY = -1
    maxVal = 0
    
    #제일 빨리 맞는 시점이, 가장 큰 박스 area
    for y in range(m-h+1):
        for x in range(n-w+1):
            minVal = 0
            for i in range(y,y+h):
                for j in range(x,x+w):
                    #print(mat[i][j])
                    if (minVal == 0 and 0 < mat[i][j] ) or (mat[i][j] != 0 and mat[i][j] < minVal):
                        minVal = mat[i][j]
                        
            if minVal == 0:
                return [y,x]
            
            if minVal > maxVal:
                maxX = x
                maxY = y
                maxVal = minVal
    
    return [maxY, maxX]

if __name__ == "__main__": 
    #print(solution(4,5,2,2,[[0, 0], [3, 1], [1, 3], [2, 4], [1, 1], [2, 2], [2, 3], [0, 4]]))
    #print(solution(3,3,1,1,[[0, 0], [0, 1], [0, 2], [1, 0]]))
    #print(solution(4,6,3,4,[[1, 2]]))
    #print(solution(4,6,1,2,[[0, 1], [0, 3], [0, 5], [1, 1], [1, 3], [1, 5], [2, 1], [2, 3], [2, 5], [3, 1], [3, 3], [3, 5]]))
    #print(solution(2,2,2,2,[[0, 0], [0, 1], [1, 1], [1, 0]]))
    print(solution2(4,4,3,1,[[2, 0], [1, 3], [3, 2], [0, 1]]))