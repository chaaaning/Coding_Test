# Greedy

**INDEX**
- [개요](#개요)
- [Stack](#Stack)
- [Queue](#Queue)
- [재귀함수(생략)](#재귀함수)
- [DFS/BFS](#dfsbfs)
    - [Graph](#graph)
    - [DFS](#dfs)
    - [BFS](#bfs)
---

## 개요

**탐색**이란 `많은 양의 데이터 중에서 원하는 데이터를 찾는 과정`을 의미한다. 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색 하는 문제를 자주 다룬다. 대표적인 탐색 알고리즘으로 DFS, BFS를 꼽을 수 있는데 이 두 알고리즘의 원리를 제대로 이해해야 코딩 테스트의 탐색 문제 유형을 해결할 수 있다. 그러나 DFs와 BFS를 제대로 이해하기 위해서는 기본 자료구조인 스택과 큐에 대한 이해가 있어야 하므로 스택, 큐, 재귀 함수를 정리해보자

**자료구조**란 `데이터를 표현하고 관리하고 처리하기 위한 구조`를 의미한다. 그 중 스택과 큐는 자료구조의 기초 개념으로 다음의 두 핵심적인 함수로 구성된다.
- 삽입(PUSH): 데이터를 삽입한다.
- 삭제(POP): 데이터를 삭제한다.

물론 실제 스택과 큐 사용 시에는 삽입, 삭제 이외에도 오버플로와 언더플로를 고민해야 한다.
- 오버플로: 특정 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생한다.(즉, 저장공간을 벗어나 데이터가 흘러 넘칠 때)
- 언더플로: 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행하면 데이터가 전혀 없는 상태에서 언더플로가 발생한다.

## Stack

- First In Last Out(선입후출) 구조 또는 Last In First Out(후입선출)구조 라고 한다.
- 간략히 구현한 Stack의 예시
    ```python
    stack=[]
    
    # 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()

    print(stack)        # 최하단 원소부터 출력
    print(stack[::-1])  # 최상단 원소부터 출력
    ```

## Queue

- First In First Out(선입선출) 구조
- 간단한 Queue 구현
    ```python
    from collections import deque

    queue = deque()

    # 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print(queue)        # 먼저 들어온 순서대로 출력
    queue.reverse()     # 다음 출력을 위해 역순으로 바꾸기
    print(queue)        # 나중에 들어온 원소부터 출력
    ```

## 재귀함수

- 생략합니다

## DFS/BFS

### Graph

- DFS를 이해하기 위해 그래프의 기본 구조부터 알아야 한다. 그래프는 **노드**(Node)와 **간선**(Edge)으로 표현되며 이때 노드를 **정점**(Vertex)이라고도 말한다. 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 만한다. 또한 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다'라고 표현한다.

- 프로그래밍에서 그래프는 크게 2가지 방식으로 표현할 수 있는데 코딩 테스트에서는 이 두 방식 모두 필요하다.
    - 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
    - 인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식

        **인접 행렬**(Adjacency Matrix)
        - 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다.
        - 연결되어 있지 않은 노드끼리는 무한의 비용이라고 작성한다.
        - 실제 코드에서는 논리적으로 정답이 될 수 없는 큰 값 중에서 999999999, 987654321 등의 값으로 초기화하는 경우가 많다.
        ```python
        INF = 999999999

        graph = [
            [0, 7, 5],
            [7, 0 , INF],
            [5, INF, 0]
        ]

        print(graph)
        ```

        **인접 리스트**(Adjacency List)
        - 모든 노드에 연결된 노드의 정보를 차례대로 연결하여 저장한다.
        - 전통적으로 C++나 Java에서는 Linked List 형태로 인접 리스트를 운용하지만 파이썬에서는 list 자료형을 사용하여 접근하도록 하자
        ```python
        graph = [[] for _ in range(3)]

        # 노드 0에 연결된 노드 정보 저장 (노드, 거리)
        graph[0].append((1,7))
        grapch[0].append((2,5))

        # 노드 1에 연결된 노드 정보 저장 (노드, 거리)
        graph[1].append((0,7))

        # 노드 2에 연결된 노드 정보 저장 (노드, 거리)
        graph[2].append((0,5))

        print(graph)
        ```
### DFS

- **DFS**는 Depth-First Search, `깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘`이다.
- 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘
- 동작 과정
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

dfs(graph,1,visited)
```

### BFS

- **BFS**(Breadth First Search) 알고리즘은 `너비 우선 탐색`이라는 의미를 가진다. 쉽게 말해 `가까운 노드부터 탐색하는 알고리즘`이다. DFS는 최대한 멀리 있는 노드를 우선을 탐색하는 방식으로 동작한다면 BFS는 이와 반대이다.

- BFS에서는 선입선출 방식의 큐 자료구조를 이용한다. 인접한 노들르 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스레 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행한다.

- BFS 동작 방식
    1. 탐색 시작 노들를 큐에 삽입하고 방문 처리한다.
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            queue.append(i)
            visited[i]=True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(graph,1,visited)
```