import sys
import heapq
heap = []
for i in range(int(sys.stdin.readline())):
    number = int(sys.stdin.readline())
    if number == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap,number)