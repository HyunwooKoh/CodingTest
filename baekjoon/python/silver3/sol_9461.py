import sys
input = sys.stdin.readline

if __name__ == "__main__":
    p = [0,1,1,1] # list P(n) init for case n = 0,1,2,3 
    for _ in range(int(input())):
        num = int(input())
        if len(p) <= num:
            for i in range (len(p) , num + 1):
                p.append(p[i - 3] + p[i - 2])
        print(p[num])