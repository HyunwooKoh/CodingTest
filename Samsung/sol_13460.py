import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
mat = []

def bfs(rx,ry,bx,by):
    res = -1
    q = deque()
    visited =  deque()

    success = False
    q.append((rx,ry,bx,by))
    for i in range(1,11):
        if success:
            break
        for _ in range(len(q)):
            if success:
                break
            
            rx, ry, bx, by = q.popleft()
            for j in range(4):
                redHole = False
                nrx, nry = rx, ry
                while True:
                    nrx += dx[j]
                    nry += dy[j]
                    if mat[nry][nrx] == '#':
                        nrx -= dx[j]
                        nry -= dy[j]
                        break
                    elif nrx == ox and nry == oy:
                        redHole = True
                        break
                
                blueHole = False
                nbx, nby = bx, by
                while True:
                    nbx += dx[j]
                    nby += dy[j]
                    if mat[nby][nbx] == '#':
                        nbx -= dx[j]
                        nby -= dy[j]
                        break
                    elif nbx == ox and nby == oy:
                        blueHole = True
                        break

                if redHole and not blueHole:
                    success = True
                    res = i
                    break
                elif blueHole:
                    continue

                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[j]
                        nry -= dy[j]
                    else:
                        nbx -= dx[j]
                        nby -= dy[j]
                
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
    return res
                

if __name__ == "__main__":
    n, m = map(int, input().split())
    rx, ry, = -1, -1
    bx, by = -1, -1
    ox, oy = -1, -1

    for i in range(n):
        line = list(input())
        for j in range(m):
            if line[j] == 'R':
                rx, ry = j, i
            elif line[j] == 'B':
                bx, by = j, i
            elif line[j] == 'O':
                ox, oy = j, i
        mat.append(line)
    print(bfs(rx,ry,bx,by))