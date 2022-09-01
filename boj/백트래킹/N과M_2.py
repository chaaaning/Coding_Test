import sys
from itertools import combinations as comb

input = sys.stdin.readline
n, m = map(int, input().split())

target = [i for i in range(1, n+1)]
result = comb(target, m)

for tup in result:
    for i in range(m):
        print(tup[i], end=" ")
    print()