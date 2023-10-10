# ref https://www.codetree.ai/training-field/frequent-problems/problems/biology-lab-intern
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]

if __name__ == "__main__":
    n, m, k = map(int, input().split())

    # Key = x좌표, y좌표
    # Value = 속도, 방향, 크기 
    molds = {}
    for _ in range(k):
        y, x, s, d, b = map(int, input().split())
        molds[(x-1,y-1)] = [s,d-1,b]

    res = 0
    for x in range(m):
        # 해당 열에서 처음 만나는 곰팡이 제거
        for y in range(n):
            if (x,y) in molds:
                res += molds[(x,y)][2]
                del molds[(x,y)]
                break

        if x != m-1:
            tmpDict = {}
            for (x,y) in molds.keys():
                mold = molds[(x,y)]
                nx = x + dx[mold[1]]*mold[0]
                ny = y + dy[mold[1]]*mold[0]

                while nx < 0 or nx >= m or ny < 0 or ny >= n:
                    if nx < 0: # 왼쪽 벽을 벗어난 경우
                        nx = abs(nx)
                        mold[1] = 2
                    elif nx >= m: # 오른쪽 벽을 벗어난 경우
                        nx = (m-1) - (nx - (m-1))
                        mold[1] = 3
                    elif ny < 0: # 위쪽 벽을 벗어난 경우
                        ny = abs(ny)
                        mold[1] = 1
                    elif ny >= n: # 아래쪽 벽을 벗어난 경우
                        ny = (n-1) - (ny - (n-1))
                        mold[1] = 0
                
                # 한 칸에 두마리 이상인 경우, 큰 곰팡이만 생존
                if not (nx,ny) in tmpDict or mold[2] > tmpDict[(nx,ny)][2]:
                    tmpDict[(nx,ny)] = mold
            molds = tmpDict
    print(res)