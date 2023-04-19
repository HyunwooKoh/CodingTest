import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    maxHeap = []
    for _ in range(int(input())):
        num = int(input())
        if num == 0:
            try:
                print(-heapq.heappop(maxHeap))
            except:
                print(0)
        else:
            heapq.heappush(maxHeap, -num)