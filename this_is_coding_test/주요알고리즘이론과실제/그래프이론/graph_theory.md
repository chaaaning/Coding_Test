# Graph

**INDEX**
- [개요](#개요)
- [서로소 집합](#서로소-집합)
- [신장 트리](#신장-트리)
- [위상 정렬](#위상-정렬)
---

## 개요

- 이전에 다루었던 DFS, BFS, Dijkstra, 플루이드 워셜 등의 알고리즘은 모두 그래프 알고리즘의 한 유형으로 볼 수 있다.

- 앞으로 배울 크루스칼 알고리즘의 경우 그리디 알고리즘으로 분류되며, 위상 정렬 알고리즘은 앞서 배운 큐, 스택 자료구조를 활용해야 구현할 수 있다.

- 그래프는 `Node`와 이를 연결하는 `Edge`의 정보를 가지고 있는 자료구조를 의미한다. 알고리즘 문제를 접했을 때 '서로 다른 개체가 연결되어 있다'는 내용이 있다면 그래프 알고리즘을 떠올려야 한다.

- 더 나아가 그래프 자료구조 중에서 트리 자료구조는 다양한 알고리즘에서 사용되므로 곡 기억해야 한다. Dijkstra 알고리즘음을 구현하기 위해 우선순위 큐를 구현했고, 이를 위해서는 최소(혹은 최대)힙을 이용해야 한다. 그래프와 트리 자료구조를 비교하면 다음과 같다.
    |          | 그래프                      | 트리          |
    |----------|-----------------------------|--------------|
    | 방향성   | 방향 그래프 혹은 무방향 그래프| 방향 그래프   |
    | 순환성   | 순환 및 비순환               | 비순환        |
    | 루트 노드 존재 여부 | 루트 노드 없음 | 루트 노드 존재    |
    | 노드간 관계성 | 부모와 자식 관계 없음| 부모와 자식 관계  |
    | 모델의 종류 | 네트워크 모델         | 계층 모델         |

- 또한 그래프 구현 방법 2가지 방식을 기억하자
    > 인접 행렬 (Adjacency Matrix): 2차원 배열을 사용하는 방식
    > 인접 리스트 (Adjacency List): 리스트를 사용하는 방식

## 서로소 집합

- **서로소 집합(Disjoint Sets)** 이란 공통 원소가 없는 두 집합을 의미한다. 이러한 서로소 집합 자료 구조는 *서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조*라고 할 수 있다. 서로소 집합 자료구조는 union과 find 2개의 연산으로 조작하므로 union-find 자료구조라고 불리기도 한다.

- 서로소 집합 자료구조를 구현할 때는 트리 자료구조를 이용하여 집합을 표현하는데, 서로소가 집합 정보(합집합 연산)가 주어졌을 때 트리 자료구조를 이용해서 집합을 표현하는 서로소 집합 계산 알고리즘은 다음과 같다.
    ```
    1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
        ⑴ A와 B의 루트 노드 A', B'를 각각 찾는다.
        ⑵ A'를 B'의 부모 노드로 설정한다.(B'가 A'를 가리키도록 한다.)
    2. 모든 union 연산을 처리할 때까지 1번의 과정을 반복한다.
    ```

**서로소 집합 알고리즘 코드**
```python
# 경로 압축이 적용된 find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
```

- 서로소 집합은 다양한 알고리즘에 사용될 수 있다. 특히 서로소 집합은 무방향 그래프 내에서의 사이클 판별 시 사용할 수 있다. 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.

- 앞서 union 연산은 그래프에서의 간선으로 표현될 수 있따고 했다. 따라서 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 과정을 반복하는 것만으로도 사이클을 판별할 수 있다. 알고리즘은 다음과 같다.
    ```
    1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
        ⑴ 루트노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
        ⑵ 루트 노드가 서로 같다면 Cycle이 발생한 것이다.
    2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정을 반복한다.
    ```
**서로소 집합을 이용한 사이클 판별**
```python
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    retunr parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: parent[b]=a
    else: parent[a]=b

v, e = map(int, input().split())
parent = [i for i in range(0, v+1)]

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle=True
        break
    else:
        union_parent(parent, a, b)
```

## 신장 트리

- 신장 트리(Spanning Tree)란 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다. 이때 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 성립 조건이기도 하다.

- 신장 트리는 위와 같은 조건에서 여러 개가 생성된다. 이때 신장 트리 중에서 최소 비용으로 만들 수 있는 신장트리를 찾는 알고리즘을 '최소 신장 트리 알고리즘'이라고 한다. 대표적인 최소 신장 트리 알고리즘으로는 **크루스칼 알고리즘(Kruskal Algorithm)이 있다.

- 기본적으로 크루스칼 알고리즘은 그리디 알고리즘으로 분류된다. 먼저 모든 간선에 대해 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 포함시키면 된다. 이때 사이클을 발생시키는 간선은 집합에 포함시키지 않는다. 알고리즘은 다음과 같다.
    ```
    1. 간선 데이터를 비용에 따라 오름차순 정렬한다.
    2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
        ⑴ 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
        ⑵ 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
    3. 모든 간선에 대하여 2번 과정을 반복한다.
    ```
**크루스칼 알고리즘 소스코드**
```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: parent[b] = a
    else: parent[a] = b

v, e = map(int, input().split())
parent = [i for i in range(0, v+1)]
edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
```

## 위상 정렬

- **위상 정렬(Topology Sort)** 은 정렬 알고리즘의 일종으로, 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용하는 알고리즘이다. 이는 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'이다.

- 위상 정렬을 이해하기 위해서는 먼저 진입차수(Indegree)를 알아야 한다. 진입차수란 특정한 노드로 '들어오는' 간선의 개수를 의미한다. 위상 정렬의 알고리즘은 다음과 같다.
    ```
    1. 진입차수가 0인 노드를 큐에 넣는다.
    2. 큐가 빌 때까지 다음의 과정을 반복한다.
        ⑴ 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
        ⑵ 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
    ```
**위상 정렬 알고리즘**
```python
from collections import deque

v, e = map(int, input().split())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    return result
```