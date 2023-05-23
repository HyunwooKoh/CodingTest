import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":
    l, c = map(int, input().split())
    constant = []
    vower = []
    for ch in list(map(str, input().split())):
        if ch in ['a', 'e', 'i', 'o', 'u']:
            vower.append(ch)
        else:
            constant.append(ch)

    #한개의 모음, 두개의 자음
    res = []
    for i in range(1, l - 1):
        if i > len(vower):
            break
        for v in combinations(vower, i):
            vString =  ''.join(v)
            for c in combinations(constant, l - i):
                resComp = vString + ''.join(c)
                res.append(''.join(sorted(resComp)))
    print('\n'.join(sorted(res)))