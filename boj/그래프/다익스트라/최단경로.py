import sys
from heapq import heappush as push
from heapq import heappop as pop

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e8)
distance = [INF]*(v+1)

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    
def djikstra(graph, distance):
    q = []
    push(q,(0, start))
    distance[start]=0
    while q:
        dist, node = pop(q)
        if distance[node] < dist:
            continue
        for next, cost in graph[node]:
            t_cost = cost+dist
            if t_cost < distance[next]:
                distance[next] = t_cost
                push(q, (t_cost, next))
    return distance[1:]

res = djikstra(graph, distance)
for r in res:
    print(r if r is not INF else "INF")