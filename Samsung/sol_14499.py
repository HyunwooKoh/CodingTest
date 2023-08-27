import sys
input = sys.stdin.readline

# x, 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
    
if __name__ == "__main__":
    n, m, x, y, k = map(int,input().split())
    dice = [0,0,0,0,0,0]
    mat = []

    for i in range(n):
        mat.append([int(x) for x in input().rstrip().split()])
    command = [int(x) for x in input().rstrip().split()]

    for i in command:
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            x, y = nx, ny
            if i == 1:
                temp = dice[1]
                dice[1] = dice[0]
                dice[0] = dice[4]
                dice[4] = dice[5]
                dice[5] = temp
            elif i == 2:
                temp = dice[4]
                dice[4] = dice[0]
                dice[0] = dice[1]
                dice[1] = dice[5]
                dice[5] = temp
            elif i == 3:
                temp = dice[5]
                dice[5] = dice[2]
                dice[2] = dice[0]
                dice[0] = dice[3]
                dice[3] = temp
            elif i == 4:
                temp = dice[3]
                dice[3] = dice[0]
                dice[0] = dice[2]
                dice[2] = dice[5]
                dice[5] = temp

            if mat[x][y] == 0:
                mat[x][y] = dice[0]
            else:
                dice[0] = mat[x][y]
                mat[x][y] = 0
            print(dice[5])