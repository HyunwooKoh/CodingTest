import sys
input = sys.stdin.readline

if __name__ == "__main__":
    stack = []
    for _ in range(int(input())):
        cmdList = input().split()
        cmd = ''
        num = 0
        if  len(cmdList) == 1:
            cmd = cmdList[0]
        else:
            cmd = cmdList[0]
            num = int(cmdList[1])
        if cmd == 'push':
            stack.append(num)
        elif cmd == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif cmd == 'size':
            print(len(stack))
        elif cmd == 'empty':
            print(1 if len(stack) == 0 else 0)
        elif cmd == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack)-1])
