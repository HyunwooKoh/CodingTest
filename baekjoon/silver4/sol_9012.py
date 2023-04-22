import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        str = input()
        count = 0
        for i in range(len(str)):
            if str[i] == '(':
                count += 1
            elif str[i] == ')':
                count -= 1

            if count < 0:
                break

        if count == 0:
            print("YES")
        else:
            print("NO")
