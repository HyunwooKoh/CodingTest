import sys
import math
input = sys.stdin.readline

if __name__ == "__main__":
    primeList = [False] * (123456 * 2 + 1)
    for i in range(1, 123456 * 2 + 1):
        isPrime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primeList[i] = True
    
    while True:
        num = int(input())
        if num == 0:
            break
        res = 0
        for i in range(num+1 , 2 * num + 1):
            if primeList[i]:
                res += 1
        print(res)