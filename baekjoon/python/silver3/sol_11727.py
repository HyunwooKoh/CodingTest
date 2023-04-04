import sys
input = sys.stdin.readline

if __name__ == "__main__":
    counts = [1,1]
    num = int(input())
    for i in range(2, num + 1):
        counts.append(counts[i-1] + 2 * counts[i-2])
    print(counts[num] % 10007)