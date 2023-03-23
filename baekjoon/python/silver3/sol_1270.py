n = int(input())

if __name__ == "__main__":
    for _ in range(n):
        data = tuple(map(int, input().split()))
        army = {}
        for i in range(1, len(data)):
            if data[i] in army:
                army[data[i]] += 1
            else:
                army[data[i]] = 1
        res = -1
        dup = False
        for key in army:
            if army[key] > data[0] / 2:
                if res != -1:
                    dup = True
                    break
                res = key
        if dup or res == -1:
            print("SYJKGW")
        else:
            print(res)
        
