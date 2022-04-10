import sys
import copy
from collections import deque
from itertools import combinations as comb
input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
points = []

for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            points.append((i,j))
            
available_points = list(comb(points, 3))

def bfs(graph):
    q=deque([])
    for i in range(n):
        for j in range(m):
            if graph[i][j]==2:
                q.append((i,j))
    while q:
        now_i, now_j = q.popleft()
        for delta in [(1,0),(-1,0),(0,1),(0,-1)]:    # Up, Down, Right, Left
            dx, dy = delta
            x, y = now_i+dx, now_j+dy
            if x<0 or y<0 or x>(n-1) or y>(m-1):
                continue
            if graph[x][y]==0:
                graph[x][y]=2
                q.append((x,y))
    return graph
        
max_0 = 0
dummy_comb, dummy_graph = None, None
for comb_point in available_points:
    count_zero = 0
    graph_copy = copy.deepcopy(graph)
    
    for p in comb_point:
        i, j = p
        graph_copy[i][j] = 1
        
    result_graph = bfs(graph_copy)
    
    for arr in result_graph:
        count_zero += arr.count(0)
    
    if count_zero > max_0:
        max_0 = count_zero
        dummy_comb = comb_point
        dummy_graph = result_graph

print(max_0)