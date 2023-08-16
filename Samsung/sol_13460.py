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
    for i in range(10):
        print("##################")
        if success:
            break
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if rx == ox and ry == oy:
                res = i
                print(res)
                success = True
                break
            
            for j in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[j]
                    nry += dy[j]
                    print("nrx : " + str(nrx) + ", nry : " + str(nry))
                    if mat[nry][nrx] == '#':
                        nrx -= dx[j]
                        nry -= dy[j]
                        break
                    elif nrx == ox and nry == oy:
                        print("!!!!!!!!!!!!!! : " + str(i))
                        break
                
                blueHole = False
                nbx, nby = bx, by
                while True:
                    nbx += dx[j]
                    nby += dy[j]
                    print("nbx : " + str(nbx) + ", nby : " + str(nby))
                    if mat[nby][nbx] == '#':
                        nbx -= dx[j]
                        nby -= dy[j]
                        break
                    elif nbx == ox and nby == oy:
                        blueHole = True
                        break

                if blueHole:
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
    print(res)
                

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
    bfs(rx,ry,bx,by)