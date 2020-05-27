[Baekjun Online Judge 1012번: 유기농 배추] </br>
출처: 백준 온라인 저지</br>
문제 링크: <https://www.acmicpc.net/problem/1012> </br>



문제 </br>
</br>차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.

(한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.

(0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)


![image](https://user-images.githubusercontent.com/35067611/65693961-11dbe380-e0b0-11e9-94cf-d1f06507a6b7.png)


</br>
</br>
입력</br>
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. </br>

</br>출력</br>
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.</br>

</br>
</br>
솔루션:</br>

```python
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
```
</br> 

> 첫 시도는 배추가 있는 위치가 입력될 때, 이를 따로 익은 배추의 위치 배열을 만들어 여기에 추가해주고, 이 배열에 있는 주소들로 BFS 혹은 DFS을 실행하는 방식으로
  구현해보았다. 입출력 예에 대해서 스스로 테스트를 했을 때에는 올바른 결과가 나왔지만, 이를 재출하고 채점을 받을 때는 아무리 수정해봐도 런타임 에러가 났다. 혹시 
  앞서 배웠듯이 배열에 대한 append 부분에 있어서 효율성 부분이 걸리는 것일까 싶어 이 배추 위치 배열을 삭제하고, 전체적인 행렬에 대해서 search를 하도록 코드를
  작성했더니 꽤나 효율적인 결과로 통과할 수 있었다. 


메모리: 31824KB
시간: 92ms
