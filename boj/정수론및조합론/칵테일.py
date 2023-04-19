import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]

def get_gcd(x, y):
    if y==0:
        return x
    else:
        return get_gcd(y, x%y)
    
lcm = 1
for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    lcm *= (p*q)//get_gcd(p, q)
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))

result = [0]*n
visited = [False]*n
result[0] = lcm

def dfs(graph, v, visited):
    visited[v] = True
    for next in graph[v]:
        node, a, b = next
        if not visited[node]:
            result[node] = result[v]*b//a
            dfs(graph, node, visited)
            
dfs(graph, 0, visited)

gcd = 0
for i, r in enumerate(result):
    if i==0:
        continue
    elif i==1:
        gcd = get_gcd(result[i-1], r)
    else:
        gcd = get_gcd(gcd, r)
        
for r in result:
    print(r//gcd, end=" ")