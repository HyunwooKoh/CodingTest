#ref https://www.codetree.ai/training-field/frequent-problems/problems/virus-experiment
import sys
input = sys.stdin.readline

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    mat = [[5]*n for _ in range(n)]
    pattern = [list(map(int, input().split())) for _ in range(n)]
    viruses = {}
    for _ in range(m):
        y,x,v = map(int, input().split())
        if (x-1, y-1) in viruses:
            viruses[(x-1,y-1)].append(v)
        else:
            viruses[(x-1,y-1)] = [v]
    
    for _ in range(k):
        # 칸 별 바이러스를 나이 어린순으로 정렬
        # 한 회차에서 남아있을 바이러스 구하기
        remainViruses = {}
        for (x,y) in viruses.keys():
            remain = []
            die = False
            viruses[(x,y)].sort()
            for v in viruses[(x,y)]:
                if mat[y][x] >= v and not die:
                    mat[y][x] -= v
                    remain.append(v+1)
                else:
                    die = True
                    mat[y][x] += v // 2

            # 해당 칸에서의 번식 수행
            if len(remain) > 0:
                if (x,y) in remainViruses:
                    remainViruses[(x,y)] += remain
                else:
                    remainViruses[(x,y)] = remain
                for v in remain:
                    if v % 5 == 0:
                        for i in range(8):
                            nx = x + dx[i]
                            ny = y + dy[i]
                        
                            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                continue
                            if (nx,ny) in remainViruses:
                                remainViruses[(nx,ny)].append(1)
                            else:
                                remainViruses[(nx,ny)] = [1]

        viruses = remainViruses
        for i in range(n):
            for j in range(n):
                mat[i][j] += pattern[i][j]
    
    res = 0
    for (x,y) in viruses.keys():
        res += len(viruses[(x,y)])
    print(res)