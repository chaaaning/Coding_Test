import sys
from itertools import product

input = sys.stdin.readline
n, m = map(int, input().split())

target = [i for i in range(1, n+1)]
result = product(target, repeat=m)

for tup in result:
    for i in range(m):
        print(tup[i], end=" ")
    print()