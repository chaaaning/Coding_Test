import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
result = []
visited = [False]*(n+1)

def bfs(graph, start, visited, k):
    q = deque([(start, k)])
    visited[start]=True
    while q:
        node, dist = q.popleft()
        if dist==0:
            result.append(node)
        elif dist<0:
            break
        for next in graph[node]:
            if not visited[next]:
                visited[next]=True
                q.append((next, dist-1))
                
bfs(graph, x, visited, k)
result.sort()
if result:
    for r in result:
        print(r)
else:
    print(-1)