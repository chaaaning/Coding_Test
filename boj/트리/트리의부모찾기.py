import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

twoway_graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    twoway_graph[a].append(b)
    twoway_graph[b].append(a)

visited = [False]*(n+1)
def dfs(graph, v, visited, result=[0]*(n+1)):
    visited[v]=True
    for next in graph[v]:
        if not visited[next]:
            result[next] = v
            result = dfs(graph, next, visited, result)
    return result

find_parent_nodes = dfs(twoway_graph, 1, visited)

for i in range(2, n+1):
    print(find_parent_nodes[i])