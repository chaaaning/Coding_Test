import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

comb_res = list(map(lambda x: sum(x), combinations(cards, 3)))
comb_res.sort()

for i in range(len(comb_res)):
    if comb_res[i] == m:
        print(comb_res[i])
        break
    elif comb_res[0]==comb_res[-1]:
        print(comb_res[0])
        break
    elif comb_res[i] > m:
        print(comb_res[i-1])
        break
    elif comb_res[-1]<m:
        print(comb_res[-1])
        break