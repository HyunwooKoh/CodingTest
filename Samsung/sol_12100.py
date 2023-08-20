import sys
from copy import deepcopy
input = sys.stdin.readline

def up(board):
    for j in range(n):
        p = 0
        for i in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[p][j] == 0:
                    board[p][j] = tmp
                elif board[p][j]  == tmp:
                    board[p][j] *= 2
                    p += 1
                else:
                    p += 1
                    board[p][j] = tmp
    return board


def down(board):
    for j in range(n):
        pointer = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board


def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer]= tmp
    return board


def right(board):
    for i in range(n):
        p = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][p] == 0:
                    board[i][p] = tmp
                elif board[i][p]  == tmp:
                    board[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    board[i][p] = tmp
    return board


def dfs(mat, count):
    if count == 5:
        return max(map(max, mat))
    else:
        return max(dfs(up(deepcopy(mat)),count+1),dfs(down(deepcopy(mat)),count+1),dfs(right(deepcopy(mat)),count+1),dfs(left(deepcopy(mat)),count+1))


if __name__ == "__main__":
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    print(dfs(mat, 0))