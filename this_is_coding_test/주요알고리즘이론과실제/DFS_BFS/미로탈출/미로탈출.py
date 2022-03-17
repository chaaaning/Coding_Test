from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
    
cur_x, cur_y = 0, 0

dx = [0,0,1,-1] # R L D U
dy = [1,-1,0,0]

queue = deque([[cur_x, cur_y]])
count_q = deque([1])
counting_num = 1
graph[cur_x][cur_y] = counting_num

while queue:
    counting_num = count_q.popleft()
    can_loc = queue.popleft()

    for i in range(4):
        can_x = can_loc[0]+dx[i]
        can_y = can_loc[1]+dy[i]
        
        if (can_x >= 0) and (can_x < n) and (can_y >= 0) and (can_y < m):
            if graph[can_x][can_y] == 1 and (can_x!=0 or can_y!=0):
                queue.append([can_x, can_y])
                count_q.append(counting_num+1)
                graph[can_x][can_y] = counting_num+1
                
    if graph[n-1][m-1] != 1: break
                
print(graph[n-1][m-1])