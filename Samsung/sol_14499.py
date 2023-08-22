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
        nx = x + dx[o]
        ny = y + dy[o]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        x , y = nx, ny
        
        # move dice
        if o == 3:
            temp = dice[5]
            dice[5] = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = temp
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
            mat[y][x] = 0

        print() # Top of Dice
