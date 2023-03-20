if __name__ == "__main__":
    x, y = map(int, input().split())

    if (x < 0 or x > 1000000000) or (y < 0 or y > x) :
        exit(-1)
    
    if x == y or (100 * y) // x == 99 :
        print(-1)
    else:
        z = (100 * y) // x 
        left = 0
        right = res = x
        while left <= right:
            mid = (left + right) // 2
            if (100 * (y + mid)) // (x + mid) > z:
                res = mid
                right = mid -1
            else:
                left = mid + 1
        print(res)