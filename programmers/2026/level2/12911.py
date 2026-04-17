#https://school.programmers.co.kr/learn/courses/30/lessons/12911

import sys
input = sys.stdin.readline

def solution(n):
    count_1 = format(n,'b').count('1')
    while True:
        n +=1
        if format(n, 'b').count('1') == count_1:
            break

    return n 

if __name__ == "__main__":
    n = int(input().strip())
    print(solution(n))