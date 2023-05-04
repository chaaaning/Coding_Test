import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
inv_graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    inv_graph[b].append((a, cost))
    indegree[b]+=1

start, end = map(int, input().split())

def topology_sort(graph, indegree):
    result = [0]*(n+1)
    q = deque([start])
    while q:
        node = q.popleft()
        for next, cost in graph[node]:
            indegree[next]-=1
            result[next] = max(result[next], result[node]+cost)
            if indegree[next]==0:
                q.append(next)
    return result

pathes = topology_sort(graph, indegree)

result = 0
visited = [False]*(n+1)
inv_q = deque([end])
visited[end] = True
while inv_q:
    node = inv_q.popleft()
    for pre_node, cost in inv_graph[node]:
        if pathes[node]==pathes[pre_node]+cost:
            result+=1
            if not visited[pre_node]:
                visited[pre_node] = True
                inv_q.append(pre_node)
                
print(pathes[end])
print(result)