import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start, visited):
    visited[start]=True
    q = deque([start])
    while q:
        cur_node = q.popleft()
        for next in graph[cur_node]:
            if not visited[next]:
                visited[next]=True
                result[next]+=1
                q.append(next)

for i in range(1, n+1):
    visited=[False]*(n+1)
    bfs(graph, i, visited)
    
max_val = 0
for i in range(1, n+1):
    max_val = max(max_val, result[i])
        
for i in range(1,n+1):
    if max_val==result[i]:
        print(i, end=" ")