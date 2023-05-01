import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b: parent[a] = b
    else: parent[b] = a

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
result = []

for _ in range(m):
    signal, a, b = map(int, input().split())
    if signal == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a)==find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")
            
for r in result:
    print(r)