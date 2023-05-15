'''
7 8
0 0 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = [[False]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, x, y, visited, count):
    visited[x][y] = True
    graph[x][y] = count
    for i in range(4):
        cur_x, cur_y = x+dx[i], y+dy[i]
        if cur_x<0 or cur_x>n-1 or cur_y<0 or cur_y>m-1:
            continue
        if not visited[cur_x][cur_y] and graph[cur_x][cur_y]!=0:
            dfs(graph, cur_x, cur_y, visited, count)

island_num = 1
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0 and not visited[i][j]:
            dfs(graph, i, j, visited, island_num)
            island_num+=1

distance = [[sys.maxsize]*(island_num) for _ in range(island_num)]

def calc_distance(arr):
    start, end, dist = 0, 0, 0
    for val in arr:
        if start!=0 and end!=0 and start==0:
            continue
        elif val!=0 and start==0:
            start=val
        elif val==0 and start!=0:
            dist+=1
        elif val!=0 and end==0:
            end=val
            if dist>1:
                save_dist = min(distance[start][end], dist)
                distance[start][end] = save_dist
                distance[end][start] = save_dist
            start, end, dist = end, 0, 0
# search rows
for i in range(n):
    row = graph[i]
    calc_distance(row)

# search cols
for c in range(m):
    cols_list = []
    for r in range(n):
        cols_list.append(graph[r][c])
    calc_distance(cols_list)

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: parent[b]=a
    else: parent[a]=b

parent = [i for i in range(island_num)]
edges = []
for i in range(1, island_num):
    for j in range(i, island_num):
        if distance[i][j]!=sys.maxsize:
            edges.append((distance[i][j], i, j))
            
edges.sort()
result, use_edges = 0, 0
for cost, a, b in edges:
    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost
        use_edges+=1

print(result if use_edges==island_num-2 else -1)