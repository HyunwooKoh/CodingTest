import sys
input = sys.stdin.readline

def dfs(l : list, s : list, count):
    if len(l) == count:
        print(' '.join(map(str, l)))
    else:
        for i in range(len(s)):
            if not s[i] in l:
                l.append(s[i])
                dfs(l, s, count)
                l.pop()

if __name__ == "__main__":
    num, count = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    dfs([], s, count)