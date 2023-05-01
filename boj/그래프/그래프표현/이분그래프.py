import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

result = []

def dfs(graph, v, visited, set_list, cur_set):
    visited[v]=True
    set_list[v]=cur_set
    if cur_set==0:
        cur_set=1
    else:
        cur_set=0
    for next in graph[v]:
        if not visited[next]:
            dfs(graph, next, visited, set_list, cur_set)
        else:
            if set_list[next]!=cur_set:
                visited[0] = True

for _ in range(n):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False]*(v+1)
    set_list = [0]*(v+1)
    cur_set = 0
    bi_graph = True
    start_node = 0
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for s in range(1, v+1):
        if not visited[s]:
            dfs(graph, s, visited, set_list, cur_set)
    
    if not visited[0]:
        result.append("YES")
    else:
        result.append("NO")
        
for r in result:
    print(r)