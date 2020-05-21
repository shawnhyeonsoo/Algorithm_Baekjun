[Baekjun Online Judge 2178번: 미로 탐색] </br>
출처: 백준 온라인 저지</br>
문제 링크: <https://www.acmicpc.net/problem/2178> </br>



문제 </br>
</br>N×M크기의 배열로 표현되는 미로가 있다.

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.</br>
</br>
입력</br>
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.</br>

</br>출력</br>
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.</br>

</br>
</br>
솔루션:</br>

```python
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
q = deque()
check = [[False] * m for i in range(n)]
dist = [[0] * m for j in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q.append((0, 0))
check[0][0] = True
dist[0][0] = 1

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == False and a[nx][ny] == 1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = True

print(dist[n - 1][m - 1])
```
</br> 

> 문제를 처음 접했을 때, DFS 관련 문제인듯 해서 DFS를 이용하여 문제를 풀어보려 했으나, 반복되는 시간초과로 인해 방법을 찾아보며 많은 코드들을 참고하게 되었다.
  기본적으로 앞선 DFS/BFS 문제와 같이 dx, dy 라는 배열을 선언해주고, 이 변수를 이용하여 움직이는 방향을 구현해주었다. 자료를 많이 찾아보며 deque 라이브러리
  를 사용하게 되었는데, 매우 효율적인 것 같았다. 시간이 생각보다 많이 소요되서 혹시 다른 방법이 있다면 찾아보는 것이 필요할 것 같다. 


메모리: 31928KB
시간: 112ms
