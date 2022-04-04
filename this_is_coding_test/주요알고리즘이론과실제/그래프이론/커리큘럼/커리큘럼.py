import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)
times = [0] * (n+1)


for i in range(1, n+1):
    # 시간, 진입노드1, 진입노드2, ... ,-1
    subject_list = list(map(int, input().split()))
    subject_list.pop(-1)
    times[i] = subject_list.pop(0)
    for ind_sub in subject_list:
        graph[ind_sub].append(i)
        indegree[i] += 1
        
print(f"graph: {graph}\nindegree: {indegree}\ntimes: {times}")
print() 

def topology_sort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now = q.popleft()
        print(f'now: {now}\tgraph: {graph[now]}')
        
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now]+times[i]) ### KEY POINT!

            if indegree[i] == 0:
                q.append(i)
        
            
    return result

print(topology_sort())
