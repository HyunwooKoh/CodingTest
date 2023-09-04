# N개의 최소공배수
from math import gcd

def solution(arr):
    ans = 0
    ans = arr[0]
    
    for num in arr:
        ans = ans * num // gcd(ans, num)
    return ans