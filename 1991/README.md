[Baekjun Online Judge 1991번: 트리 순회] </br>
출처: 백준 온라인 저지</br>
문제 링크: <https://www.acmicpc.net/problem/1991> </br>



문제 </br>
</br>이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오. </br>

![image](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/201007/trtr.png)

예를 들어 위와 같은 이진 트리가 입력되면,

* 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
* 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
* 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

가 된다.

</br>


입력</br>
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다. </br>

</br>출력</br>
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.</br>

</br>
</br>
솔루션:</br>

```python
import string
Alphabet = string.ascii_uppercase
node = int(input())
node_graph = {i: [] for i in Alphabet}

for _ in range(node):
    node, left, right = map(str, input().split())
    node_graph[node] += [left, right]


def preorder(node_graph, root):
    stack = [root]
    result = ''

    while stack:
        node = stack.pop()
        result += node

        if node_graph[node][1] != '.':
            stack.append(node_graph[node][1])

        if node_graph[node][0] != '.':
            stack.append(node_graph[node][0])

    return result


def inorder(node_graph, root):
    stack = [root]
    result = ''

    while stack:
        if node_graph[stack[-1]][0] != '.' and node_graph[stack[-1]][0] not in result:
            stack.append(node_graph[stack[-1]][0])

        elif stack[-1] in result:
            stack.append(node_graph[stack[-1]][1])

        else:
            node = stack.pop()
            result += node
            if node_graph[node][1] != '.':
                stack.append(node_graph[node][1])

    return result


def postorder(node_graph, root):
    stack = [root]
    result = ''

    while stack:
        if node_graph[stack[-1]][0] != '.' and node_graph[stack[-1]][0] not in result:
            stack.append(node_graph[stack[-1]][0])

        elif node_graph[stack[-1]][1] == '.' or node_graph[stack[-1]][1] in result:
            result += stack.pop()

        else:
            stack.append(node_graph[stack[-1]][1])

    return result


print(preorder(node_graph, "A"))
print(inorder(node_graph, "A"))
print(postorder(node_graph, "A"))
```
</br> 

> 파이썬에서는 graph를 이용하여 트리를 구현하는 것이 간단한 것은 알고 있었지만, 알파벳을 어떻게 이용할까 고민하다가 생각난 것이 string 라이브러리였다. 이를
  이용해서 대문자 알파벳이 저장된 문자열을 만들었고, 이 문자열이랑 비교하며 입력된 변수에 대해서 트리를 구현했다. 그 이후엔 문제에 주어진 조건대로 전위, 중휘,
  후위 순회를 문제에 맞게 조건을 걸어주었는데, 스택 구조를 이용해서 할 수 있었다. 
  https://codingstarter.tistory.com/6?category=935492 여기를 보며 많이 참고해서 코드를 작성할 수 있었다.


메모리: 32940KB
시간: 124ms
