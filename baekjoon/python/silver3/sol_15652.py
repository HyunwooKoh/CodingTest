import sys
input = sys.stdin.readline

def dfs(l : list, num, count):
    if len(l) == count:
        print(' '.join(map(str, l)))
    else:
        for i in range(l[len(l) - 1] if len(l) > 0 else 1, num + 1):
            l.append(i)
            dfs(l, num, count)
            l.pop()

if __name__ == "__main__":
    num, count = map(int, input().split())
    dfs([], num, count)