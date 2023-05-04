import sys
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort(graph, indegree):
    q = deque([])
    result = []
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        node = q.popleft()
        result.append(node)
        
        for next in graph[node]:
            indegree[next]-=1
            if indegree[next]==0:
                q.append(next)
    return result
res = topology_sort(graph, indegree)
for r in res:
    print(r, end=" ")