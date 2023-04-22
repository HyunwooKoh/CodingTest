import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    five_rest = n % 5
    five_val = n // 5
    if five_rest > 0:
        if five_rest == 1 and five_val >= 1:
            print(five_val + 1)
        elif five_rest == 2 and five_val >= 2:
            print(five_val + 2)
        elif five_rest == 3:
            print(five_val + 1)
        elif five_rest == 4 and five_val >= 1:
            print(five_val + 2)
        else:
            print(-1)
    else:
        print(five_val)
