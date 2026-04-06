## https://school.programmers.co.kr/learn/courses/30/lessons/468379?language=python3

import sys
from collections import deque
input = sys.stdin.readline

def printMat(mat):
    for i in range(len(mat)):
        print(mat[i])

def solution(m,n,h,w,drops):
    mat = [[0]*n for _ in range(m)]

    printMat(mat)

    time = 0
    for drop in drops:
        time +=1 
        mat[drop[0]][drop[1]] = time

    print()
    printMat(mat)
    
    maxX = -1
    maxY = -1
    maxVal = 0
    #제일 빨리 맞는 시점이, 가장 큰 박스 area
    for x in range(m-w+1):
        for y in range(n-h+1):
            print('x : ' + str(x), ', y : ' + str(y))
            minVal = 0
            for i in range(x,x+w):
                for j in range(y,y+h):
                    print(mat[i][j])
                    if (minVal == 0 and 0 < mat[i][j] ) or (mat[i][j] != 0 and mat[i][j] < minVal):
                        minVal = mat[i][j]
                        print('change! minval : ' + str(minVal))
                        
            print('minVal : ' + str(minVal))
            if minVal == 0:
                print(str(x) + ", " + str(y))
                return
            
            if minVal > maxVal:
                print('MAX Val change, maxVal : ' + str(minVal) + ', x : ' + str(x) + ', y : ' + str(y))
                maxX = x
                maxY = y
                maxVal = minVal
            print()
    
    print(str(maxX) + ", " + str(maxY))

if __name__ == "__main__": 
    #solution(4,5,2,2,[[0, 0], [3, 1], [1, 3], [2, 4], [1, 1], [2, 2], [2, 3], [0, 4]])
    #solution(3,3,1,1,[[0, 0], [0, 1], [0, 2], [1, 0]])
    solution(4,6,3,4,[[1, 2]])