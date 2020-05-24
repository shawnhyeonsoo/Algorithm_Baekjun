import sys
from collections import deque
r = sys.stdin.readline

def ripe(M, N, array):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    days = -1

    while ripe_list:
        days += 1
        for _ in range(len(ripe_list)):
            x, y = ripe_list.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (array[nx][ny] == 0) and (0 <= nx < N) and (0 <= ny < M):
                    array[nx][ny] = array[x][y] + 1
                    ripe_list.append([nx, ny])

    for b in array:
        if 0 in b:
            return -1
    return days


M, N = map(int, r().split())
A, ripe_list = [], deque()
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(M):
        if row[j] == 1:
            ripe_list.append([i, j])
    A.append(row)


print(ripe(M, N, A))