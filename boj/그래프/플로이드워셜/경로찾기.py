import sys

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    input_list = list(map(int, input().split()))
    graph.append(input_list)
    
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k]==1 and graph[k][b]==1:
                graph[a][b] = 1
        
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()