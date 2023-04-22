import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    cards = deque([i for i in range(1, num + 1)])
    for _ in range(num - 1):
        cards.popleft()
        cards.append(cards.popleft())
    print(cards[0])
