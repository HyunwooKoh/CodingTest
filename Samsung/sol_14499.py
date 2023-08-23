import sys
input = sys.stdin.readline

# x, 동, 서, 북, 남
dx = [0, 0,0,-1,0] 
dy = [0, 1,-1,0,0]

# bottom, left, front, back, right, top
dice = [0,0,0,0,0,0]

if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))
    orders = list(map(int, input().split()))

    for o in orders :
        print(mat)
        print(dice)
        nx = x + dx[o]
        ny = y + dy[o]
        if 0<= nx < m and 0 <= ny < n:        
            x , y = nx, ny
            # move dice
            if o == 3:
                temp = dice[5]
                dice[5] = dice[2]
                dice[2] = dice[0]
                dice[0] = dice[3]
                dice[3] = temp
            elif o == 4:
                temp = dice[3]
                dice[3] = dice[0]
                dice[0] = dice[2]
                dice[2] = dice[5]
                dice[5] = temp
            elif o == 1:
                temp = dice[1]
                dice[1] = dice[0]
                dice[0] = dice[4]
                dice[4] = dice[5]
                dice[5] = temp
            elif o == 2:
                temp = dice[4]
                dice[4] = dice[0]
                dice[0] = dice[1]
                dice[1] = dice[5]
                dice[5] = temp


            # process logic
            if mat[y][x] == 0:
                mat[y][x] = dice[0]
            else:
                # copy mat[y][x] to bottom of dice
                dice[0] = mat[y][x]
                mat[y][x] = 0
            print(dice[5]) # Top of Dice
