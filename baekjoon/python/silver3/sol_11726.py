import sys
input = sys.stdin.readline

if __name__ == "__main__":
    counts = [0, 1, 2]
    num  = int(input())
    if num > 2:
        for i in range(3, num + 1):
          counts.append(counts[i - 2] + counts[i - 1])
    
    print(counts[num] % 10007)
