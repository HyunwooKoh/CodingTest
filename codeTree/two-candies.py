# ref https://www.codetree.ai/training-field/frequent-problems/problems/two-candies/
import sys
from collections import deque

input = sys.stdin.readline
dx = [0,0,1,-1] 
dy = [1,-1,0,0]

def bfs(r_x, r_y, b_x, b_y):
    queue = deque([])
    queue.append((r_x, r_y, b_x, b_y, 0))
    res = -1

    while queue and res == -1:
        rx, ry, bx, by, cnt = queue.popleft()
        if cnt >= 10:
            continue

        for i in range(4):
            red, blue = False, False
            rCnt, bCnt = 0, 0
            
            while True: # 빨간공 이동
                nrx = rx + dx[i]
                nry = ry + dy[i]
                
                if nrx < 0 or nrx >= m or nry < 0 or nry >= n:
                    break

                rCnt += 1
                if mat[nry][nrx] == '#':
                    break
                elif  mat[nry][nrx] == 'O':
                    red = True
                    break
                else:
                    rx = nrx
                    ry = nry
        
            while True: # 파란공 이동
                nbx = rx + dx[i]
                nby = ry + dy[i]
                
                if nbx < 0 or nbx >= m or nby < 0 or nby >= n:
                    break

                bCnt += 1
                if mat[nby][nbx] == '#':
                    break
                elif mat[nby][nbx] == 'O':
                    blue = True
                else:
                    bx = nbx
                    by = nby

            if red and not blue: # 빨간 공만 나간 경우
                res = cnt
                break
            elif not red and not blue: # 둘 다 안나간 경우
                if rCnt > bCnt: # 빨간 공이 뒤인 경우
                    rx -= dx[i]
                    ry -= dy[i]
                else:           # 파란 공이 뒤인 경우
                    bx -= dx[i]
                    by -= dy[i]

                queue.append((rx, ry, bx, by, cnt+1))
    return res
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    rx, ry = -1, -1
    bx, by = -1, -1
    mat = []
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
    
    print(bfs(rx, ry, bx, by))