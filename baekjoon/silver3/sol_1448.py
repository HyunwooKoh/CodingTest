import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    p = []
    for _ in range(num):
        p.append(int(input()))
    
    p.sort(reverse=True)
    res = -1
    for i in range(num - 2):
        if p[i] < p[i+1] + p[i+2]:
            res = p[i] + p[i+1] + p[i+2]
            break
    print(res)