import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = [0, 1, 1]
    num = int(input())
    for i in range(3, num + 1):
      n.append(n[i - 2] + n[i - 1])
    print(n[num])