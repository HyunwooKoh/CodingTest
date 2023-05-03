import sys
import math

input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    houses = []

    for _ in range(num):
        houses.append(list(map(int, input().split())))
    
    for i in range(1, num):
        houses[i][0] = min(houses[i - 1][1], houses[i - 1][2]) + houses[i][0]
        houses[i][1] = min(houses[i - 1][0], houses[i - 1][2]) + houses[i][1]
        houses[i][2] = min(houses[i - 1][0], houses[i - 1][1]) + houses[i][2]
    
    print(min(houses[num-1]))