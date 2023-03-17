# DFS구현
# import sys
# sys.setrecursionlimit(100000)


# input = sys.stdin.readline

# v, e = map(int, input().split())

# graph = [[] for _ in range(v+1)]
# visited = [False]*(v+1)

# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# def dfs(graph, v, visited):
#     visited[v]=True
#     for nb in graph[v]:
#         if not visited[nb]:
#             dfs(graph, nb, visited)

# result = 0

# for i in range(1, v+1):
#     if not visited[i]:
#         result+=1
#         dfs(graph, i, visited)
    
# print(result)

# Union-Find 구현
import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [i for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

result = []
for p in parent[1:]:
    result.append(find_parent(parent, p))

print(len(set(result)))