[Baekjun Online Judge 2667번: 단지번호붙이기] </br>
출처: 백준 온라인 저지</br>
문제 링크: <https://www.acmicpc.net/problem/2667> </br>



문제 </br>
</br><그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오. </br>

![images](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png)

</br>
입력</br>
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다. </br>

</br>출력</br>
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.</br>

</br>
</br>
솔루션:</br>

```python
def DFS(matrix, cnt, x, y):
    global N
    matrix[x][y]=0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        xpos = x + dx[i]
        ypos = y + dy[i]
        if xpos >= 0 and xpos < N and ypos >= 0 and ypos < N:
            if matrix[xpos][ypos] == 1:
                cnt = DFS(matrix, cnt+1, xpos, ypos)
    return cnt


N = int(input())

A = [list(map(int, input())) for i in range(N)]

ans = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            ans.append(DFS(A, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)
```
</br> 

> 여러 코딩테스트를 볼 때, 비슷한 문제가 항상 나와 도전해보고 싶었던 유형의 문제였다. 문제를 보면 DFS 혹은 BFS를 사용해서 접근할 수 있을 것 같은데,
  위의 소스코드는 DFS를 사용한 코드다. 사실 처음에 접근하는 것이 난감해 어떻게 단지별로 구분해야하나 싶었는데, 한 DFS를 수행하면서 지나온 좌표는 모두
  0으로 변환해도 되지 않으며, 그렇게 하면 더 편하지 않을까 싶어서 그렇게 접근해봤다. 또한 처음에 접근할 때는 위와 같이 한 좌표에서 상하좌우 다 하는 것이
  아닌, 한 점에서 출발해서 주변에 1이 없을때까지 계속해서 좌표를 이동하는 방법을 택했는데, 시간초과로 이어졌다. 다른 분들의 코드를 보며, dx, dy 식으로
  길이 4의 배열을 두 개 만들어서 좌, 우, 상, 하 로 방향을 for문을 이용해서 접근하는 것을 보고 응용해보았다. 


메모리: 29456KB
시간: 64ms
