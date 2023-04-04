import sys
from heapq import heappush as push
from heapq import heappop as pop

input = sys.stdin.readline

n = int(input())

num_list = []

for _ in range(n):
    a = int(input())
    push(num_list, a)

answer = 0
while num_list:
    min_fst = pop(num_list)
    try:
        min_scd = pop(num_list)
        summation = min_fst + min_scd
        push(num_list, summation)
        answer+=summation
    except:
        break

print(answer)

# 2 2 3 3 = 2 3 / 2 3 / 5 5 = 20