# ref https://www.codetree.ai/training-field/frequent-problems/problems/matrix-number-play
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    r, c, k = map(int, input().split())
    width, height = 3, 3
    time = 0

    mat = [[0]*100 for _ in range(100)]
    for i in range(3):
        line = list(map(int, input().split()))
        for j in range(3):
            mat[i][j] = line[j]
    
    while mat[r-1][c-1] != k and time <= 100:
        if  width <= height:   
            
            for i in range(height):
                rowDict = {}
                
                for j in range(width):    
                    if mat[i][j] == 0:
                        continue
                    if mat[i][j] in rowDict:
                        rowDict[mat[i][j]] += 1
                    else:
                        rowDict[mat[i][j]] = 1
                
                sortedDictList = sorted(rowDict.items(), key = lambda x : (x[1], x[0]))
                width = min(100, max(width, len(sortedDictList)*2))

                for j in range(0, width, +2):
                    if sortedDictList:
                        num, cnt = sortedDictList.pop(0)
                        mat[i][j] = num
                        mat[i][j+1] = cnt
                    else:
                        mat[i][j] = 0
                        mat[i][j+1] = 0    
        else:
            
            for i in range(width):
                colDict = {}
                
                for j in range(height):
                    if mat[j][i] == 0:
                        continue
                    if mat[j][i] in colDict:
                        colDict[mat[j][i]] += 1
                    else:
                        colDict[mat[j][i]] = 1
                
                sortedDictList = sorted(colDict.items(), key = lambda x : (x[1], x[0]))
                height = min(100, max(height, len(sortedDictList)*2))

                for j in range(0, height, +2):
                    if sortedDictList:
                        num, cnt = sortedDictList.pop(0)
                        mat[j][i] = num
                        mat[j+1][i] = cnt
                    else:
                        mat[j][i] = 0
                        mat[j+1][i] = 0
        time += 1
    print(time if time != 101 else -1)