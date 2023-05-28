import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    y, x, di = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    d = [[0,-1], [1,0], [0,1], [-1,0]] # 북, 동, 남 서

    while True:
        # 현재 칸이 청소되어 있는지 확인
        if mat[y][x] == 0:
            res += 1
            mat[y][x] = 2
        
        # 주위 4칸의 상태 확인
        clean = False
        for i in range(1, 5):
            ndi = di - i if di - i >= 0 else di -i + 4            
            nx, ny = x + d[ndi][0], y + d[ndi][1]
            if 0 <= nx < m and 0 <= ny < n and mat[ny][nx] == 0:
                clean = True
                break
        
        # -> 주위 4칸이 모두 청소되어 있거나 벽임 
        if not clean:
            #   -> 뒷 칸으로 이동 가능하면 좌표 변경
            tempDI = di
            tempDI = di - 2 if di - 2 >= 0 else di + 2
            nx, ny = x + d[tempDI][0], y + d[tempDI][1]
            #   -> 뒷 칸으로 이동 불가능하면 break
            if nx < 0 or nx >= m or ny < 0 or ny > n or mat[ny][nx] == 1:
                break
            else:
                x, y = nx, ny
        else:
            # -> 주위 4칸 중 빈 칸이 있으면 반시계 방향으로 회전
            for _ in range(4):
                di = di - 1 if di - 1 >= 0 else di + 3
                nx , ny = x + d[di][0], y + d[di][1]
                if mat[ny][nx] == 0:
                    x, y = nx, ny
                    break
    print(res)