import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    input_list = list(map(int, input().split()))[0:-1]
    for i in range(1, len(input_list), 2):
        graph[input_list[0]].append((input_list[i], input_list[i+1]))
'''
 문제의 메인 아이디어는 노드 탐색의 끝을 찾는다면 트리 지름을 이루는
 두 노드 중 하나의 노드에 도달한다는 것
'''

def bfs(graph, start, visited):
    q = deque([(0, start)])
    distance = [0]*(len(graph))
    max_cost, max_idx = 0, 0
    visited[start] = True
    while q:
        cost, node = q.popleft()
        for nb, c in graph[node]:
            if not visited[nb]:
                distance[nb] = cost+c
                q.append((cost+c, nb))
                visited[nb] = True
                if max_cost < cost+c:
                    max_cost = cost+c
                    max_idx = nb
                
    return max_cost, max_idx

visited=[False]*(n+1)
cur_max, next_idx = bfs(graph, 1, visited)
visited=[False]*(n+1)
print(bfs(graph, next_idx, visited)[0])