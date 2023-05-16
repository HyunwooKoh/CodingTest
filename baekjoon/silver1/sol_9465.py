import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        num = int(input())
        cards = [list(map(int, input().split())) for _ in range(2)]
        for i in range(1, num):
            if i == 1:
                cards[0][i] += cards[1][i - 1]
                cards[1][i] += cards[0][i - 1]
            else:
                cards[0][i] += max(cards[1][i - 1], cards[1][i - 2])
                cards[1][i] += max(cards[0][i - 1], cards[0][i - 2])
        print(max(cards[0][num-1], cards[1][num-1]))