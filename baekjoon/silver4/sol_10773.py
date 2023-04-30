import sys
input = sys.stdin.readline

if __name__ == "__main__":
    stack = []
    sum = 0
    for _ in range(int(input())):
        num = int(input())
        if num == 0:
            sum -= stack.pop()
        else:
            sum += num
            stack.append(num)        
    print(sum)