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
        rpx, rpy, bpx, bpy, cnt = queue.popleft()
        if cnt >= 10:
            continue

        print("POP")
        print("rx : " + str(rpx) + ", ry : " + str(rpy))        
        print("bx : " + str(bpx) + ", by : " + str(bpy))
                
        for i in range(4):
            red, blue = False, False
            rCnt, bCnt = 0, 0
            
            while True: # 빨간공 이동
                nrx = rpx + dx[i]
                nry = rpy + dy[i]
                if i == 2:
                    print(dx[i])
                    print(dy[i])
                    print(str(nrx) + " " + str(nry))
                if nrx < 0 or nrx >= m or nry < 0 or nry >= n:
                    break

                if mat[nry][nrx] == '#':
                    break
                else:
                    rCnt += 1
                    rpx = nrx
                    rpy = nry
                    if  mat[nry][nrx] == 'O':
                        red = True
                        break
            
            while True: # 파란공 이동
                nbx = bpx + dx[i]
                nby = bpy + dy[i]
                
                if nbx < 0 or nbx >= m or nby < 0 or nby >= n:
                    break

                if mat[nby][nbx] == '#':
                    break
                else:
                    bCnt += 1
                    bpx = nbx
                    bpy = nby
                    if mat[nby][nbx] == 'O':
                        blue = True
                        break
            if i == 2:
                print(i)
                print("rx : " + str(rpx) + ", ry : " + str(rpy))        
                print("bx : " + str(bpx) + ", by : " + str(bpy))
                print()
                    
            if red and not blue: # 빨간 공만 나간 경우
                res = cnt
                break
            elif not red and not blue: # 둘 다 안나간 경우
                if rpx == bpx and rpy == bpy:
                    if rCnt > bCnt: # 빨간 공이 뒤인 경우
                        rpx -= dx[i]
                        rpy -= dy[i]
                    else:           # 파란 공이 뒤인 경우
                        bpx -= dx[i]
                        bpy -= dy[i]
                if not rVisited[rpy][rpx] or not bVisited[bpy][bpx]:
                    rVisited[rpy][rpx] = True
                    bVisited[bpy][bpx] = True
                    queue.append((rpx, rpy, bpx, bpy, cnt+1))
    return res
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    rx, ry = -1, -1
    bx, by = -1, -1
    mat = []
    rVisited = [[False for _ in range(m)] for _ in range(n)]
    bVisited = [[False for _ in range(m)] for _ in range(n)]
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
    
    rVisited[ry][rx] = True
    bVisited[by][bx] = True
    print(bfs(rx, ry, bx, by))