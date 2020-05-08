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
            # 스택은 뒤부터 나가니 역순 정렬

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