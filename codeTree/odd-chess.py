# ref https://www.codetree.ai/training-field/frequent-problems/problems/odd-chess
import sys
input = sys.stdin.readline

# 남 북 동 서
dx = [0,0,1,-1]
dy = [1,-1,0,0]
horsesType = [[],[],[],[],[]]

def directCnt(x,y,dir):
    res = 0
    while True:
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= m or y < 0 or y >= n:
            break
        elif mat[y][x] == 6:
            break
        elif mat[y][x] == 0:
            res += 1
    return res

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = []
    horses = []
    for i in range(n):
        line = list(map(int ,input().split()))
        for j in range(m):
            if line[j] in (1,2,3,4,5):
                horses.append([j,i, line[j]])
        mat.append(line)
    
    horses.sort(key = lambda x : (-x[2]))

    for horse in horses:
        x, y, type = horse[0], horse[1], horse[2]
        if type == 1:
            break
        elif type == 2:
            north = directCnt(x,y,1)
            south = directCnt(x,y,0)
            west = directCnt(x,y,3)
            east = directCnt(x,y,2)


        elif type == 3:
            break
        elif type == 4:
            break
        elif type == 5:
            for i in range(4):
                nx, ny = x, y
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        break
                    elif mat[ny][nx] == 6:
                        break
                    elif mat[ny][nx] == 0:
                        mat[ny][nx] = -1
    
    
