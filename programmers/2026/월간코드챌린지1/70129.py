#https://school.programmers.co.kr/learn/courses/30/lessons/70129

import sys
input = sys.stdin.readline

def solution(s):
    zero_count = 0
    count = 0

    while len(s) > 1:
        count += 1
        zero_count += s.count('0')
        s = s.replace('0','')
        s = format(len(s),'b')

    return [count, zero_count]
    

if __name__ == "__main__":
    x = input().strip()
    print(solution(x))