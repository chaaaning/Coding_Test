import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

q = deque([])
result = []

for i, val in enumerate(arr):
    if not q:
        q.append((i, val))
        result.append(q[0][1])
        continue
    if i-q[0][0]>=L:
        q.popleft()
    while True:
        if not q:
            q.append((i, val))
            break
        cur_i, cur_val = q[-1]
        if val>=cur_val:
            q.append((i, val))
            break
        else:
            q.pop()
    if q:
        result.append(q[0][1])
    
for r in result:
    print(r, end=" ")