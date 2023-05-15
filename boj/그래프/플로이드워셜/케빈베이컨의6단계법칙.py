import sys

input = sys.stdin.readline

INF = sys.maxsize
n, m = map(int, input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for i in range(1, n+1):
    graph[i][i]=0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a!=b:
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
min_kb_num, kb_index = INF, 0
for i,g in enumerate(graph[1:]):
    cur_kb_num = sum(g[1:])
    if cur_kb_num < min_kb_num:
        min_kb_num = cur_kb_num
        kb_index=i+1
print(kb_index)