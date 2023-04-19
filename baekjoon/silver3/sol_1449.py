if __name__ == "__main__":
    n, l = map(int, input().split())
    hole = list(map(int, input().split()))
    hole.sort()

    end = hole[0] + l - 0.5
    count = 1
    for i in range(1, len(hole)):
        if hole[i] <= end:
            continue
        else:
            end = hole[i] + l - 0.5
            count += 1
    print(count)