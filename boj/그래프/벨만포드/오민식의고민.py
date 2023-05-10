import sys

input = sys.stdin.readline

INF = sys.maxsize

n, start, end, m = map(int, input().split())
graph = []
costs = [-INF]*n

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
    
get_money = list(map(int, input().split()))

def bf_search(graph, costs, start, get_money):
    costs[start] = get_money[start]
    for check in range(n+101):
        for s, e, c in graph:
            if costs[s]==-INF:
                continue
            elif costs[e] < costs[s]-c+get_money[e]:
                if check<n-1:
                    costs[e] = costs[s]-c+get_money[e]
                else:
                    costs[e] = INF
            elif costs[s]==INF:
                costs[e]=INF
    return costs

res = bf_search(graph, costs, start, get_money)[end]
if res==INF:
    print("Gee")
elif res==-INF:
    print("gg")
else:
    print(res)