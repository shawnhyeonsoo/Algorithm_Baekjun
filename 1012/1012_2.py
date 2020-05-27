import sys
from collections import deque
sys.setrecursionlimit(50000)

def search(i,j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    to_visit = deque()
    to_visit.append((i,j))
    while to_visit:
        node = to_visit.popleft()
        x, y = node[0], node[1]
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if (0<= mx <M ) and (0<= my < N) and (total[my][mx] == 1):
                total[my][mx] = 'a'
                to_visit.append((mx,my))


for t in range(int(sys.stdin.readline())):
    M,N,K = map(int,sys.stdin.readline().split())
    to_visit = deque()
    count = 0
    total = [[0]*M for j in range(N)]
    for _ in range(K):
        a,b = map(int,sys.stdin.readline().split())
        total[b][a] = 1

    for q in range(N):
        for w in range(M):
            if total[q][w] == 1:
                search(w,q)
                total[q][w] = 'a'
                count += 1

    print(count)