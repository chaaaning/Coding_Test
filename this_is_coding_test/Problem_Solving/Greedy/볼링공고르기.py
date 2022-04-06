import sys
from itertools import combinations as comb

def is_unique(tup):
    if len(tup) == len(set(tup)):
        return True
    return False

input = sys.stdin.readline

n, m = map(int, input().split())
balls = list(map(int, input().split()))

# count = 0
# total = list(comb(balls, 2))
# total_len = len(total)
# for i in range(0, len(total)):
#     if not is_unique(total[i]):
#         total_len-=1

# print(total_len)

result = len(list(comb(balls, 2)))
count = 0
for i in range(1,m+1):
    if balls.count(i) > 1:
        count+=1
print(result - count)

