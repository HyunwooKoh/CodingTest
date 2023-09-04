import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())

    res = 0
    for num in a:
        if num <= b:
            res += 1
        else:
            res += 1 + ((num-b) // c)
            if (num-b) % c != 0:
                res += 1
    print(res)