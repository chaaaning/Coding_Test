import sys
from heapq import heappop as pop
from heapq import heappush as push

input = sys.stdin.readline
INF = int(1e8)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    
start, end = map(int, input().split())

def djikstra(graph, distance):
    q = []
    push(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, node = pop(q)
        if distance[node] < dist:
            continue
        for next, cost in graph[node]:
            t_cost = cost+dist
            if t_cost < distance[next]:
                distance[next]=t_cost
                push(q, (t_cost, next))
                
    return distance[end]

print(djikstra(graph, distance))