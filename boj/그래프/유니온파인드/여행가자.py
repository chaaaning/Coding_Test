import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []
parent = [i for i in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: parent[b]=a
    else: parent[a]=b
    
for i in range(n):
    for j in range(i, n):
        if graph[i][j]==1:
            union_parent(parent, i, j)

travels = list(map(int, input().split()))

possible = True
for i, t in enumerate(travels):
    convert_t = t-1
    if i==0:
        p = find_parent(parent, convert_t)
    else:
        if p!=find_parent(parent, convert_t):
            possible=False
            break

if possible: print("YES")
else: print("NO")