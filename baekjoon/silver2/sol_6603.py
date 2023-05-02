import sys
input = sys.stdin.readline

def dfs(depth, idx, select : list):
    if len(select) == 6:
        print(' '.join(map(str, select)))
        return
    else:
        for i in range(idx, len(s)):     
            select.append(s[i])
            dfs(depth + 1, i + 1, select)
            select.pop()


if __name__ == "__main__":
    while True:
        s = list(map(int, input().split()))
        if len(s) == 1 and s[0] == 0:
            break
        k = s[0]
        s = s[1:]

        dfs(0, 0, [])
        print("")
        