import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__" : 
    inputString = input()
    stickCount = 0
    count = 0
    for i in range(0, len(inputString)):
        # 연속해서 ()가 오는 경우 -> 레이저
        if inputString[i] == '(' and inputString[i+1] == ')':
            if stickCount > 0 :
                count += stickCount
            i += 1
        # '('로 열린 후 ')'로 바로 닫히지 않으면 막대기 
        elif inputString[i] == '(' and not inputString[i+1] == ')':
            stickCount += 1
            count += 1
        # ')'로 닫힌 경우 중 직전이 '('가 아닌 경우(레이저)에는 막대기 수 -1
        elif inputString[i] == ')' and not inputString[i-1] == '(':
            stickCount -=1
    print(count) 
