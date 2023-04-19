import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    l = list(map(int,input().split()))
    
    for i in range(1, num):
        l[i] = max(l[i], l[i] + l[i-1])
    
    print(max(l))