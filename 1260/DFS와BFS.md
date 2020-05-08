[Baekjun Online Judge 1260번: DFS와 BFS] </br>
출처: 백준 온라인 저지</br>
문제 링크: <https://www.acmicpc.net/problem/1260> </br>



문제 </br>
</br>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다. </br>
</br>
입력</br>
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다. </br>

</br>출력</br>
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</br>

</br>
</br>
솔루션:</br>

```python
N, M, V = map(int,input().split())

graph = {}
for i in range(1,N+1):
    graph[i] = set()

for m in range(M):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)


def DFS(graph, V):
    visited = []
    stack = [V]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(list(graph[node] - set(visited)), reverse=True)

    return visited

def BFS(graph,v):
    visited = [v]
    tobevisited = sorted(list(graph[v]))

    while tobevisited:
        node = tobevisited.pop(0)
        if node not in visited:
            visited.append(node)
            tobevisited += sorted(list(graph[node]))

    return visited

for i in list(DFS(graph, V)):
    print(i, end=" ")
print()
for j in list(BFS(graph, V)):
    print(j, end= " ")
```
</br> 

> 기본적인 DFS 와 BFS에 관한 문제였다. DFS는 전에 바이러스 문제를 풀 때 구현해봐서 DFS는 자신있게 짜고 BFS를 힘들게 짜고 테스트를 다 해봤는데
  입출력 예는 다 맞는데도 틀렸다고 나오길래 한참 고민했다. 여기저기 찾아보다가 원래 구현한 DFS가 재귀함수로 구현해서 런타임 에러도 나고 시간도 오래걸리는
  문제였던 것 같다. 자신 있던 DFS 부분을 고치고, 마지막 print(DFS(graph,V))에서 위와 같이 고쳐서 제출했더니 겨우 통과했다. 


메모리: 30616KB
시간: 728ms
