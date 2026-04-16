#https://school.programmers.co.kr/learn/courses/30/lessons/12924

import sys
input = sys.stdin.readline

def solution(n):
    count = 0

    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                count+=1
                break
            elif sum > n:
                break

    return count

if __name__ == "__main__":
    n = int(input().strip())
    print(solution(n))