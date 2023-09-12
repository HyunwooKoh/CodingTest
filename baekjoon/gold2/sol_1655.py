import sys
import heapq

input = sys.stdin.readline
if __name__ == "__main__":
    maxHeap = [] # 최대 heap, 값을 음수처리하여 가장 작은 값을 최대로 관리
    minHeap = [] # 최소 heap
    for i in range(int(input())):
        num = int(input())

        if len(maxHeap) == len(minHeap):
            heapq.heappush(maxHeap, -num)
        else:
            heapq.heappush(minHeap, num)
        
        if minHeap and minHeap[0] < -maxHeap[0]:
            leftValue = heapq.heappop(maxHeap)
            rightValue = heapq.heappop(minHeap)

            heapq.heappush(maxHeap, -rightValue)
            heapq.heappush(minHeap, -leftValue)

        print(-maxHeap[0])