import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n, m = map(int, input().split())
truth_num = list(map(int, input().split()))

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b: parent[a] = b
    else: parent[b]= a
    
parties = []
parent = [i for i in range(n+1)]
for _ in range(m):
    p = list(map(int, input().split()))
    parties.append(p)
    if p[0]==1:
        continue
    else:
        for i in range(p[0]):
            idx = i+1
            if idx==1:
                continue
            else:
                union_parent(parent, p[idx-1], p[idx])

truth_parent = list(map(lambda x: find_parent(parent, x), truth_num[1:]))
for p in parties:
    if find_parent(parent, p[1]) in truth_parent:
        m-=1
        
print(m)