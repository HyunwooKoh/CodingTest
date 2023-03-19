if __name__ == "__main__":
    size = int(input())
    arrA = [int(i) for i in input().split(' ')]
    arrB = [int(i) for i in input().split(' ')]
    arrA.sort()
    res = 0
    for i in range(size):
        res += arrA[i] * arrB.pop(arrB.index(max(arrB)))
    print(res)