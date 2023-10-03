# ref https://www.codetree.ai/training-field/frequent-problems/problems/cube-rounding/
import sys
input = sys.stdin.readline

# 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
sqare = [0,0,0,0,0,0] #위, 앞, 좌, 뒤, 우, 밑

if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    direct = list(map(int, input().split()))

    for d in direct:
        #print("pos : " + str(y) + ", " + str(x)) 
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 방향에 맞게 정육면체 회전
        if d == 1 : # 동쪽
            # 우 -> 밑, 밑 -> 좌, 좌->위, 위->우
            temp = sqare[4]
            sqare[4] = sqare[0]
            sqare[0] = sqare[2]
            sqare[2] = sqare[5]
            sqare[5] = temp
        elif d == 2: # 서쪽
            # 위->좌, 좌->밑, 밑->우, 우->위
            temp = sqare[0]
            sqare[0] = sqare[4]
            sqare[4] = sqare[5]
            sqare[5] = sqare[2]
            sqare[2] = temp
        elif d == 3: # 북쪽
            # 위->뒤, 뒤->밑, 밑->앞, 앞->위
            temp = sqare[0]
            sqare[0] = sqare[1]
            sqare[1] = sqare[5]
            sqare[5] = sqare[3]
            sqare[3] = temp
        elif d == 4: # 남쪽
            # 위->앞, 앞->밑, 밑->뒤, 뒤->위
            temp = sqare[0]
            sqare[0] = sqare[3]
            sqare[3] = sqare[5]
            sqare[5] = sqare[1]
            sqare[1] = temp

        if mat[nx][ny] == 0:
            mat[nx][ny] = sqare[5] # 정육면체의 밑면
        else:
            sqare[5] = mat[nx][ny]
            mat[nx]n[y] = 0
        
        x = nx
        y = ny
        
        print(sqare[0])
