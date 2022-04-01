import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))  # connect_node, cost
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # cost, node
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for connect in graph[now]:
            cost = connect[1] + dist
            if cost < distance[connect[0]]:
                distance[connect[0]] = cost
                heapq.heappush(q, (cost, connect[0]))

dijkstra(start)
num_of_node, total_time = 0, 0

for time in distance[1:]:
    if time < INF:
        num_of_node += 1
    if total_time < time:
        print(total_time, time)
        total_time = time
        print(total_time)

print(num_of_node-1, total_time)