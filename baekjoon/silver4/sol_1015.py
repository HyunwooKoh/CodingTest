if __name__ == "__main__":
    size = int(input())
    arr = input().split(' ')
    arr = [int(i) for i in arr]
    sortedArr = sorted(arr)

    res = ""
    for i in range(0,len(arr)):
        idx = sortedArr.index(arr[i])
        res += str(idx) + " "
        sortedArr[idx] = -1
    print(res)