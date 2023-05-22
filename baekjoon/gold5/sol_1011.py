import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        x, y = map(int, input().split())
        dist = y - x
        n = 1
        while True:
            if n**2 <= dist < (n+1)**2 :
                break
            n += 1
        
        if dist == n**2 :
            print((n*2) - 1)
        elif n**2 < dist <= n*(n+1):
            print(n*2)
        else :
            print((n*2) + 1)