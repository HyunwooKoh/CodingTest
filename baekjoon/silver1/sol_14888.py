import sys
input = sys.stdin.readline

MAX = -(10**8)
MIN = 10**8

def dfs(idx, total, plus, minus, mul, div):
    if idx == num:
        global MAX
        global MIN
        MAX = max(total, MAX)
        MIN = min(total, MIN)
        return
    if plus:
        dfs(idx + 1, total + nums[idx], plus-1, minus, mul, div)
    if minus:
        dfs(idx + 1, total - nums[idx], plus, minus-1, mul, div)
    if mul:
        dfs(idx + 1, total * nums[idx], plus, minus, mul-1, div)
    if div:
        dfs(idx + 1, int(total / nums[idx]), plus, minus, mul, div-1)

if __name__ == "__main__":
    num = int(input())
    nums = list(map(int, input().split()))
    op = list(map(int, input().split()))

    dfs(1, nums[0], op[0], op[1], op[2], op[3])
    print(MAX)
    print(MIN)
        