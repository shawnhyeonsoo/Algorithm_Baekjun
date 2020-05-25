import sys
from collections import deque

def BFS(total,ripe_list):
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    count = -1
    while ripe_list:
        for _ in range(len(ripe_list)):
            ripe = ripe_list.popleft()
            ripex = ripe[0]
            ripey = ripe[1]%N
            ripez = ripe[1]//N
            for k in range(6):
                mx = ripex + dx[k]
                my = ripey + dy[k]
                mz = ripez + dz[k]
                if (0<= mx < M) and (0<= my < N) and (0<= mz < H) and total[(N*mz)+my][mx] == 0:
                    total[(N * mz) + my][mx] = 1
                    ripe_list.append((mx,(N*mz)+my))
        count += 1

    for b in total:
        if 0 in b:
            return -1
    return count

M, N, H = map(int,sys.stdin.readline().split())
ripe_list = deque()
total = []
for i in range(N*H):
    B = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        if B[j] == 1:
            ripe_list.append((j,i))
    total.append(B)

print(BFS(total,ripe_list))