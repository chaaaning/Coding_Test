import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(n):
    line = input().rstrip()
    graph[i] = [int(x) for x in line]

def bfs(graph, x1, x2):
    dist = 1
    q = deque([(x1, x2, dist)])
    graph[x1][x2] = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        x, y, dist = q.popleft()
        if x==n-1 and y==m-1:
            break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny, dist+1))
    return dist
print(bfs(graph, 0, 0))