#예상 대진표# 1,2 -> 1
# 3,4 -> 2
# 5.6 -> 3
# -> 나머지가 있으면 +1
def solution(n,a,b):
    ans = 1
    while True:
        if (a // 2 + a % 2) == (b // 2 + b % 2):
            break
        else:
            a = a // 2 + 1 if a % 2 == 1 else a // 2
            b = b // 2 + 1 if b % 2 == 1 else b // 2
            ans += 1
    
    return ans