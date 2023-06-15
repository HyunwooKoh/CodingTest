import sys
input = sys.stdin.readline

if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    c = [0] * len(line2)

    for i in range(len(line1)):
        cnt = 0
        for j in range(len(line2)):
            if cnt < c[j]:
                cnt = c[j]
            elif line1[i] == line2[j]:
                c[j] = cnt + 1
    print(max(c))