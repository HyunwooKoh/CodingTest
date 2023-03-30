import sys
input = sys.stdin.readline

if __name__ == "__main__":
    tryCount = int(input())
    counts = [0,1,2,4] # count for 0, 1,2,3
    for _ in range(tryCount):
        num = int(input())
        if num >= len(counts):
            for i in range(len(counts), num + 1):
                counts.append(counts[i - 1] + counts[i - 2] + counts[i - 3])
        print(counts[num])