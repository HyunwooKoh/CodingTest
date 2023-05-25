import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        calc = list(map(str, input().strip()))
        listLen = int(input())
        flag = False
        front = True

        queue = deque(input().strip()[1:-1].split(","))
        if listLen == 0:
            queue = deque()
    
        for c in calc:
            if c == 'R':
                front = not front
            elif c == 'D':
                if len(queue) == 0:
                    flag = True
                    print("error")
                    break
                else:
                    if front:
                        queue.popleft()
                    else:
                        queue.pop()

        if not flag:
            if not front:
                queue.reverse()
            print("[" + ",".join(queue) + "]")