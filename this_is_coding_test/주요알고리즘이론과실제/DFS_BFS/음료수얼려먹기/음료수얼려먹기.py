n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
    
count = 0

def dfs(graph, x, y):
    graph[x][y] = 1
    for i in range(4):
        can_x, can_y = x+dx[i], y+dy[i]
        if (can_x >= 0) and (can_x < n) and (can_y >= 0) and (can_y < m):
            if graph[can_x][can_y] != 1:
                dfs(graph, can_x, can_y)
            
dx = [0, 0, 1, -1]  # R L D U        
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(graph, i, j)
            count+=1
            
        
print(count)
        
        

    