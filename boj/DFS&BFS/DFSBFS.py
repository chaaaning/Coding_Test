import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
d_res, b_res = [], []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph_s = list(map(lambda x: sorted(x), graph))

def dfs(graph, v, visited):
    global d_res
    visited[v] = True
    d_res.append(v)
    for nb in graph[v]:
        if not visited[nb]:
            dfs(graph, nb, visited)
            
def bfs(graph, start, visited):
    global b_res
    visited[start] = True
    q = deque([start])
    b_res.append(start)
    while q:
        now = q.popleft()
        for nb in graph[now]:
            if not visited[nb]:
                visited[nb]=True
                b_res.append(nb)
                q.append(nb)

d_visited, b_visited = [False]*(n+1), [False]*(n+1)
dfs(graph_s, v, d_visited)
bfs(graph_s, v, b_visited)
                
for d in d_res:
    print(d, end=" ")
print()
for b in b_res:
    print(b, end=" ")