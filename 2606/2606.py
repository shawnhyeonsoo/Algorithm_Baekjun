N = int(input())
pairs = int(input())
graph = {}
for i in range(1,N+1):
    graph[i] = set()

for j in range(pairs):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
visited = []

def DFS(graph, root):
    for k in graph[root]:
        if k not in visited:
            visited.append(k)
            DFS(graph, k)

DFS(graph,1)
print(len(visited)-1)