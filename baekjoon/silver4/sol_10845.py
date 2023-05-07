import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    queue = deque([])
    for _ in range(int(input())):
        cmd = list(map(str, input().split()))
        if cmd[0] == 'push':
            queue.append(int(cmd[1]))
        elif cmd[0] == 'pop':
            if len(queue) > 0:
                print(queue.popleft())
            else:
                print(-1)
        elif cmd[0] == 'size':
            print(len(queue))
        elif cmd[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'front':
            if len(queue) > 0 :
                print(queue[0])
            else:
                print(-1)
        elif cmd[0] == 'back':
            if len(queue) > 0:
                print(queue[len(queue) - 1])
            else:
                print(-1)
