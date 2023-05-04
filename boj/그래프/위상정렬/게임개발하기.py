import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
times = [0]


for i in range(1, n+1):
    input_vals = list(map(int, input().split()))
    for j, val in enumerate(input_vals):
        if j==0:
            times.append(val)
        elif val==-1:
            break
        else:
            graph[val].append(i)
            indegree[i]+=1
          
def topology_sort(graph, indegree, times):
    q = deque([])
    result = [0]*(n+1)
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        node = q.popleft()
        for next in graph[node]:
            indegree[next]-=1
            # Highlight
            result[next] = max(result[next], times[node]+result[node])
            if indegree[next]==0:
                q.append(next)
    return result

res = topology_sort(graph, indegree, times)

for i in range(1, n+1):
    print(res[i]+times[i])