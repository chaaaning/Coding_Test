import sys

input=sys.stdin.readline

INF = sys.maxsize
n, m = map(int, input().split())
graph = []
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph.append((a, b, c))

def bf_search(graph, distance):
    distance[1] = 0
    for check in range(1, n+1):
        for node, next, cost in graph:
            if distance[node]!=INF & distance[next] > distance[node]+cost:
                if check==n: return -1
                distance[next] = distance[node]+cost
    return distance[1:]

res = bf_search(graph, distance)

if res==-1:
    print(res)
else:
    for i, r in enumerate(res):
        if i == 0:
            continue
        print(r if r!=INF else -1)