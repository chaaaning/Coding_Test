import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
visited = [False]*(n+1)

def bfs(graph, start, visited, target):
    result=[]
    dist_q = deque([0])
    q = deque([start])
    visited[start] = True
    
    while q:
        now = q.popleft()
        cur_dist = dist_q.popleft()
        if cur_dist == target:
            result.append(now)
        elif cur_dist > target:
            return result
        next_dist = cur_dist + 1
        for connect in graph[now]:
            if not visited[connect]:
                q.append(connect)
                dist_q.append(next_dist)
                visited[connect] = True
    return result

ans = bfs(graph, x, visited, k)
ans.sort()
if not ans:
    print(-1)
else:
    for a in ans:
        print(a)