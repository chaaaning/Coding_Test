import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph, data = [], []

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] != 0:
            data.append((arr[j],0,i,j))
    graph.append(arr)
    
data.sort()
q = deque(data)

s, x, y = map(int, input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]     # up, down right, left
while q:
    virus ,time, now_x, now_y = q.popleft()
    if time == s:
        break
    for i,j in zip(dx, dy):
        nx, ny = now_x+i, now_y+j
        if nx<0 or ny<0 or nx>(n-1) or ny>(n-1):
            continue
        if graph[nx][ny]==0:
            q.append((virus, time+1, nx, ny))
            graph[nx][ny] = virus

print(graph[x-1][y-1])

"""
문제를 잘 읽자. 런타임 에러로 index error가 지속적으로 발생.
해당 부분은 n x n 행렬을 n x m 으로 잘 못 이해한데서 오는 에러 이다.
m은 바이러스의 수이다. 또한 첫번째로 작성한 코드는 시간과 낮은 수의 바이러스 번호로 인해
우선순위 큐로 bfs를 구현했지만, 첫 번째 순서만 정렬이 되어 있으면 되기 때문에
deque로도 충분히 구현할 수 있는 bfs이다. 시간을 너무 허비하지 말자. 
"""