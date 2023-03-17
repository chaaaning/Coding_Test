import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0

def dfs(graph, v, depth, visited):
    global answer
    visited[v] = True
    depth+=1
    if depth > 4:
        answer = 1
        return
    for nb in graph[v]:
        if not visited[nb]:
            dfs(graph, nb, depth, visited)
    visited[v] = False
    
for i in range(n):
    visited = [False]*n
    dfs(graph, i, 0, visited)
    if answer==1:
        break

print(answer)