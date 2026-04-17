#괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
#"()()" 또는 "(())()" 는 올바른 괄호입니다.
#")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
#'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

import sys
from collections import deque

input = sys.stdin.readline

def solution(s):
    answer = True
    
    de = deque()
    for i in range(len(s)):
        if s[i] == '(':
            de.append(s[i])
        else:
            if len(de) == 0:
                answer = False
                break
            else:
                de.pop()

    if answer == True and len(de) !=0:
        answer = False
        
    return answer

def solution2(s):
    answer = True
    
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            if count == 0:
                answer = False
                break
            else:
                count -= 1

    if count !=0:
        answer = False
        
    return answer

if __name__ == "__main__":
    str_list = input().strip()
    print(solution(str_list))