import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    brokenCount = int(input())
    brokenList = None
    if brokenCount == 0:
        brokenList = []
    else:
        brokenList = list(map(int, input().split()))
    
    res = abs(100 - n)
    for i in range(1000001): 
        s = str(i)
        for j in range(len(s)):
            if int(s[j]) in brokenList:
                break
            elif j == len(s) - 1:
                res = min(res, len(s) + abs(i - n))

    print(res)