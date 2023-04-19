# lwh = n * a^3 -> a를 구하고
# 이분 탐색
# l // a -> 가로 최대 개수
# w // a -> 세로 최대 개수
# (l //a) * (w // a) -> 한 층의 개수
# (h // a) -> h내에서 가능한 층 수
#  n / (l //a) * (w // a) -> 필요 높이
if __name__ == "__main__":
    n, l, w, h = map(int, input().split())
    right = min([l,w,h])
    left = 0
    for _ in range(10000):
        mid = (left + right) / 2
        if (l // mid) * (w // mid) * (h // mid) >= n:
            left = mid
        else:
            right = mid
    print(right)