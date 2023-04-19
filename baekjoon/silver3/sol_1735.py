import sys
import math

input = sys.stdin.readline

if __name__ == "__main__":
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    b = b1 * b2
    a = (a1 * b2) + (a2 * b1)
    cd = math.gcd(a, b)

    print(str(a // cd) + " " + str(b // cd))