import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque([i for i in range(1, N+1)])

while N > 2:
    top1 = q.popleft()
    top2 = q.popleft()
    N-=1
    q.append(top2)
    
print(q[-1])