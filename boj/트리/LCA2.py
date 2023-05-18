import sys
from collections import deque

input=sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depths = [0]*(n+1)
visited = [False]*(n+1)
temp, max_depth = 1, 0
while temp <= n:
    temp <<= 1
    max_depth+=1

parents = [[0]*(n+1) for _ in range(max_depth+1)]

def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        node = q.popleft()
        for next in tree[node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                depths[next] = depths[node]+1
                parents[0][next] = node

bfs(1)

for i in range(1, max_depth+1):
    for j in range(1, n+1):
        parents[i][j] = parents[i-1][parents[i-1][j]]
        
def executeLCA(a, b):
    if depths[b] < depths[a]:
        a, b = b, a
    for k in range(max_depth, -1, -1):
        if 2**k <= depths[b]-depths[a]:
            if depths[a] <= depths[parents[k][b]]:
                b = parents[k][b]
    for k in range(max_depth, -1, -1):
        if a==b: break
        if parents[k][a] != parents[k][b]:
            a = parents[k][a]
            b = parents[k][b]
    LCA = a
    if a!=b:
        LCA = parents[0][LCA]
    return LCA

m = int(input())
result = []
for _ in range(m):
    a, b = map(int, input().split())
    result.append(executeLCA(a,b))
    
for r in result:
    print(r)