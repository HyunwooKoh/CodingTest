#https://school.programmers.co.kr/learn/courses/30/lessons/70128

import sys
input = sys.stdin.readline


def solution(a, b):

    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer


if __name__ == "__main__":
    a = list(map(int,input().strip().split(',')))
    b = list(map(int,input().strip().split(',')))
    print(solution(a,b))