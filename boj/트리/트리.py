import sys
sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().split()))
del_node = int(input())
graph = [[] for _ in range(n)]
root_node = 0
for i, val in enumerate(input_list):
    if i==del_node:
        continue
    if val!=-1:
        graph[val].append(i)
    else:
        root_node=val

visited = [False]*n
def dfs(graph, v, visited, result=[]):
    visited[v] = True
    result.append(v)
    for next in graph[v]:
        if not visited[next]:
            result = dfs(graph, next, visited)
    return result
        
del_nodes = dfs(graph, del_node, visited)

for dNode in del_nodes:
    graph[dNode] = [-1]
    
result = 0
for i, g in enumerate(graph):
    if not g:
        result+=1
        
print(result)