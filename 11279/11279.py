import heapq
import sys
heap = []
for i in range(int(input())):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        if not heap:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))