import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
INF = int(1e8)
graph = [[] for _ in range(n+1)]
distance = [[INF]*k for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))
    
def k_djikstra(graph, distance, k):
    q = []
    heapq.heappush(q, (0,1))
    # 핵심
    distance[1][0]=0
    while q:
        cost, node = heapq.heappop(q)
        for nxt, cst in graph[node]:
            total_cost = cost+cst
            if distance[nxt][k-1] > total_cost:
                distance[nxt][k-1] = total_cost
                distance[nxt].sort()
                heapq.heappush(q, (total_cost, nxt))
    result = []
    for i, d_list in enumerate(distance):
        if i==0:
            continue
        result.append(d_list[k-1] if d_list[k-1]!=INF else -1)
        
    return result

res = k_djikstra(graph, distance, k)
for r in res:
    print(r)