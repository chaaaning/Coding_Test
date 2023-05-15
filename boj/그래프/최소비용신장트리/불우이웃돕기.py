import sys
from collections import deque

input=sys.stdin.readline

n = int(input())

wran_length = dict()
total_length = 0
for i in range(1, 27):
    wran_length[chr(i+96)] = i

for i in range(27, 53):
    wran_length[chr(i+38)] = i

wran_graph = [[0]*n]
for _ in range(n):
    input_list = [0]+list(map(lambda x: wran_length[x] if x!="0" else 0, input().rstrip()))
    wran_graph.append(input_list)
    
edges = []
for i in range(1, n+1):
    for j in range(1, n+1):
        total_length+=wran_graph[i][j]
        edges.append((wran_graph[i][j], i, j))
        
edges.sort()
d_edges = deque(edges)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: parent[b]=a
    else: parent[a]=b

parent = list(range(n+1))
use_edges, used_wran_length = 0, 0
 
while use_edges<n-1 and d_edges:
    cost, a, b = d_edges.popleft()
    if a==b or cost==0: continue
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        used_wran_length+=cost
        use_edges+=1

if use_edges==n-1:
    print(total_length-used_wran_length)
else:
    print(-1)