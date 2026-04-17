#https://school.programmers.co.kr/learn/courses/30/lessons/12973

import sys
input = sys.stdin.readline

from collections import deque
def solution(s):

    de = deque()
    for i in range(len(s)):
        if len(de) == 0:
            de.append(s[i])
        elif de[-1] == s[i]:
            de.pop()
        else:
            de.append(s[i])

    if len(de) == 0:
        return 1
    else:
        return 0
    

if __name__ == "__main__":
    s = input().strip()
    print(solution(s))