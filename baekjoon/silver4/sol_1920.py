import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    A = list(sorted(map(int, input().split())))
    m = int(input())
    X = list(map(int, input().split()))

    for i in X:
        left = 0
        right = len(A) -1
        find = 0
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == i:
                find = 1
                break
            elif A[mid] > i:
                right = mid -1
            elif A[mid] < i:
                left = mid + 1
        print(find)