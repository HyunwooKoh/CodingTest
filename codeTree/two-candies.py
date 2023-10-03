# ref https://www.codetree.ai/training-field/frequent-problems/problems/two-candies/
import sys
from collections import deque

input = sys.stdin.readline
dx = [0,0,1,-1] 
dy = [1,-1,0,0]

def bfs(r_x, r_y, b_x, b_y):
    queue = deque([])
    queue.append((r_x, r_y, b_x, b_y, 1))
    res = -1

    while queue and res == -1:
        rx, ry, bx, by, cnt = queue.popleft()
        if cnt > 10:
            continue

        for i in range(4):
            red, blue = False, False
            rCnt, bCnt = 0, 0
            nrx, nry = rx, ry
            nbx, nby = bx, by
            
            while True: # 빨간공 이동
                nrx += dx[i]
                nry += dy[i]
                rCnt += 1
                if nrx < 0 or nrx >= m or nry < 0 or nry >= n or mat[nry][nrx] == '#':
                    nrx -= dx[i]
                    nry -= dy[i]
                    rCnt -= 1
                    break
                elif  mat[nry][nrx] == 'O':
                        red = True
                        break
            
            while True: # 파란공 이동
                nbx += dx[i]
                nby += dy[i]
                bCnt += 1
                if nbx < 0 or nbx >= m or nby < 0 or nby >= n or mat[nby][nbx] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    bCnt -= 1
                    break
                elif mat[nby][nbx] == 'O':
                        blue = True
                        break
                    
            if red and not blue: # 빨간 공만 나간 경우
                res = cnt
                break
            elif not red and not blue: # 둘 다 안나간 경우
                if nrx == nbx and nry == nby:
                    if rCnt > bCnt: # 빨간 공이 뒤인 경우
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:           # 파란 공이 뒤인 경우
                        nbx -= dx[i]
                        nby -= dy[i]
                
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby, cnt+1))
                    visited.append((nrx, nry, nbx, nby))
    return res
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    rx, ry = -1, -1
    bx, by = -1, -1
    mat = []
    visited = []
    for i in range(n):
        line = list(input())
        for j in range(m):
            if line[j] == 'R':
                rx = j
                ry = i
            elif line[j] == 'B':
                bx = j
                by = i
        mat.append(line)
    
    visited.append((rx,ry,bx,by))
    print(bfs(rx, ry, bx, by))