#https://school.programmers.co.kr/learn/courses/30/lessons/68935
import sys
input = sys.stdin.readline

def solution(num):
    rev_base = ''
    while num > 0:
        num, mod = divmod(num,3)
        rev_base += str(mod)
    
    return int(rev_base, 3)

if __name__ == "__main__":
    num = int(input().strip())
    print(solution(num))