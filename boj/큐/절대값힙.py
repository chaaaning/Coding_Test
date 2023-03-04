import sys
from heapq import heappush as push
from heapq import heappop as pop

input = sys.stdin.readline
N = int(input())
result, q = [], []

for _ in range(N):
    a = int(input())
    if a!=0:
        sign_bit = 1 if a>0 else 0
        push(q, (abs(a), sign_bit))
    else:
        try:
            val, sign = pop(q)
            result.append(val if sign==1 else -val)
        except:
            result.append(0)
for r in result:
    print(r)