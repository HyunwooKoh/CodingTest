import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    street = list(map(int, input().split()))
    city = list(map(int, input().split()))
    
    price = city[0] * street[0]
    minPriceCity = 0
    for i in range(1, num -1):
        # 이전 도시에서 다음 도시로 갈때의 비용
        # 최소 도시에서 가스를 더 넣는 것 vs 다음 도시에서 가스를 더 넣는 것
        if city[i] < city[minPriceCity]:
            minPriceCity = i
        price += street[i] * city[minPriceCity]
    print(price)
        