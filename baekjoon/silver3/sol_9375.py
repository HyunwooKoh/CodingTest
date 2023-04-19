import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        clothes = {}
        for _ in range(int(input())):
            cloth, type = input().split()
            if type in clothes:
                clothes[type] += 1
            else:
                clothes[type] = 1
        count = 1
        for i in clothes:
            count *= clothes[i] + 1
        print(count - 1)