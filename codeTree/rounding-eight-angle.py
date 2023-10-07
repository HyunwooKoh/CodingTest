# ref https://www.codetree.ai/training-field/frequent-problems/problems/rounding-eight-angle
import sys
input = sys.stdin.readline

def turn(table, dir):
    if dir == 1: # 시계방향
        tmp = table[7]
        table = [tmp] + table[0:7]
    else: # 반시계 방향
        tmp = table[0]
        table = table[1:8] + [tmp]
    return table

if __name__ == "__main__":
    tables = [[]]
    for _ in range(4):
        tables.append(list(map(int, input().strip())))
    k = int(input())
    moves = [map(int, input().split()) for _ in range(k)]
    
    # 오른쪽 끝(idx) : 2, 왼쪽 끝(idx) : 6
    left, right = 6, 2

    for target, dir in moves:
        tmpDir = dir
        lastLeft = tables[target][6]
        lastRight = tables[target][2]

        # target 식탁 회전
        tables[target] = turn(tables[target], tmpDir)

        # 돌리는 식탁의 왼쪽 식탁들
        for i in range(target-1, 0, -1):
            if tables[i][right] != lastLeft:
                lastLeft = tables[i][left]
                tmpDir *= -1
                tables[i] = turn(tables[i], tmpDir)
            else:
                break
        
        # 돌리는 식탁의 오른쪽 식탁들
        tmpDir = dir
        for i in range(target+1, 5):
            if tables[i][left] != lastRight:
                lastRight = tables[i][right]
                tmpDir *= -1
                tables[i] = turn(tables[i], tmpDir)
            else:
                break
        
    res = 0
    for i in range(1,5):
        tables[i][0]
        if tables[i][0] == 1:
            res += (2**(i-1))
    print(res)